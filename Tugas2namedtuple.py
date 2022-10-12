
from random import shuffle
from collections import namedtuple

Card = namedtuple('Card',['value', 'balak'])

test = Card(3,'spades')
print('look how namedtuples make things easier: {}'.format(test))
print('now that test is a card we can access its attributes cleanly: {} of {}'.
    format(test.value, test.balak))

# create a deck of 28 cards 
deck = [Card(i,c)
    for c in ['six devil', 'balak', 'murni kecil', 'murni besar', 'qiuqiu']
    for i in range(2, 15)]
 
shuffle(deck)
 
# deal 3 cards for each player
# slicing the list can be a bit cleaner than looping over it
player1 = deck[:3]
deck = deck[3:]

player2 = deck[:3]
deck = deck[3:]

print('player1: ', player1)
print('player2: ', player2)

# use the key parameter to sort by card value
player1 = sorted(player1, key = lambda x: x.value)
print('sorted player1: {}'.format(player1))
# that key parameter works for max and min too:
player2_best = max(player2, key = lambda x: x.value)
print('player2 highest is: {}'.format(player2_best))

def compare(hand_a, hand_b):
    '''
    compare a couple hands of cards, return better hand, or None if tied

    works by sorting the hands from high to low, then cross checking each card
    '''
    hand_a = sorted(hand_a, key = lambda x: -x.value)
    hand_b = sorted(hand_b, key = lambda x: -x.value)
    for card_a, card_b in zip(hand_a,hand_b):
        if card_a>card_b:
            return hand_a
        elif card_b>card_a:
            return hand_b

print(compare(player1, player2))

# now some static hands so you can muck around to make sure this actually works
hand_a = [
        Card(1,'clubs'),
        Card(3,'clubs'),
        Card(3,'clubs'),
        ]

hand_b = [
        Card(2,'clubs'),
        Card(3,'clubs'),
        Card(3,'clubs'),
        ]

print(compare(hand_a, hand_b))
