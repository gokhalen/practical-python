# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:23:32 2020

@author: Gokhale
"""

class TableFormatter:
    def headings(self,headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()
        
    def row(self,rowdata):
        '''
        Emit a single row of table data
        '''
        
        raise NotImplementedError()
        
    
class TextTableFormatter(TableFormatter):
    
    def headings(self,headers):
        for h in headers:
            print(f'{h:>10s}',end=' ')
# call print to get a newline
        print()
        print(('-'*10+' ')*len(headers))
        
    def row(self,rowdata):
        for d in rowdata:
            print(f'{d:>10s}',end=' ')
        print()

class CSVTableFormatter(TableFormatter):

    def headings(self,headers):
        print(','.join(headers))
    
    def row(self,rowdata):
        print(','.join(rowdata))
        
class HTMLTableFormatter(TableFormatter):
    
    def headings(self,headers):
        print('<tr>',end="")
        for h in headers:
            print(f'<th>{h}</th>',end="")
        print('</tr><br>')
    
    def row(self,rowdata):
        print('<tr>',end="")
        for r in rowdata:
            print(f'<th>{r}</th>',end="")
        print('</tr><br>')

def create_formatter(fmt):
    
    if(fmt == 'txt'):
        formatter = TextTableFormatter()
    elif (fmt == 'csv'):
        formatter = CSVTableFormatter()
    elif (fmt == 'html'):
        formatter = HTMLTableFormatter()
    else:
        raise RunTimeError(f'Unknown format {formatter}')    
        
    return formatter
        
    