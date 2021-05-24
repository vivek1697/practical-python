# pcost.py
#
# Exercise 1.31
def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f).split(',')
    total_sum = 0
    for line in f:
        row = line.split(',')
        try:
            total_sum = total_sum + float(row[1]) * float(row[2])
        except ValueError:
            print("Couldn't process the balnk string data")
    return total_sum

cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)