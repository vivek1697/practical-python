# mortgage.py
#
# Exercise 1.11
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
#Create a new variable which will count the amont of extra payment for given months
new_payment = payment + extra_payment


while principal > 0:
    month += 1
    #Check if cutomer wants to make extra payments for months or not
    #If yes it will take the payment value accoring to that else take the regualr value 
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = new_payment
        
    else:
        payment = 2684.11
        
    #if principal amount is less than customer will pay only the remaining amount instead of full payment
    if principal < payment:
        payment = principal
        principal = 0
    else:    
        principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(month, round(total_paid, 2), round(principal, 2))
    
print("Total paid", round(total_paid, 2)) 
print("Month", month)