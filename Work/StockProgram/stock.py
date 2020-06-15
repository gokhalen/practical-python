# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:40:15 2020

@author: Gokhale
"""

class Stock(object):
    
    def __init__(self,name:str,shares:int,price:float):
        self.name   = str.upper(name)
        self.shares = int(shares)
        self.price  = float(price)
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, number):
        self.shares -= number
        return self.shares
    
    def __str__(self):
        return f'({self.name},{self.shares},{self.price})'
    
    def __repr__(self):  
        return f'stock.Stock({self.name},{self.shares},{self.price})'
    
class MyStock(Stock):
    
    def __init__(self,name,shares,price,factor):
        super().__init__(name,shares,price)
        self.factor = factor
    
    def panic(self): 
        return self.sell(self.shares)
        
    def cost(self):
        actual_cost = super().cost()
        return self.factor*actual_cost

class MyClass():
    xx = 1
    def __init__(self,var):
        self.xx = var
        
    def __repr__(self):
        return f'xx={__class__.xx}, self.xx={self.xx}'