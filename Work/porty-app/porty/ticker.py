# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:10:21 2020

@author: Gokhale
"""

from follow import follow
import csv
import report
import tableformat

def select_columns(rows,indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows,types):
    for row in rows:
        yield [ func(val) for func,val in zip(types,row)]
        
def make_dicts(rows,headers):
    for row in rows:
        yield dict(zip(headers,row))

def filter_symbols(rows,names):
    for row in rows:
        # rows is a generator of dictionaries 
        # names is a Portfolio object. It implements __contains__
        # therefore we can do row['name'] in names:
        if row['name'] in names:
            yield row
            
def format_and_print_rows(rows,fmt):
    formatter=tableformat.create_formatter(fmt)
    for row in rows:
        rowdata =(str(rr) for rr in row.values())
        formatter.row(rowdata)
        yield rowdata
            
def parse_stock_data(lines,pf,fmt):
    rows = csv.reader(lines)
#   rows = select_columns(rows,[0,1,4])
#   rows = convert_types(rows,[str, float, float])
#   rows = make_dicts(rows,['name','price','change'])
#   rows = filter_symbols(rows,pf)
#   rowdata = format_and_print_rows(rows,fmt)

    types     = [str, float, float]
    headers   = ['name','price','change']
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(headers)
    selected_rows    = ([ row[index] for index in [0,1,4]] for row in rows)
    converted_rows   = ([ func(val)  for func,val in zip(types,row) ] for row in selected_rows)
    dictionary_gen   = ({ key:value  for key,value in zip(headers,row)} for row in converted_rows)
    filter_dict_gen  = ( dd for dd in dictionary_gen if dd['name'] in pf)
    values_list_gen  = ( list(dd.values()) for dd in filter_dict_gen )
    list_string_gen  = ( [str(ss[ii]) for ii in range(len(ss))] for ss in values_list_gen)
    for ll in list_string_gen:
        formatter.row(ll)    
#    return rowdata

def ticker(portfile,logfile,fmt):
    pf    = report.read_portfolio(portfile)
    lines = follow(logfile)
    parse_stock_data(lines,pf,fmt)
    

if __name__ == '__main__':
    # my portfolio file
    portfile='../Data/portfolio.csv'
    # logfile generated by stockmarket simulator
    logfile='../Data/stocklog.csv'
    # format for output
    fmt='txt'
    ticker(portfile,logfile,fmt)
    
    