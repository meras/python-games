# Implementation of classic arcade game Pong
# 2012
import simplegui
import random

# initialize globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0 , 0]

paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
vel_change = 8

# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0 , 0]
    if right:
        ball_vel[0] = random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3)
    elif not right:
        ball_vel[0] = -random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 3)

# event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2
    score1 = score2 = 0
    ball_init(True)

def increase_difficulty():
    global ball_vel
    if -11 < ball_vel[0] * 1.1 < 11:
        return 1.1
    else:
        return 1
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if (HALF_PAD_HEIGHT <= paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
    
    if (HALF_PAD_HEIGHT <= paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line((HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT), (HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT), PAD_WIDTH, "White")
    c.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT), (WIDTH -HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT), PAD_WIDTH, "White")    

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # bounce the ball off walls
    if ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    # bounce the ball off the paddles
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH: #gutter
        if (paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1]
        <= paddle1_pos + HALF_PAD_HEIGHT): #check if ball strikes paddle
            ball_vel[0] = - ball_vel[0] * increase_difficulty()
            print ball_vel
        else:
            score2 += 1
            ball_init(True)
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if (paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1]
        <= paddle2_pos + HALF_PAD_HEIGHT):
            ball_vel[0] = - ball_vel[0] * increase_difficulty()
            print ball_vel
        else:
            score1 += 1
            ball_init(False)
        
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1), (150, 100), 50, "White")
    c.draw_text(str(score2), (450, 100), 50, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= vel_change
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += vel_change
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= vel_change
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += vel_change
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel += vel_change
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= vel_change
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel += vel_change
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= vel_change

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
reset_button = frame.add_button("Reset", new_game, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()
new_game()