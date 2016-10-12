# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:05:13 2016

@author: lukaswolff
"""

import unittest
import Stock as st



class TestStock_ReturnsMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stock1 = st.Stock('Pear', [2,2,5,3,3,3], 'Technology', 'PPAR')
        cls.stock2 = st.Stock('Banana', [4,7,1,9,3,4], 'Energy', 'BANA')
        cls.stock_list = [cls.stock1, cls.stock2]
    
    def getMinimumDailyReturns(self):
        self.assertEqual(self.getMinimumDailyReturns(self.stock_list), -X)
    
    def getMaximumDailyReturns(self):
        self.assertEqual(self.getMinimumDailyReturns(self.stock_list), -X)