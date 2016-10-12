# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:28:02 2016

@author: lukaswolff
"""
import csv
import numpy as np
import Stock as st
import Correlations as c




Stock_List = []
Trade_Dates = []

def readCSVIntoList(name):
    """
    Reads in a csv file and returns the rows as a list. This method is used
    for the function PriceListToMatrix and in dataPrep for the csv file with 
    the sectors and names
    Input: name of the csv file
    Output: List where every line of the csv file is stored in an element
    of the list returned
    
    """
    L = []
    with open(name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            L.append(row)
    return L

    
def priceListToMatrix(L):
    """
    Transforms a list of rows into a matrix to simplify operations on columns
    Input: List with all rows of the csv file
    Output: numpy matrix with all price entries of the csv file, 
    header containing the symbols of the companies and list with all dates
    """ 
    first_row = L[0]
    header = first_row[1:]
    
    
    #Creates a matrix of the size of the csv file with 0s in each cell
    num_col = len(header)
    num_row = len(L)-1
    price_matrix = np.zeros((num_row, num_col))
    
    #Fills the matrix with the stock price movements
    for i in range (len(L)-1):
        row = L[i+1]
        #Strips off the dates row and stores it in a separate list
        price_matrix[i,] = row[1:]
        Trade_Dates.append(row[0])
    
    return price_matrix, header 


def priceMatrixToStockClasses(pm, header, sectors, names):
    """
    Transforms our price matrix into a list of stocks
    Input: Price matrix, header with the symbols of the companies, a list with
    all the names of the companies and the sectors of each company
    Output: List of stocks (stock class) 
    """
    for i in range(len(header)):
        name = names[i]
        price_movement = pm[:,i]
        sector = sectors[i]
        symbol = header[i]
        newStock = st.Stock(name, price_movement, sector, symbol)
        Stock_List.append(newStock)
   
    

def dataPrep():
    """
    Wrap up function calling all the functions defined in this file
    """
    price_sheet = readCSVIntoList('SP_500_close_2015.csv')
    price_matrix, header = priceListToMatrix(price_sheet)
    
    name_sheet = readCSVIntoList('SP_500_firms.csv') 
    names = []
    sectors = []
    
    for i in range(1, len(name_sheet)):
        row = name_sheet[i]
        names.append(row[1])
        sectors.append(row[2])
           
    priceMatrixToStockClasses(price_matrix, header, sectors, names)
    


def findStock(symbol):
    for i in range(len(Stock_List)):
        if Stock_List[i].getSymbol()==symbol:
            return Stock_List[i]
        
    #if stock is not in Stock_List (probably wrong spelled?)
    return None
    
dataPrep()
#print(len(Stock_List))
#for i in range (len(Stock_List)):
   # print(Stock_List[i].get())
#print(Stock_List[3].getPrice_List())
#print(findStock('YHOO').getName())
#print(Stock_List[0].getSymbol())
#print(c.getCorrelation(findStock('AAPL'), findStock('MMM')))
print(c.getCorrelation(Stock_List[5], Stock_List[80]))



