# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:52:49 2020

@author: Gokhale
"""


class Portfolio:
    def __init__(self):
        self._holdings = holdings
        
    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])
    
    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares