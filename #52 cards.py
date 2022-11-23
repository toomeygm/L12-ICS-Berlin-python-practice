#52 cards
# 2 players
# 4 card families
#card values - Ace, 2, 3, 4, 5, 6 ,7, 8, 9, 10

#dealer
#player (name of the player)

#rules of the game
#deal cards- 2 cards initially
#take dealt cards out of deck
# check value of player's cards, sum up the cards

from random import shuffle #Imported from "random" library

def create_deck():
    card_families = ['Hearts', 'Spades', 
    'Diamonds', 'Clubs']
    card_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []
    for family in card_families:
        for value in card_values:
            deck.append(f'{value} of {family}')
    shuffle(deck)
    return deck

def deal_card(deck):
    card = deck.pop()
    return card

def value_of_card(card):
    firstAlphabet = card[0]
    if firstAlphabet in ['J', 'Q', 'K']:
        return int(10) # or just return 10
    elif firstAlphabet == 'A':
        #ask use if ACE is 1 or 11
        pass
    else:
        return int(firstAlphabet)


