#*****************************************************************************************************
#@purpose: to calculate the total stock price
#@file:stock.py
#@author:Gursheesh Kour
#*****************************************************************************************************

import json 
from stock_portfo import Cal_Stock

class Stock:

    def stock_open(self):
        file = open("/home/user/Desktop/newfolder/Fellowship/stock/stock_json.json","r")
        stock_dict = json.load(file)
        stock_arr = stock_dict["Stock_name"]
        return stock_arr

  
obj1 = Stock()
a = obj1.stock_open()
print(a)
obj = Cal_Stock()
obj.valueof_each(a)
obj.total_value(a)
            