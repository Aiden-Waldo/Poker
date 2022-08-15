# poker.py

#import cards
from random import randint

def checkHand(hand, river):
    cards = hand+river
    cards.sort(key=lambda x: x[2])
    value = cards[-1][2]
    totalPairs = []
    hearts = []
    spades = []
    clubs = []
    diamonds = []
    straight = 0
    mult = 0
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
                    for i in range(len(totalPairs)):
                        for tpCard in totalPairs[i]:
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
                value = 13*6+high
            else:
                high = totalPairs[1][0][2]
            value = 13*6+high
        else:
            if totalPairs[0][0][2] > totalPairs[1][0][2]: # 2 pair
                high = totalPairs[0][0][2]
                value = 13*2+high
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
    # straight check 
    for i in range(len(cards)):
        if i+cards[0][2] == cards[i][2]:
            straight += 1
    if straight == 5:
        value = 13*4+cards[-1][2]
    # suit related
    cards = [spades, clubs, hearts, diamonds]
    for ele in cards:
        ele.sort(key=lambda x: x[2])
        if len(ele) == 5:
            straight = 0
            for i in range(len(ele)):
                if i+ele[0][2] == ele[i][2]:
                    straight += 1
            if straight == 5 and ele[-1][2] == 13:
                value = 13*9+13
            elif straight == 5:
                value = 13*8+ele[-1][2]
            elif value < 13*6:
                value = 13*5+ele[-1][2]
    return value
def printValue(hand, river, value):
    print(f'''
hand: {hand}
river: {river}
value: {value}''')

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
ii = 0
j = 0
k = []
for i in range(50000000):
    import cards
    deck = cards.makeDeck()
    cards.shuffle(deck)
    hand = [cards.draw(deck), cards.draw(deck)]
    river = [cards.draw(deck), cards.draw(deck), cards.draw(deck)]
    value = checkHand(hand, river)
    
    if value > 13*0 and value <= 13*1 and a == 0:
        value = checkHand(hand, river)
        printValue(hand, river, value)
        a = 1
        k.append(a)
    if value > 13*1 and value <= 13*2 and b == 0:
        value = checkHand(hand, river)
        printValue(hand, river, value)
        b = 1
        k.append(b)
    if value > 13*2 and value <= 13*3 and c == 0:
        value = checkHand(hand, river)
        printValue(hand, river, value)
        c = 1
        k.append(c)
    if value > 13*3 and value <= 13*4 and d == 0:
        value = checkHand(hand, river)
        printValue(hand, river, value)
        d = 1
        k.append(d)
    if value > 13*4 and value <= 13*5 and e == 0:
        value = checkHand(hand, river)
        printValue(hand, river, value)
        e = 1
        k.append(e)
    if value > 13*5 and value <= 13*6 and f == 0:
        value = checkHand(hand, river)
        printValue(hand, river, value)
        f = 1
        k.append(f)
    if value > 13*6 and value <= 13*7 and g == 0:
        value = checkHand(hand, river)
        printValue(hand, river, value)
        g = 1
        k.append(g)
    if value > 13*7 and value <= 13*8 and h == 0:
        value = checkHand(hand, river)
        printValue(hand, river, value)
        h = 1
        k.append(h)
    if value > 13*8 and value <= 13*9 and ii == 0:
        value = checkHand(hand, river)
        printValue(hand, river, value)
        ii = 1
        k.append(ii)
    if value > 13*9 and value <= 13*10 and j == 0:
        value = checkHand(hand, river)
        printValue(hand, river, value)
        j = 1
        k.append(j)
    if len(k) == 10:
        quit()


