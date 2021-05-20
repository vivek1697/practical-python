# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
total_sum = 0
for line in f:
    row = line.split(',')
    total_sum = total_sum + float(row[1]) * float(row[2])
print(f'Total cost {total_sum}')    