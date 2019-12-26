#*****************************************************************************************************
#@purpose: to calculate the total stock price
#@file:stock.py
#@author:Gursheesh Kour
#*****************************************************************************************************

#importing json module 
import json 
#importing Cal_Stock class from Stock_portfo
from stock_portfo import Cal_Stock

#class named stock
class Stock:

    #method to open file
    def stock_open(self):
        
        file = open("/home/user/Desktop/newfolder/Fellowship/stock/stock_json.json","r")
        
        stock_dict = json.load(file)
        stock_arr = stock_dict["Stock_name"]
        
        file.close()
        
        return stock_arr

#creating object for the class for calling methods
obj1 = Stock()
a = obj1.stock_open()

obj = Cal_Stock()
obj.valueof_each(a)
obj.total_value(a)