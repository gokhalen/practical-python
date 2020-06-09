# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:19:50 2020

@author: Gokhale

Uses functions developed earlier in report.py and readprices.py
to calculate current value of portfolio
pretty_print_prices.py,readprices.py,retire.py

"""

from report import read_portfolio, make_report
from readprices import read_prices
from pretty_print_prices import pretty_print_prices,pretty_print_prices_tuple

portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')


purchase_total = 0
current_total  = 0


current_total,purchase_total,stock_table = make_report(portfolio,prices)       

print(f'Current portfolio value = {current_total}, '
      f'Cost portfolio value = {purchase_total}')

#pretty_print_prices(portfolio)
#print("")
pretty_print_prices_tuple(stock_table)