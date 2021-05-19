# mortgage.py
#
# Exercise 1.10
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
new_payment = payment + extra_payment


while principal > 0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = new_payment
        
    else:
        payment = 2684.11
       
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month, round(total_paid, 2), round(principal, 2))
    
print("Total paid", round(total_paid, 2)) 
print("Month", month)