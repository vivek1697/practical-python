# pcost.py
#
# Exercise 3.16
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

def main(argv):
    if len(sys.argv) != 2:
        raise SystemExit(f'missing arguments for {sys.argv[0]} ')
    filename = argv[1]
        
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
   




