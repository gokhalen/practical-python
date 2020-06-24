# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:52:37 2020

@author: Gokhale
"""
import time

def timethis(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end   = time.time()
        print(f'function {func.__name__} took {end - start} seconds to execute')
    return wrapper

@timethis
def looper(end=1000000):
    for ii in range(end):
        pass
    return 

looper(100000000)
