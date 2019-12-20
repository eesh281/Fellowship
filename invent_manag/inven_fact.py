from __future__ import generators
import random
from enum import Enum, auto

class ItemType(Enum):
    rice  = auto() 
    pulse  = auto()
    wheat = auto()


class Type(object):
    pass

class Rice(Type):
    def name(self):
        print("Rice.name")
    def price(self): 
        print("Rice.price")

class Pulse(Type):
    def name(self): 
        print("Pulse.name")
    def price(self): 
        print("Pulse.price")

class Wheat(Type):
    def name(self): 
        print("Pulse.name")
    def price(self): 
        print("Pulse.price")
    

class InventoryFact(object):

    @staticmethod
    def item(type):
        #return eval(type + "()") # simple alternative
        if type in InventoryFact.choice:
            return InventoryFact.choice[type]()

        assert 0, "not an available item: " + type    

    choice = { ItemType.rice:  Rice,
               ItemType.pulse:  Pulse 

             }

# Test factory
# Generate item_type name strings:
def name_ofitem(n):

    types = list(ItemType)

    for i in range(n):
        yield random.choice(types)

data = \
  [ InventoryFact.item(i) for i in name_ofitem(7)]

for item_type in data:
    item_type.name()
    item_type.price()