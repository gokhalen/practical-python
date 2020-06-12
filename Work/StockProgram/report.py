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
            drow = dict(zip(headers,row))
            name   = drow["name"]
            shares = drow["shares"]
            price  = drow["price"]
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

def portfolio_report(portfolio_filename='../Data/portfolio.csv',
                     prices_filename='../Data/prices.csv'):
    
    from report import read_portfolio, make_report,read_prices
#    from readprices import read_prices
    from pretty_print_prices import print_report
    from fileparse import parse_csv

#   portfolio = read_portfolio(portfolio_filename) 
#   prices    = read_prices(prices_filename)
    
    portfolio = parse_csv(portfolio_filename,select=['name','shares','price'],types=[str,int,float])
    prices    = parse_csv(prices_filename,has_headers=False)

    current_total,purchase_total,stock_table = make_report(portfolio,prices)       

    print(f'Current portfolio value = {current_total}, '
          f'Cost portfolio value = {purchase_total}')

    print_report(stock_table)