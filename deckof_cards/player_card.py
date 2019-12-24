from deck_of_cards import Card
from deck_of_cards import Deck

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        print ("I am {}".format(self.name))
        return self

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else: 
                return False
        return True

