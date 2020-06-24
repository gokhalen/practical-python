# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:01:26 2020
@author: Gokhale
"""

import stock
import unittest

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG',100,490.1)
        self.assertEqual(s.name,'GOOG')
        self.assertEqual(s.shares,100)
        self.assertEqual(s.price,490.1)
        
    def test_cannot_set_shares_to_non_integer_value_1(self):
#        with self.assertRaises(TypeError):
#           # cannot set number of shares to a floating point value
#           s = stock.Stock('GOOG',1.2,490.1)
        self.assertRaises(TypeError,stock.Stock,'GOOG',1.2,490.1)
    
    def test_cannot_set_shares_to_non_integer_value_2(self):
        self.assertRaises(TypeError,stock.Stock,'GOOG','G',490.1)

        
    def test_cost(self):
        s = stock.Stock('GOOG',100,490.1)
        self.assertEqual(s.cost,49010)
        
    def test_sell(self):
        s = stock.Stock('GOOG',100,490.1)
        s.sell(25)
        self.assertEqual(s.shares,75)
    
if __name__ == '__main__':
    unittest.main()


