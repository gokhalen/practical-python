# report.py
#
# Exercise 2.4

import csv
import sys
import stock
import tableformat
import portfolio

def read_portfolio(filename):
    '''
    returns Portfolio object
    '''
    stocklist = []
    
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            drow = dict(zip(headers,row))
            name   = drow["name"]
            shares = drow["shares"]
            price  = drow["price"]
            dd = stock.Stock(name,shares,price)
            stocklist.append(dd)

    pf = portfolio.Portfolio(stocklist)
    return pf


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
        name            = pf.name
        quantity        = pf.shares
        purchase_price  = pf.price
        purchase_total += quantity*purchase_price
        current_price   = prices[name].price
        current_total  += quantity*current_price
        change          = (current_price - purchase_price)
        stock_table.append((name,quantity,current_price,change))
    
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
                     prices_filename='../Data/prices.csv',fmt='txt'):
    
    from fileparse import parse_csv_iterable

    with open(portfolio_filename) as f:
        portfolio = parse_csv_iterable(f,select=['name','shares','price'],types=[str,int,float],has_headers=True)
        
    with open(prices_filename) as f:
        prices = parse_csv_iterable(f,has_headers=False)
    
    
    current_total,purchase_total,stock_table = make_report(portfolio,prices)

    print(f'Current portfolio value = {current_total}, '
          f'Cost portfolio value = {purchase_total}')
    
    formatter = tableformat.create_formatter(fmt)
    print_report(stock_table,formatter)


def print_report(reportdata,formatter):
    '''
    Print a nicely formatted table from a list of (name,shares,price)
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    
    for name,shares,price,change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}',f'{change:0.2f}']
        formatter.row(rowdata)
    
def print_report_old(ll):
    '''
    Takes list of tuple generated by make_report and pretty prints it
    Unlike the dictionary in pretty_print_prices, 
    this tuple doesn't have header information 
    '''
    if len(ll) >= 1 :
        ss=(f'{"Name":>10}'
            f' {"Shares":>10}'
            f' {"Price":>10}'
            f' {"Change":>10}'
            )
        print(ss)
        ss = f'{"":_>43}'
        print(ss)          
        
        for tt in ll:
            name   = tt[0]
            shares = tt[1]
            price  = tt[2]
            change = tt[3]
            
            ss=(f'{name:>10}'
                f' {shares:>10d}'
                f' {price:>10.2f}'
                f' {change:>10.2f}'
                )
            print(ss)
            
    
def main(args:list):
    if args:
        portfolio_filename = args[0]
        prices_filename    = args[1]
        fmt                = args[2]
    else:
        portfolio_filename = '../Data/portfolio.csv'
        prices_filename    = '../Data/prices.csv'
        fmt                = 'txt' 
    portfolio_report(portfolio_filename,prices_filename,fmt=fmt)

if __name__ == '__main__':
    args = []
    
    if (len(sys.argv) < 4):
        print('Usage: python report.py <portfolio_filename> <prices_filename> <fmt>')
        print('Using defaults ../Data/portfolio.csv ../Data/prices.csv fmt="txt"')
    else:
        args = sys.argv[1:4]
    
    main(args)    