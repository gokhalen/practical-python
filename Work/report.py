# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''
    returns portfolio as a list of dictionaries
    '''
    portfolio = []
    
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            name, shares, price = row
            dd = {"name":name,"shares":int(shares),"price":float(price)}
            portfolio.append(dd)
    
    return portfolio


def make_report(portfolio,prices):
    '''
    returns total purchase price (purchase_total) 
            current valuation    (current_total)
            table (list of tuple) to be printed 
            modifies portfolio to add a new item "change"
    '''
    current_total  = 0.0
    purchase_total = 0.0
    stock_table    = []
    for pf in portfolio:
        name=pf['name']
        quantity        = pf["shares"]
        purchase_price  = pf["price"]
        purchase_total += quantity*purchase_price
        current_price   = prices[name]
        current_total  += quantity*current_price
        pf["change"]    = (current_price - purchase_price)
        stock_table.append((name,quantity,current_price,pf["change"]))

    return current_total,purchase_total,stock_table 
