# mortgage.py
#
# Exercise 1.7
# 
# Dave makes an extra payment of $1000/month between month
# This logic makes Dave overshoot the principal (i.e. makes the principal neg)
# Fixed in this file
# This also pretty prints the table using f-strings

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month=60
extra_payment_end_month=108
extra_payment=1000

while principal > 0:
    
    total_payment = payment
    if ( extra_payment_start_month <= month <= extra_payment_end_month):
        total_payment += extra_payment 
    
    if (principal * (1+rate/12) - total_payment) < 0 :
        total_payment = principal*(1+rate/12)
        
    principal  = principal * (1+rate/12) - total_payment
    total_paid = total_paid + total_payment
    
    outstring=f'Month={month:3}, Total paid={total_paid:10.2f}, Principal={principal:10.2f}'
    print(outstring)
    
    month += 1

print('Total paid', round(total_paid,2))