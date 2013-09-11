# implementation of card game - Memory
# 2012
import simplegui
import random

deck = range(8) * 2
random.shuffle(deck)
state = moves = 0
card = [[0, 0], [0, 0]]
exposed = [False for n in range(16)]

# helper function to initialize globals
def init():
    pass

# define event handlers
def mouseclick(pos):
    global state, moves, card
    if exposed[pos[0] // 50] == False:
        if state == 0:
            exposed[pos[0] // 50] = True
            card[0][0] = deck[pos[0] //50]
            card[0][1] = pos[0] // 50
            state = 1
        elif state == 1:
            exposed[pos[0] // 50] = True
            card[1][0] = deck[pos[0] //50]
            card[1][1] = pos[0] // 50
            moves += 1
            state = 2
        elif state == 2:
            if card[0][0] == card[1][0]:
                exposed[card[0][1]] = exposed[card[1][1]] = True
            else:
                exposed[card[0][1]] = exposed[card[1][1]] = False
                
            exposed[pos[0] // 50] = True
            card[0][0] = deck[pos[0] //50]
            card[0][1] = pos[0] // 50
            state = 1
    label.set_text("Moves = " + str(moves)) 
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed
    card_pos = 25
    
    if all(exposed) == True:
        canvas.draw_text("You Won", (300, 80), 90, "White")
    else:    
        for card in range(16):
            #canvas.draw_text(str(deck[card]), (card * 50, 80), 90, "White")    
            if exposed[card] == False:
                canvas.draw_line((card_pos, 0), (card_pos, 100), 48, "Green")
            elif exposed[card] == True:
                canvas.draw_text(str(deck[card]), (card * 50, 80), 90, "White")
            card_pos += 50 

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")
# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
