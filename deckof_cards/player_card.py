from cards import Card
from deck import Deck

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

    # Display all the cards in the players hand
    def displayHand(self):
        print ("{}'s hand: {}".format(self.name, self.hand))
        return self

    def discard(self):
        return self.hand.pop()

# Test making a Card
# card = Card('Spades', 6)
# print card

# Test making a Deck
myDeck = Deck()
myDeck.shuffle()
# deck.display()

obj = Player("Gursheesh")
obj.sayHello()
obj.draw(myDeck, 5)
obj.displayHand()