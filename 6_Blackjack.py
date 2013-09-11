# Blackjack
# 2012

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

#global variables
in_play = False
outcome = "Hit or Stand?"
score = 0

#cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
class Hand:
    def __init__(self):
        self.cards = []	# create Hand object

    def __str__(self):
        self.ans = "Hand contains"
        # return a string representation of a hand
        for card in self.cards:
            self.ans += " " + str(card)
        return self.ans
            
    def add_card(self, card):
        self.cards.append(card) # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        self.value = 0
        self.ace = False
        for card in self.cards:
            self.value += VALUES[card.get_rank()]
            if 'A' in card.get_rank(): self.ace = True
        if self.ace:
            if self.value + 10 <= 21:
                return self.value + 10
            else:
                return self.value
        else:
            return self.value
        
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0]
        
class Deck:
    def __init__(self):
        self.cards = []	# create a Deck object
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # add cards back to deck and shuffle
        Deck()
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop(len(self.cards) - 1)
    
    def __str__(self):
        ans = "Deck contains"
        # return a string representing the deck
        for card in self.cards:
            ans += " " + str(card)
        return ans

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, score

    player_hand = Hand()
    dealer_hand = Hand()
    deck = Deck()
    deck.shuffle()
    outcome = "Hit or Stand?"

    if in_play: score -= 1

    for i in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

    in_play = True
    

def hit():
    global player_hand, in_play, score, outcome

    if in_play:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            print "You have busted"
            outcome = "You lost. New deal?"
            score -= 1
            in_play = False
       
def stand():
    global in_play, dealer_hand, player_hand, score, outcome

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        
        in_play = False
        
        if dealer_hand.get_value() > 21:
            outcome = "You win. New deal?"
            score += 1
        elif player_hand.get_value() <= dealer_hand.get_value():
            outcome = "You lose. New Deal?"
            score -= 1
        else:
            outcome = "You win. New deal?"
            score += 1

# draw handler    
def draw(canvas):
    global player_hand, dealer_hand, in_play, score, outcome
    
    canvas.draw_text("Blackjack", [150, 70], 80, "White")
    canvas.draw_line((50, 95), (550, 95), 4, "White")
    canvas.draw_text("Dealer", [100, 150], 40, "White")
    canvas.draw_text("Player", [100, 350], 40, "White")
    
    dealer_hand.draw(canvas, [100, 170])
    player_hand.draw(canvas, [100, 370])
    
    canvas.draw_text(outcome, [200, 520], 40, "White")
    canvas.draw_text("Score: " + str(score), [100, 580], 40, "White")
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 170 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE) 

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
player_hand = Hand()
dealer_hand = Hand()
frame.start()