#********************************************************************************************************
#@purpose
#@file
#@author
#*********************************************************************************************************
import random

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



    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
            # You can also use the build in shuffle method
            # random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()


