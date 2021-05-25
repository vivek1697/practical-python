# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    
    portfolio = []
    #Open the csv file and read the data from it 
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        #Run a loop on each row convert it into the tuple and append that into the portfolio list
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
        #Calculate the total valuation of Portfolio    
        total = 0.0
        for s in portfolio:
            total += s[1] * s[2]
    return print(total)

read_portfolio('Data/portfolio.csv')