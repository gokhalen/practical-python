# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:43:09 2020

@author: Gokhale
"""


name = 'Dave'

def changename():
    global name
    name = 'Nachiket'
    
changename()
print(f'name={name}')