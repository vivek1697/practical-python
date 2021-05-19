# mortgage.py
#
# Exercise 1.8
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    month += 1
    if month <= 12:
        payment = 3684.11
    else:
        payment = 2684.11    
 
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    
    

print('Total paid', total_paid, 'for', month)