# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:51:28 2020
@author: Gokhale

Takes a list of dicts and pretty prints it as per the format 
specified in formatting dabaez-course. 
Related files: report.py,readprices.py,retire.py
"""

def pretty_print_prices(ll):
# first check if list has dictionaries
    if len(ll) >= 1 :
# print the keys of the first dictionary
# assuming all dictionaries have the same
        ss = "" 
        for key in ll[0].keys():
            ss=ss + f'{key.title():>10s}' + " "
        print(ss)
# Makes underscores below the header fields
# Can also use a straight, simple f-string f'{"":_>40}'
# How ever the code is a bit more general, it makes the 
# number of underscores dependent on n 
        ss  = ""
        ss2 = ""
        nn  = 10
        for key in ll[0].keys():
            ss=ss+f'{ss2:_>{nn}}' + " "
        print(ss)
       
# Now print the fields
# this is brute force, you can also iterate over keys
# remember, if you use single-quotes for the outermost quotes of the f-string
# you must use double-quotes to refer to dd["name"]
        for dd in ll:
            ss=(f'{dd["name"]:>10}'
                f' {dd["shares"]:>10d}'
                f' {dd["price"]:>10.2f}'
                f' {dd["change"]:>10.2f}'
                )
            print(ss)
        
def pretty_print_prices_tuple(ll):
# in this case tuples don't have header information in them
# first check if list has tuples
    if len(ll) >= 1 :
        ss=(f'{"Name":>10}'
            f' {"Shares":>10}'
            f' {"Price":>10}'
            f' {"Change":>10}'
            )
        print(ss)
        ss = f'{"":_>43}'
        print(ss)          
        
        for tt in ll:
            name   = tt[0]
            shares = tt[1]
            price  = tt[2]
            change = tt[3]
            
            ss=(f'{name:>10}'
                f' {shares:>10d}'
                f' {price:>10.2f}'
                f' {change:>10.2f}'
                )
            print(ss)
            