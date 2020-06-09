# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    with open(filename,'rt') as f:
        rows   = csv.reader(f)
        header = next(rows)
        total_cost = 0.0
        for rowno,row in enumerate(rows,start=1):
            record=dict(zip(header,row))
            try:
                nshares=int(record['shares'])
                price  =float(record['price'])
            except ValueError:
                print(f'Row{rowno}: Bad row: {row}')
            total_cost += nshares*price 
            
    return total_cost

if len(sys.argv) == 2 :
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

total_cost=portfolio_cost(filename)

print('total_cost=',total_cost)
