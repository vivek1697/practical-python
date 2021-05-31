# report.py
#
# Exercise 3.12
import csv
import fileparse
#Function create a portfolio dic from the file   
def read_portfolio(filename):
    portfolio = fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float], has_headers=True)
    return portfolio

#Function create a prices dic from the file       
def read_prices(filename):
    prices = dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))
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


def main(argv):
    if len(sys.argv) != 3:
        raise SystemExit(f'missing arguments for {sys.argv[0]} ')
    portfoliofile = argv[1]
    pricefile = argv[2]
        
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    report = make_report(portfolio, prices)
    print_report(report)
    
if __name__ == '__main__':
    import sys
    main(sys.argv)