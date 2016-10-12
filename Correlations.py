# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:45:12 2016

@author: lukaswolff


"""

import Stock as st
import numpy as np


    
    
def getCorrelation(stock1, stock2):
    """
    Returns the correlation for two given stocks using the formula
    given in the homework assignment
    Output: 
    """

    
    x = stock1.getDailyReturnAll()
    y = stock2.getDailyReturnAll()
    
    #s1 = stockFirst.getYearlyReturn()
    #s2 = stockSecond.getYearlyReturn()
    
    n = len(x)
    
    xy = 0
    for i in range(0,len(x)):
        xy = xy + (x[i]*y[i])
    
    cor = (xy - (n*stock1.getMean()*stock2.getMean())) / (n*stock1.getStandardDeviation()*stock2.getStandardDeviation())
    return cor

def printCorrelation(stock1, stock2):
    """
    Prints out the companies full names of the two given stocks and
    the correlation between those two
    """
    print('')


def getCorrelationList(stock, stock_list):
    """
    Returns for a given stock a list with the correlation to all other 
    stocks inside a list of tuples (stock name, correlation) and sorts the
    list according to the correlation (descending)
    """
    return None #correlation_list

def getLeastCorrelatedCompany(stock, stock_list):
    """
    Returns for a given stock the company with the least correlation and the
    correlation to this company
    """
    return None

def printLeastCorrelatedCompany(stock, stock_list):
    """
    Prints out for a given stock the name of the company, the company it has
    the least correlation to and the name of the related company
    """
    print('')


def getHighestCorrelatedCompany(stock, stock_list):
    """
    Similar to LeastCorrelatedCompany
    """
    return None

def printHighestCorrelatedCompany(stock, stock_list):
    """
    Similar to LeastCorrelatedCompany
    """
    print('')





 



