# cards.py

from random import randint
suits = {
        0: "Spades",
        1: "Clubs",
        2: "Hearts",
        3: "Diamonds"
        }
names = {
        1: "Ace",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "Jack",
        12: "Queen",
        13: "King"
        }

def makeDeck():
    deck = []
    for i in range(4):
        for j in range(1, 14):
            if j == 1:
                k = 13
            else:
                k = j-1
            deck.append([names[j], suits[i], k])
    return deck
deck = makeDeck()
def shuffle(deck):
    for i in range(len(deck)):
        card = deck.pop(randint(0, (len(deck)-1)))
        deck.insert(randint(0, len(deck)), card)
shuffle(deck)
def draw(deck):
    return deck.pop()

if __name__ == "__main__":
    x = list(suits.values())
    print(x)
