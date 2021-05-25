# report.py
#
# Exercise 2.5
import csv

def read_portfolio(filename):
    
    portfolio = []
    #Open the csv file and read the data from it 
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        #Run a loop on each row convert it into the dic and append that into the portfolio list
        for row in rows:
            holding = {'name' : row[0], 'shares' : int(row[1]), 'price'  : float(row[2])}
            portfolio.append(holding)
        #Calculate the total valuation of Portfolio    
        total = 0.0
        for s in portfolio:
           total += s['shares'] * s['price']
    return print(total)

read_portfolio('Data/portfolio.csv')

