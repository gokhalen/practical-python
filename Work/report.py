# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []
    
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            name, shares, price = row
            dd = {"name":name,"shares":int(shares),"price":float(price)}
            portfolio.append(dd)
    
    return portfolio
    
portfolio=read_portfolio('Data/portfolio.csv')

'''
total=0.0
for dd in portfolio:
     shares = dd["shares"]
     price  = dd["price"]
     total += shares*price

print(total)
'''