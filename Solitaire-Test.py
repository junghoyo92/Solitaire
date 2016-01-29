class Card():
    def __init__(self, faceNum, suitNum):
        self.faceNum = faceNum
        self.suitNum = suitNum
 
    def getCardName(self):
        nameSuit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        nameFace = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        return "%s of %s" % (nameFace[self.faceNum], nameSuit[self.suitNum])
def Make_Deck():
    deck = []
    for i in range(4):
        for suitNum in range(4):
            for faceNum in range(13):
                deck.append(Card(faceNum, suitNum))
    return deck
         
deck = Make_Deck()
for card in deck:
    print (card.getCardName())

