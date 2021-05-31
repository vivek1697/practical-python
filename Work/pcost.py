# pcost.py
#
# Exercise 2.15
import sys
#import csv
import report

def portfolio_cost(filename):
    total_cost = 0
    records = report.read_portfolio(filename)
    for record in records:
        nshares = int(record['shares'])
        price = float(record['price'])
        total_cost += nshares * price
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/portfoliodate.csv')
print('Total cost:', cost)

