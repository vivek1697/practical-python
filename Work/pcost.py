# pcost.py
#
# Exercise 2.15
import sys
import csv

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    total_sum = 0
    for rowno, row in enumerate(rows, start=1):
        try:
            total_sum = total_sum + float(row[1]) * float(row[2])
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')
    return total_sum

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)

