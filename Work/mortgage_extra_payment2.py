# mortgage.py
#
# Exercise 1.7
# 
# Dave makes an extra payment of $1000/month between month
# This logic makes Dave overshoot the principal (i.e. makes the principal neg)
# Fixed in mortgage extra_payment3.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month=60
extra_payment_end_month=108
extra_payment=1000

while principal > 0:
    
    principal  = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    
    if ( extra_payment_start_month <= month <= extra_payment_end_month):
        principal  = principal  - extra_payment
        total_paid = total_paid + extra_payment
    
    print(month,round(total_paid,2),round(principal,2))
    
    month += 1

print('Total paid', round(total_paid,2))