#********************************************************************************************************
#@purpose: implement game of playing cards
#@file:player_card.py
#@author:Gursheesh Kour
#*********************************************************************************************************

try:
    #importing required classes
    from cards import Card
    from deck import Deck

except ImportError:
    print("Error while Importing")  


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def say_hello(self):
        print ("I am {}".format(self.name))
        return self

   
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else: 
                return False
        return True

    # Display all the cards in the players hand
    def display_hand(self):
        print ("{}'s hand: {}".format(self.name, self.hand))
        return self

    def discard(self):
        return self.hand.pop()


my_deck = Deck()
my_deck.shuffle()

obj = Player("Gursheesh")
obj.sayHello()
obj.draw(myDeck, 5)
obj.displayHand()