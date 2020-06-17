# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:52:49 2020

@author: Gokhale
"""


class Portfolio:
    def __init__(self,holdings:list):
        self._holdings = holdings
    
    def __iter__(self):
        # list is not an iterator because it does not implement __next__
        # it implements __iter__ from which we can get an iterator
        return self._holdings.__iter__()
    
    def __len__(self):
        return len(self._holdings)
    
    def __getitem__(self,index):
        return self._holdings[index]
    
    def __contains__(self,name):
        return any([s.name == name for s in self._holdings])
    
        
    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])
    
    
    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares