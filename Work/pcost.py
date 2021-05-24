# pcost.py
#
# Exercise 1.32
import csv
f = open('Data/portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
total_sum = 0
for row in rows:
    total_sum = total_sum + float(row[1]) * float(row[2])
print(f'Total cost {total_sum}')     


