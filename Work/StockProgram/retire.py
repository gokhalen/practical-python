# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:19:50 2020

@author: Gokhale

Uses functions developed earlier in report.py and readprices.py
to calculate current value of portfolio
pretty_print_prices.py,readprices.py,retire.py

"""

def portfolio_report(portfolio_filename='../Data/portfolio.csv',
                     prices_filename='../Data/prices.csv'):
    
    from report import read_portfolio, make_report
    from readprices import read_prices
    from pretty_print_prices import print_report

    portfolio = read_portfolio(portfolio_filename) 
    prices    = read_prices(prices_filename)

    current_total,purchase_total,stock_table = make_report(portfolio,prices)       

    print(f'Current portfolio value = {current_total}, '
          f'Cost portfolio value = {purchase_total}')

    print_report(stock_table)