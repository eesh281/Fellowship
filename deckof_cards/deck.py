#********************************************************************************************************
#@purpose: implement game of playing cards
#@file:deck.py
#@author:Gursheesh Kour
#*********************************************************************************************************

try:
    #importing required modules
    import random
    from cards import Card

except ImportError:
    
    print("Error while Importing")  


class Deck(object):
   
    def __init__(self):
      
        self.cards = []
        self.build()

    # Display all cards in the deck
    def display(self):
       
        for card in self.cards:
            
            print (card.display())

    # Generate 52 cards
    def build(self):
       
        self.cards = []
        
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
         
            for val in range(1,14):
                self.cards.append(Card(suit, val))

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
       
        for _ in range(num):
       
            for i in range(length-1, 0, -1):
                rand = random.randint(0, i)
               
                if i == rand:
                    continue
                
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
           
    # Return the top card
    def deal(self):
        return self.cards.pop()
