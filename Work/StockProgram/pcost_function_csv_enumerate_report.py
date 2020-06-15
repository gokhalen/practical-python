# pcost.py
#
# Exercise 1.27

import csv
import sys
import report

def portfolio_cost(filename):
    with open(filename,'rt') as f:
        rows   = csv.reader(f)
        header = next(rows)
        total_cost = 0.0
        for i,row in enumerate(rows,start=1):
            try:
                if (row[0]==''):
                    raise RuntimeError('Blank stock name')
            except RuntimeError as inst:
                print(inst.args)
            
            try:
                nn = int(row[1])
            except ValueError as inst:
                nn = 0
                print(f'ValueError in number of shares on line {i}, args=', inst.args)
                print('Setting number of shares to zero')                
            try:
                cost = float(row[2])
            except ValueError as inst:
                cost = 0
                print('ValueError in cost args, args=',inst.args)
                print('Setting cost to zero')
            total_cost += nn*cost 
            
    return total_cost

def main(args:list):
    if args:
        filename = args[0]
    else:
        filename = '../Data/portfolio.csv'
    
    print(f'filename={filename}')
    portfolio=report.read_portfolio(filename)
    total_cost = 0
    for dd in portfolio:
        total_cost += dd.price*dd.shares
    print('total_cost=',total_cost)
    
    
if __name__ == "__main__":
    args = []
    if len(sys.argv) < 2 :
        print('Usage: python <portfolio_filename>')
        print('Using default: ../Data/portfolio.csv')
    else:
        args=sys.argv[1:]
    main(args)
        

