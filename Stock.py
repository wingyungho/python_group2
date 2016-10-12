# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:29:45 2016

@author: lukaswolff
Stock returns. Calculate the daily returns for all stocks in the data. Discuss the returns over
the year: what companies experienced the maximum and minimum daily returns - can you
find the reasons for these? Which companies performed overall best and worst over the year?
Which companies exhibited most and least volatility, as measured by the standard deviation
of their returns over the year?
"""

import numpy as np
import math



class Stock():
    
    def __init__(self, name, price_list, sector, symbol):
        """
        Constructor function for our stock class to initialize name, list with 
        the price changes, sector and the stock symbol (e.g. AAPL for Apple)
        
        """
        self.name = name
        self.price_list = price_list
        self.sector = sector
        self.symbol = symbol
        
    
    def getName(self):
        return self.name
        
    def getSector(self):
        return self.sector
    
    def getSymbol(self):
        return self.symbol
    
    def getPrice_List(self):
        return self.price_list

    def getDailyReturnAll(self):
        """
        Input: No input
        Output: Movement of the stock price compared to the price the day before for the whole period
        """
        dailyReturn = []
        for items in range(0, len(self.price_list)-1):
            dailyReturn.append(((self.price_list[items + 1] - self.price_list[items]) / self.price_list[items])*100)
        return dailyReturn
    
    def getDailyReturn(self, date):
        """
        Input: Date as a index of our price list (e.g. 1 for price at 
        the second day)
        Output: Movement of the stock price compared to the price the day 
        before or None if it is the first observation
        """

        return (self.price_list[date]-self.price_list[date-1])/self.price_list[date-1]

    def getYearlyReturn(self):
        """
        Returns the return of the stock for the whole year
        """
        yearlyReturn = (self.price_list[-1]-self.price_list[0]) / self.price_list[0]

        return yearlyReturn

    def getMean(self):
        """
        Returns the mean Stock Price Movement of the stock for the whole period
        of time
        """
        mean = sum(self.getDailyReturnAll()) / len(self.price_list)
        return mean
        
        
    def getVariance(self):
        """
        Returns the variance of the Stock Price Movement for the 
        whole period
        """

        average = self.getMean() ### This gives you the mean the Stock
        all_returns = self.getDailyReturnAll()

        variancelist = [] #Subtract the Mean and square the result
        for items in range(0, len(all_returns)):
            variancelist.append((all_returns[items]-average)**2)
        
        variance = sum(variancelist)/len(variancelist) #The mean of those squared differences divided by the length is the variance.
        return variance
        
    def getStandardDeviation(self):
        """
        Returns the Standard Deviation of the Stock Price Movement for the 
        whole period
        """
        variance = self.getVariance()
        return math.sqrt(variance)

    def getGeometricMean(self):
        """
        Returns the geometric mean of the Stock Price Movement for the whole
        period
        """
        dailyReturnPercentage =self.getDailyReturnAll()

        dailyReturn = []
        for number in dailyReturnPercentage:
            if number < 0:
                turnPositive = 1-((-1*(number) )/100)
                dailyReturn.append(turnPositive)
            elif number >= 0:
                positive = 1 + ((number)/100)
                dailyReturn.append(positive)

        sumOfDailyReturn = sum(dailyReturn)
        lengthOfReturn = len(dailyReturn)

        geometricMean = sumOfDailyReturn**(1/lengthOfReturn)

        return geometricMean
        
        
    def getOverallPerformance(self):
        """
        ??? 
        """
        return None



