# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:06:03 2016

@author: lukaswolff


TASK
Stock returns. Calculate the daily returns for all stocks in the data. Discuss the returns over
the year: what companies experienced the maximum and minimum daily returns - can you
find the reasons for these? Which companies performed overall best and worst over the year?
Which companies exhibited most and least volatility, as measured by the standard deviation
of their returns over the year?
"""

import Stock as st


def getDailyReturnsForAllStocks(stock_list):
    """
    Calculates the daily returns for all stocks 
    Input: List with all stocks 
    Output: List with a list of all daily returns for each stock 
    """

    dailyreturnforall=[]
    for i in range(len(stock_list)):
        dailyreturnforall.append(stock_list[i].getDailyReturnAll())
    return dailyreturnforall
    
    
def getMinimumDailyReturns(stock_list):
    """
    Returns the lowest daily return for the observed period and the company
    associated to it
    """
    dailyreturnforall = getDailyReturnsForAllStocks(stock_list)
    minforeachcompany=[]
    for i in range(len(dailyreturnforall)):
        minforeachcompany.append(min(dailyreturnforall[i]))
    min_dailyreturn = min(minforeachcompany)
    min_dailyreturn_index  = minforeachcompany.index(min_dailyreturn)
    min_dailyreturn_com = stock_list[min_dailyreturn_index]
    return (min_dailyreturn_com, min_dailyreturn )
    
    
def getMaximumDailyReturns(stock_list):
    """
    Returns the highest daily return for the observed period and the company
    associated to it
    """
    maxforeachcompany=[]
    dailyreturnforall = getDailyReturnsForAllStocks(stock_list)
    for i in range(len(dailyreturnforall)):
        maxforeachcompany.append(max(dailyreturnforall[i]))
    max_dailyreturn = max(maxforeachcompany)
    max_dailyreturn_index  = maxforeachcompany.index(max_dailyreturn)
    max_dailyreturn_com = stock_list[max_dailyreturn_index]
    return (max_dailyreturn_com, max_dailyreturn )
    
    
def getBestPerformingCompany(stock_list):
    """
    WHAT COULD BE A MEASURE OF GOOD PERFORMANCE? (maybe geometric mean?)
    """
    return None
    
    
def getWorstPerformingCompany(stock_list):
    """
    same question as above
    """
    return None        
    
    
def getCompanyWithLeastVolatility(stock_list):
    """
    Returns the lowest standard deviation of returns
    for all observed companies and the company associated to it
    """
    allsd=[]
    for i in range(len(stock_list)):
        allsd.append(stock_list[i].getStandardDeviation())
    minsd=min(allsd)
    minsd_index = allsd.index(minsd)
    minsd_name = stock_list[minsd_index]
    return (minsd_name, minsd)
    
    
def getCompanyWithHighestVolatility(stock_list):
    """
    Returns the highest standard deviation of returns
    for all observed companies and the company associated to it
    """
    allsd=[]
    for i in range(len(stock_list)):
        allsd.append(stock_list[i].getStandardDeviation())    
    maxsd = max(allsd)
    maxsd_index = allsd.index(maxsd)
    maxsd_name = stock_list[maxsd_index]
    return (maxsd_name, maxsd)    
    return None
    
    
def printSummary(stock_list):
    """
    This function wraps up all functions in this module and creates a summary
    of the dataset. 
    """
    #Maybe also include graphics?
    Min_daily_return = getMinimumDailyReturns(stock_list)[1]
    Max_daily_return = getMaximumDailyReturns(stock_list)[1]
    Min_return_coname = getMinimumDailyReturns(stock_list)[0].getName()
    Max_return_coname = getMaximumDailyReturns(stock_list)[0].getName()
    Low_v = getCompanyWithLeastVolatility(stock_list)[1]
    High_v = getCompanyWithHighestVolatility(stock_list)[1]
    Low_v_coname = getCompanyWithLeastVolatility(stock_list)[0].getName()
    High_v_coname = getCompanyWithHighestVolatility(stock_list)[0].getName()
    print('The lowest daily return for the observed period is', Min_daily_return ,' and the company associated to it is', Min_return_coname)
    print('The highest daily return for the observed period is', Max_daily_return ,' and the company associated to it is', Max_return_coname)    
    print('The company with least volatility is', Low_v_coname ,' and its standard deviation in price is', Low_v)
    print('The company with highest volatility is', High_v_coname ,'and its standard deviation in price is', High_v)
    
