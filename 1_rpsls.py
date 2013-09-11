# Rock, Paper, Scissors, Lizard, Spock
# 2012

import random

def rpsls(name):
    player_guess = name_to_number(name)
    comp_number = random.randrange(0, 5)
    result = (player_guess - comp_number) % 5
    
    print "Player chooses " + name
    print "Computer chooses " + number_to_name(comp_number)

    if result == 0:
        print "Player and computer tie!\n"
    elif result == 1 or result == 2:
        print "Player wins!\n"
    else:
        print "Computer wins!\n"
        
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4

def number_to_name(num):
    if num == 0:
        return "rock"
    elif num == 1:
        return "Spock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "lizard"
    elif num == 4:
        return "scissors"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")