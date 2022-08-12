# poker.py

#import cards
from random import randint

def checkHand(hand, river):
    cards = hand+river
    value = 0
    return value


for i in range(500):
    import cards
    deck = cards.makeDeck()
    cards.shuffle(deck)
    hand = [cards.draw(deck), cards.draw(deck)]
    river = [cards.draw(deck), cards.draw(deck), cards.draw(deck)]
    value = checkHand(hand, river)
    if value > 104:
        value = checkHand(hand, river)
        print(f'''
hand: {hand}
river: {river}
value: {value}''')

