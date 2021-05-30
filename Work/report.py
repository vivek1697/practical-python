# report.py
#
# Exercise 3.1
import csv

#Function create a portfolio dic from the file   
def read_portfolio(filename):
    portfolio = []
    #Open the csv file and read the data from it 
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        #Run a loop on each row convert it into the dic and append that into the portfolio list
        for row in rows:
            record = dict(zip(headers, row))
            holding = {'name' : record['name'], 'shares' : int(record['shares']), 'price'  : float(record['price'])}
            portfolio.append(holding)
    return portfolio

#Function create a prices dic from the file       
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

#Function Create a report from Portfolio and Prices
def make_report(portfolio, prices):
    report = []
    for row in portfolio:
        holding = (row['name'], row['shares'], float(prices[row['name']]), round(float(prices[row['name']]) - row['price'],2))
        report.append(holding)
    
    return report    

#Function to print the values
def print_report(report):
    #Code creates a table view for values
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print((10*'_' + ' ') * len(headers))
    for name, shares, price, change in report:
        new_price = "$" + str(price)
        print(f'{name:>10s} {shares:>10d} {new_price:>10s} {change:>10.2f}')
    return    

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
print_report(report) 