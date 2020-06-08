# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:41:04 2020

@author: Gokhale
"""

import csv

def read_prices(filename):
    
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        price_dict = {}
        for row in rows:
            if (len(row) == 2):
                name,price=row
            price=float(price)
            price_dict[name]=price
            
    return price_dict

#prices = read_prices('Data/prices.csv')
        
