# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:48:50 2020

@author: Gokhale
"""

import csv
import sys
import gzip
from   typing import Iterable,Union
import stock
import portfolio

def check_consistency(has_headers,select):
    try:    
       if (has_headers==False) and (select != None):
           raise RuntimeError("Select argument requires has_headers=True")
    except RuntimeError as e:
       raise
    

def check_consistency_header_types(select:list,types:list):
     assert(select !=None),'Need to specify fields to select'
              
     #if types are specified for conversion, then they must be equal to number of fields        
     if types:
         assert (len(select) == len(types)), 'Length of select is not equal to length of types'

def find_fields_types(rows:Union[Iterable,list],select:list,types:list,delimiter=','):
#   if rows is created using 'raw','csvgz' it is _io.TextIOWrapper: can use next
#   if rows is created using 'list','cvs' it is a list, a list is not an iterator
#   so we need to check whether it is an iterator or not
    try:
        iter(rows)
        headers = next(rows)
    except TypeError:
        # assume rows is a list
        headers = rows.pop(0)
        
    if (type(headers)==str):
        headers = headers.strip('\n')
        headers = headers.split(delimiter)
        
    foundfields = []
    foundtypes  = []
    
    for ii,ss in enumerate(select):
        if ss not in headers:
            print(f'User specified field {ss} not found')
            sys.stdout.flush()
        else:
            foundfields.append(ss)
            if types:
                foundtypes.append(types[ii])
    
    if not foundfields: raise RuntimeError("None of the specified fields were found")
    return headers,foundfields,foundtypes


def parse_row_with_headers(rows:Iterable,foundfields,foundtypes,indices,delimiter=',',silence_errors=False):
    '''
    Creates a Portfolio of Stock objects. While the fucntion is smart enough to understand
    to select only those fields which are specified by the user, the last line 
    which creates stocklist assumes the existence of the fields 'name', 'shares','price'
    '''
    assert (type(rows) != str),'parse_row_with_headers expects iterable object generated from a file or a list of strings'
    records = []
    for rowno,row in enumerate(rows):
        # row is either a list of strings or a delimited string
        # if blank row then skip to the next row
        if not row:
            continue
        
        # if row is a string then split by delimiter and convert to list
#        print('type row = ',type(row))      
        if ( type(row)==str):
            row = row.strip('\n')
            row = row.split(delimiter)
        # if types were specified, do conversion
        if foundtypes:
            try:
                # Note the numbers in row are strings
                # int('32.2') throws ValueError
                record    = { ff:tt(row[ii]) for ff,ii,tt in zip(foundfields,indices,foundtypes)}
            except ValueError:
                record = {}
                if not silence_errors: print(f'Bad data in on line {rowno+2}')
        else:   
            record = { ff:row[ii] for ff,ii in zip(foundfields,indices) }
            # do not append blank records
        if record: records.append(record)
        
    stocklist=[stock.Stock(dd['name'],dd['shares'], dd['price']) for dd in records]
    pf=portfolio.Portfolio(stocklist)
            
    return pf

def parse_row_without_headers(rows:Iterable,delimiter=','):
    '''
        reads a prices file to return a dictionary of stocks
        e.g.  
              AA,492.1
              GOOG,399.1
        will be 
        { 'AA':Stock('AA',0,492.1}
        { 'GOOG': Stock('GOOG',0,399.1)}
    '''    
    records = {}
    assert (type(rows) != str),'parse_row_without_headers expects iterable object generated from a file or a list of strings'
    for row in rows:
        # row is either a list of strings or a delimited string
        # if blank row then skip to the next row
        if not row:
            continue
        if (type(row)==str):
            row = row.strip('\n')
            row = row.split(delimiter)
            # if the row is a string '' on the last line 
            # creates a list with an empty string
            # such a list does not evaluate to False
        if row[0] == '':
            row = []
        if row:   
            records[row[0]]=float(row[1])
            
    stocklist = { key:stock.Stock(key,0,value) for key,value in records.items()}
    return stocklist

def parse_csv(filename:str,select:list=None,
              types=[],has_headers=True,delimiter=",",silence_errors=False):
    '''
    Parse a CSV file into a list of records
    filename: file to be opened
    select:  list of fields to be selected
    Notes: types defaults to empty list. Do NOT mutate it (Amy Hanlon's talk)
    '''
    check_consistency(has_headers,select)
       
    with open(filename) as f:
        rows    = csv.reader(f,delimiter=delimiter)
        records = []        

        if has_headers:
            
            check_consistency_header_types(select,types)
            headers, foundfields, foundtypes=find_fields_types(rows,select,types,delimiter)
            indices = [ headers.index(ff) for ff in foundfields ]
            records = parse_row_with_headers(rows,foundfields,foundtypes,indices,delimiter,silence_errors)
  
        else:
             # case of no headers
             records = parse_row_without_headers(rows,delimiter)
    return records


def parse_csv_iterable(rows:Iterable,select:list=None,
              types=[],has_headers=True,delimiter=",",silence_errors=False):
    
    check_consistency(has_headers,select)
    records = []
    
    if has_headers:
        check_consistency_header_types(select,types)
        headers, foundfields, foundtypes=find_fields_types(rows,select,types,delimiter)
        indices = [ headers.index(ff) for ff in foundfields ]
        records = parse_row_with_headers(rows,foundfields,foundtypes,indices,delimiter,silence_errors)
    else:
        records = parse_row_without_headers(rows,delimiter)

    return records

def test_parse_csv_iterable(mode='raw'):
    
    if mode == 'raw':
        with open('../Data/portfolio.csv') as f:
            records = parse_csv_iterable(f,select=['name','shares','price'],types=[str,int,float],has_headers=True)
            
    elif mode == 'csv':
        with open('../Data/portfolio.csv') as f:
            rows    = csv.reader(f,delimiter=',')
            records = parse_csv_iterable(rows,select=['name','shares','price'],types=[str,int,float],has_headers=True)
            
    elif mode == 'csvgz':
        with gzip.open('../Data/portfolio.csv.gz','rt') as f:
            records = parse_csv_iterable(f,select=['name','shares','price'],types=[str,int,float],has_headers=True)
            
    elif mode == 'list':
        stocklist=['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
        records = parse_csv_iterable(stocklist,select=['name','shares','price'],types=[str,int,float],has_headers=True)
    
    elif mode == 'nh_raw':
        with open('../Data/prices.csv') as f:
            records = parse_csv_iterable(f,has_headers=False)
    elif mode == 'string':
        records = parse_csv_iterable('../Data/prices.csv',has_headers=False)

    print(records)
    
        