# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:19:50 2020

@author: Gokhale

Uses functions developed earlier in report.py and readprices.py
to calculate current value of portfolio

"""

from report import read_portfolio
from readprices import read_prices

portfolio=read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

purchase_total = 0
current_total  = 0

for pf in portfolio:
    name=pf['name']
    quantity        = pf["shares"]
    purchase_price  = pf["price"]
    purchase_total += quantity*purchase_price
    current_price   = prices[name]
    current_total  += quantity*current_price
    

print(f'Current portfolio value = {current_total}, '
      f'Cost portfolio value = {purchase_total}')