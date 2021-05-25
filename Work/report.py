# report.py
#
# Exercise 2.9
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
    return portfolio
       
def read_prices(filename):
    prices = {}
    #Open the csv file and read the data from it 
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        
        #Run a loop on each row append into the dic
        for row in rows:
            if row != []:
                k, v = row
                prices[k] = v
       
    return prices

def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        holding = (row['name'], row['shares'], row['price'], round(float(prices[row['name']]) - row['price'],2))
        report.append(holding)
    
    return report    

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
for r in report:
    print(r)