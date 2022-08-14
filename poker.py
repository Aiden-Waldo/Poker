# poker.py

#import cards
from random import randint

def checkHand(hand, river):
    cards = hand+river
    cards.sort(key=lambda x: x[2])
    value = 0
    totalPairs = []
    hearts = []
    spades = []
    clubs = []
    diamonds = []
    for card in cards:
        pairs = [card]
        others = cards.copy()
        others.pop(others.index(card))
        for otherCard in others:
            if otherCard[2] == pairs[0][2]: # pair related
                found = False
                for pairCard in pairs:
                    if otherCard == pairCard:
                        found = True
                if found == False:
                    pairs.append(otherCard)
        # splitting cards to their suits
        if card[1] == "Spades":
            spades.append(card)
        elif card[1] == "Clubs":
            clubs.append(card)
        elif card[1] == "Hearts":
            hearts.append(card)
        else:
            diamonds.append(card)
        
        # pair related
        if len(pairs) > 1:
            if len(totalPairs) > 0:
                found = False
                for pairCard in pairs:
                    for tpCard in totalPairs[0]:
                        if pairCard == tpCard:
                            found = True
                if found == False:
                    totalPairs.append(pairs)
            else:
                totalPairs.append(pairs)
    if len(totalPairs) == 2:
        if len(totalPairs[0]) == 3 or len(totalPairs[1]) == 3: # full house
            if totalPairs[0][0][2] > totalPairs[1][0][2]:
                high = totalPairs[0][0][2]
            else:
                high = totalPairs[1][0][2]
            value = 13*6+high
        else:
            if totalPairs[0][0][2] > totalPairs[1][0][2]: # 2 pair
                high = totalPairs[0][0][2]
            else:
                high = totalPairs[1][0][2]
                value = 13*2+high
    else:
        if len(totalPairs) == 1:
            pairs = totalPairs[0]
            if len(pairs) == 2: # pair
                value = 13*1+pairs[0][2]
            elif len(pairs) == 3: # 3 of a kind
                value = 13*3+pairs[0][2]
            elif len(pairs) == 4: # 4 of a kind
                value = 13*7+pairs[0][2]

    # suit related
    cards = [spades, clubs, hearts, diamonds]
    print(cards)
    return value


for i in range(1):
    import cards
    deck = cards.makeDeck()
    cards.shuffle(deck)
    hand = [cards.draw(deck), cards.draw(deck)]
    river = [cards.draw(deck), cards.draw(deck), cards.draw(deck)]
    value = checkHand(hand, river)
    if value > 13*7 and value < 13*8:
        value = checkHand(hand, river)
        print(f'''
hand: {hand}
river: {river}
value: {value}''')

