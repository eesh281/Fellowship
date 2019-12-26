#*****************************************************************************************************
#@purpose: to create all method necessary for calculating total price
#@file:stock_portfo.py
#@author:Gursheesh Kour
#*****************************************************************************************************

#importing json module 
import json

#creating a class for calculating values
class Cal_Stock:
    
    #method to find value of each stock
    def valueof_each(self, stock_arr):
        each_price = 0

        for key in stock_arr:
            each_price =  key["numof_share"] * key["price"]
            print("price of each stock is respectively is : ", each_price)
        
    #method to find total value of stock
    def total_value(self, stock_arr):
        total_price = 0

        for key in stock_arr:
            total_price = total_price + key["price"]
        print("price of total stock is: ", total_price)

