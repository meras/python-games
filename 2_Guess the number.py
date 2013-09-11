# Guess the number game
# 2012

import simplegui
import random
import math

range = 0
guesses = 0
ran_num = 0

# initialize new game, determines guesses

def init():
    global ran_num
    global range
    global guesses
    
    guesses = math.ceil(math.log(range, 2))
    
    print "New game. Range is from 0 to", range
    print "Remaining guesses:", guesses
    print
    guesses -= 1
    ran_num = random.randrange(0, range)

# define event handlers for control panel
    
def range100():
    global range
    global guesses
    range = 100
    guesses =7
    init()

def range1000():
    global range
    global guesses
    range = 1000
    guesses = 10
    init()
    
# main game logic
def get_input(guess):
    global ran_numg 
    global guesses

    my_guess = int(guess)
    print "Guess was", my_guess
    print "Number of remaining guesses is", guesses
    
    if guesses > 0:
        if my_guess > ran_num:
            print "Lower"
            guesses -= 1
        elif my_guess < ran_num:
            print "Higher"
            guesses -= 1
        elif my_guess == ran_num:
            print "\nYou win\n"
            init()
    elif guesses == 0:
        print "\nYou lost"
        print "The secret number was", ran_num
        print
        init()
    print
        

# frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("0-100", range100, 200)
frame.add_button("0-1000", range1000, 200)
frame.add_input("Your guess", get_input, 200)

# start frame, set initial range
range100()
frame.start()
