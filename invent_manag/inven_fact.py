#*******************************************************************************************************
#@purpose:to create a factory inventory
#@file   :invent_fact.py
#@author :Gursheesh Kour
#*******************************************************************************************************
from __future__ import generators
try:
    #importing required modules
    from __future__ import generators
    import random
    from enum import Enum, auto
except ImportError:
    print("Error while Importing")  

#creating a enum class to define all attributes
class ItemType(Enum):
    
    rice  = auto() 
    pulse  = auto()
    wheat = auto()


#interface
class Type(object):
    pass

#creating a class for rice
class Rice(Type):
    
    def name(self):
       
        print("Brown rice")
        print("White rice") 
        print("jasmine rice")
   
    
    def price(self): 
        
        price = 1200
        print("price of brown rice is: ", price)
        price1 = 1400
        print("price of white rice is: ", price1)
        price2 = 1000
        print("price of jasmine rice is: ", price2)
       
        total_price = 0
        total_price = price + price1 + price2
        print("total price of rice is : ", total_price)

#creating a class for pulse
class Pulse(Type):
    
    def name(self): 
        
        print("green lentils")
        print("chickpeas")
        print("kidney beans")
    
    
    def price(self): 
       
        price = 200
        print("price of green lentils is: ", price)
        price1 = 400
        print("price of chickpeas is: ", price1)
        price2 = 100
        print("price of kidney beans is: ", price2)
        
        total_price = 0
        total_price = price + price1 + price2
        print("total price of beans is : ", total_price)

#creating a class for wheat
class Wheat(Type):
   
    def name(self): 
        print("beige wheat")
        print("golden wheat")
        print("silver wheat")
    
   
    def price(self): 
        
        price = 300
        print("price of beige wheat is: ", price)
        price1 = 100
        print("price of golden wheat is: ", price1)
        price2 = 400
        print("price of silver wheat is: ", price2)
        
        total_price = 0
        total_price = price + price1 + price2
        print("total price of beans is : ", total_price)

    
#inentory factory class
class InventoryFact(object):

    @staticmethod
    def item(type):
        
        #return eval(type) 
        if type in InventoryFact.choice:
            return InventoryFact.choice[type]()

        assert 0, "not an available item: " + type    

    #giving choice for various functions to run
    choice = { ItemType.rice:  Rice,
               ItemType.pulse:  Pulse,
               ItemType.wheat:  Wheat 
 

             }

# Test factory
def name_ofitem(n):

    types = list(ItemType)

    #traversing for random values
    for i in range(n):
        yield random.choice(types)

#running loop given number of times
data = [ InventoryFact.item(i) for i in name_ofitem(2)]

for item_type in data:
    item_type.name()
    item_type.price()