# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:57:28 2020

@author: Gokhale
"""

initial_height = 100
height = initial_height

for ii in range(10):
    bounce = height * (3/5)
    print("bounce = ", round(bounce,4))
    height = bounce
    