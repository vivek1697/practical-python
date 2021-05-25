# report.py
#
# Exercise 2.7
import csv

def read_portfolio(filename):
    prices = read_prices('Data/prices.csv')
        
    portfolio = []
    #Open the csv file and read the data from it 
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        #Run a loop on each row convert it into the dic and append that into the portfolio list
        for row in rows:
            holding = {'name' : row[0], 'shares' : int(row[1]), 'price'  : float(row[2])}
            portfolio.append(holding)
        #Calculate the total valuation of Portfolio and current_market_value 
        total_valuation = 0.0
        actual_market_value = 0.0

        for s in portfolio:
            total_valuation += s['shares'] * s['price']
            actual_market_value += s['shares'] * float(prices[s['name']])   
        #Check if it's loss or gain    
        if total_valuation > actual_market_value:
            return print("Loss", total_valuation - actual_market_value)
        else:
            return print("Gain", actual_market_value - total_valuation)    
    



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


read_portfolio('Data/portfolio.csv')