# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    with open(filename,'rt') as f:
        header = next(f)
        total_cost = 0.0
        for line in f:
            line=line.strip('\n')
            listline = line.split(',')
            try:
                if (listline[0]==""):
                    raise RuntimeError("Blank stock name")
            except RuntimeError as inst:
                print(inst.args)
            
            try:
                nn = int(listline[1])
            except ValueError as inst:
                nn = 0
                print("ValueError in number of shares, args=", inst.args)
                
            try:
                cost = float(listline[2])
            except ValueError as inst:
                cost = 0
                print("ValueError in cost args, args=",inst.args)
            
            total_cost += nn*cost 
            
    return total_cost


total_cost=portfolio_cost('Data/missing.csv')

print("total_cost=",total_cost)
