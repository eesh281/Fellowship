

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