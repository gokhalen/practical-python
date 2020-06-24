# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:52:49 2020

@author: Gokhale
"""
from . import stock
from . import fileparse

class Portfolio:
    def __init__(self):
        self._holdings = []
    
    def __iter__(self):
        # list is not an iterator because it does not implement __next__
        # it implements __iter__ from which we can get an iterator
        return self._holdings.__iter__()
    
    def __len__(self):
        return len(self._holdings)
    
    def __getitem__(self,index):
        return self._holdings[index]
    
    def __contains__(self,name):
        return any((s.name == name for s in self._holdings))
    
    def __str__(self):
        string=f'{"-"*20}\n'
        for stock in self._holdings:
            string += str(stock)+'\n'
        string +=f'{"-"*20}\n'  
        return string
    
    def append(self,holding):
        if not isinstance(holding,stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)
    
    @property
    def total_cost(self):
        return sum((s.cost for s in self._holdings))
   
    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
    
    def sortpf(self,key='name',rev=False):
        if (key=='name'):
            self._holdings.sort(key=lambda s:s.name,reverse=rev)
        elif (key == 'price'):
            self._holdings.sort(key=lambda s:s.price,reverse=rev)
        elif (key == 'shares'):
            self._holdings.sort(key=lambda s:s.shares,reverse=rev)
        
    @classmethod
    def from_csv(cls,lines,**opts):
        # call the consttructor and make an object
        self = cls()
        portdicts = fileparse.parse_csv_iterable(lines,select=['name','shares','price'],
                                       types=[str,int,float],has_headers=True,
                                       **opts)
        for d in portdicts:
            self.append(stock.Stock(**d))
        
        return self 
        
            
        
        
    