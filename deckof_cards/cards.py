#********************************************************************************************************
#@purpose
#@file
#@author
#*********************************************************************************************************


class Card(object):
    
    def __init__(self, suit, val):
        
        self.suit = suit
        self.value = val

    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.display()
    
    def __str__(self):
        return self.display()
    
    def __repr__(self):
        return self.display()
        
    def display(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value
        
        format1 = "{} of {}".format(val, self.suit)

        return format1




