import cards  #, displayGame

# show off the constructor. Fairly safe from bad input. Bad input returns a "blank"
# card (rank of 0, suit of '')
TenHearts = cards.Card(10,'H')
AceSpades = cards.Card('a','s')
JackClubs = cards.Card('J','c')
badCard1 = cards.Card(25,'q')
badCard2 = cards.Card(1.0,1.0)
blankCard = cards.Card()
print(TenHearts,AceSpades,JackClubs,blankCard,badCard1,badCard2)

print(TenHearts.get_rank())
print(JackClubs.get_rank())
print(AceSpades.get_rank())
print(TenHearts.get_suit())
print(TenHearts.get_value())
print(JackClubs.get_value())
print(AceSpades.get_value())

if JackClubs.has_same_color(AceSpades):
    print(JackClubs, "and",AceSpades,"have same color")
else:
    print(JackClubs, "and",AceSpades,"have different color")
    
print("try to hide a card")
print("before hiding:",JackClubs)
JackClubs.set_hidden()
print("after hiding:",JackClubs)
JackClubs.set_hidden(val=False)
print("after unhiding:", JackClubs)




aDeck = cards.Deck()
aDeck.shuffle()
print(aDeck)
c = aDeck.deal()
print(c, aDeck)
print('How many cards left:',aDeck.cards_left())
print('Top Card is:',aDeck.top())
print('Bottom Card is:',aDeck.bottom())
print("Is the deck empty?",aDeck.empty())
aDeck.add_card_top(c)
print('adding',c,'to the top of the deck yields',aDeck)
aDeck.add_card_bottom(c)
print('adding',c,'to the bottom of the deck yields',aDeck)

hand = [aDeck.deal() for i in range(5)]
print("5-card hand dealt is:", hand)
print('remaining in the deck:', aDeck)



