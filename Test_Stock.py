# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:03:35 2016

@author: lukaswolff
"""

import unittest
import Stock as st




class TestStockMethods(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.stock1 = st.Stock('Pear', [2,2,5,3,3,3], 'Technology', 'PPAR')
        cls.stock2 = st.Stock('Banana', [4,7,1,9,3,4], 'Energy', 'BANA')
    
    
    def test_getDailyReturn1(self):
        self.assertEqual(self.stock1.getDailyReturn(1), 0)
        
    def test_getDailyReturn2(self):
        self.assertEqual(self.stock1.getDailyReturn(0), None)
        
    """
    def test_getMeanReturn(self):
        self.assertEqual(self.stock1.getMeanReturn(), 0.22)
    
    
    

        
    def test_getYearlyReturn(self):
        self.assertEqual(self.stock1.getYearlyReturn(), 0.5)
        
        
    def test_getStandardDeviation(self):
        self.assertEqual(self.stock1.getStandardDeviation(), 1)
    
    def test_getGeometricMean(self):
        self.assertEqual(self.stock1.getGeometricMean(), 1.069913194)
     
     """
    
if __name__ == '__main__':
    unittest.main()
    

#3
