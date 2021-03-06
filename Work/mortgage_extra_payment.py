# mortgage.py
#
# Exercise 1.7
# 
# Dave makes an extra payment of $1000/month for the first 12 months

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

while principal > 0:
    extra_payment = 0
    if month <= 12:
       extra_payment = 1000
    principal = principal * (1+rate/12) - payment -extra_payment
    total_paid = total_paid + payment + extra_payment
    month += 1

print('Total paid', total_paid)