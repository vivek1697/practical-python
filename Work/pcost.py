# pcost.py
#
# Exercise 1.33
import sys
import csv

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    total_sum = 0
    for row in rows:
        try:
             total_sum = total_sum + float(row[1]) * float(row[2])
        except ValueError:
            print("Couldn't process the balnk string data")
    return total_sum

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)