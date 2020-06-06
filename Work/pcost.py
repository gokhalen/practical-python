# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv','rt') as f:
    header = next(f)
    total_cost = 0.0
    for line in f:
        line=line.strip('\n')
        listline = line.split(',')
        nn   = int(listline[1])
        cost = float(listline[2])
        total_cost += nn*cost 

print(total_cost)
print(cost)
print(nn)