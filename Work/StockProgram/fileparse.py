# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:48:50 2020

@author: Gokhale
"""

import csv
import sys
from typing import Iterable

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

def find_fields_types(rows:Iterable,select:list,types:list,delimiter=','):
    headers     = next(rows)
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


def parse_row_headers(rows:Iterable,foundfields,foundtypes,indices,delimiter=',',silence_errors=False):
    records = []
    for rowno,row in enumerate(rows):
        # if blank row then skip to the next row
        if not row:
            continue
        
        # if row is a string then split by delimiter and convert to list
        print('type row = ',type(row))      
        if ( type(row)==str):
            row = row.split(delimiter)
        
        # if types were specified, do conversion
        if foundtypes:
            try:
                # Note the numbers in row are strings
                # int('32.2') throws ValueError
                record = { ff:tt(row[ii]) for ff,ii,tt in zip(foundfields,indices,foundtypes)}
            except ValueError as e:
                record = {}
                if not silence_errors: print(f'Bad data in on line {rowno+2}')
        else:   
            record = { ff:row[ii] for ff,ii in zip(foundfields,indices) }
            # do not append blank records
        if record: records.append(record)
            
    return records

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
            records = parse_row_headers(rows,foundfields,foundtypes,indices,delimiter,silence_errors)
  
        else:
             # case of no headers
             # can use dict comprehension but don't know how to handle blank rows
             records = {}
             for row in rows:
                 if not row:
                     continue
                 records[row[0]]=float(row[1])
                     
    return records


def parse_csv_iterable(rows:Iterable,select:list=None,
              types=[],has_headers=True,delimiter=",",silence_errors=False):
    
    check_consistency(has_headers,select)
    records = []
    
    if has_headers:
        check_consistency_header_types(select,types)
        headers, foundfields, foundtypes=find_fields_types(rows,select,types,delimiter)
        pass
    else:
        pass
    
    return records

def test_parse_csv_iterable():
    with open('../Data/portfolio.csv') as f:
        records = parse_csv_iterable(f,select=['name','shares','price'],has_headers=True)

    print(records)
    
        