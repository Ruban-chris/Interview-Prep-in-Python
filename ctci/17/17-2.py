# shuffle a deck of cards
import random

def randomCardIndex():
    random.randrange(0, 51, 1)
    
def shuffle(deck):
    for i, card in enumerate(deck):
        swapIndex = randomCardIndex()
        temp = deck[swapIndex]
        deck[swapIndex] = deck[i]
        deck[i] = temp
    return deck

