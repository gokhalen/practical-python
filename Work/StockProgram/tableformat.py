# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:23:32 2020

@author: Gokhale
"""

class FormatError(Exception):
    
    def __init__ (self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None
        print('__init__ in FormatError called')
    
    def __str__(self):
        print('calling str')
        if self.message:
            return f'FormatError,{self.message}'
        else:
            return 'FormatError has been raised'
    
    pass

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
    try:
        if(fmt == 'txt'):
            formatter = TextTableFormatter()
        elif (fmt == 'csv'):
            formatter = CSVTableFormatter()
        elif (fmt == 'html'):
            formatter = HTMLTableFormatter()
        else:
            raise FormatError(f'Unknown format {fmt}')
    except FormatError as e:
        raise
       
    return formatter
        
def print_table(portfolio,formatter,select=['name','shares','price']):
    
# contrary to its name, formatter does not format
# it assumes its input is an iterator yielding formatted strings 

    formatter.headings(select)
    
    for pf in portfolio:
        ll = []
        for ss in select:
            temp = getattr(pf,ss)
            if (type(temp)==str):
                ll.append(temp)
            elif (type(temp) == int):
                ll.append(str(temp))
            elif (type(temp) == float):
                ll.append(f'{temp:0.2f}')
            else:
                raise RuntimeError('Type conversion failed in __name__')
        formatter.row(ll)
        
    
    