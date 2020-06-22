# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:40:37 2020

@author: Gokhale
"""


def typedproperty(name,expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self,private_name)
    
    
    @prop.setter
    def prop(self,value):
        if not isinstance(value,expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self,private_name,value)
        
    return prop