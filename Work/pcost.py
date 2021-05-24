# pcost.py
#
# Exercise 1.30
def portfolio_cost(filename):
    f = open('Data/portfolio.csv', 'rt')
    headers = next(f).split(',')
    total_sum = 0
    for line in f:
        row = line.split(',')
        total_sum = total_sum + float(row[1]) * float(row[2])
    return total_sum

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)