# A simple stopwatch game
# 2012

import simplegui

# global variables
time = 0
x = 0
y = 0

# format the time
def format(t):
    a = t // 600
    b = ((t // 10) % 60) // 10
    c = ((t // 10) % 60) % 10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

# format the score
def score():
    global x, y
    return str(x) + "/" + str(y)

# event handlers for "Start", "Stop" and "Reset"
def start():
    timer.start()

def stop():
    global x, y
    if timer.is_running():
        y += 1
        if time % 10 == 0:
            x += 1
    
    timer.stop()
    
def reset():
    global time, x, y
    timer.stop()
    time = x = y = 0
    
# event handler for timer
def timer_handler():
    global time
    time += 1

# draw handler
def draw(canvas):
    global time
    canvas.draw_text(format(time), (100, 120), 50, "White")
    canvas.draw_text(score(), (225, 30), 30, "Green")

# create frame
frame = simplegui.create_frame("Timer", 300, 200)

start_button = frame.add_button("Start", start, 200)
stop_button = frame.add_button("Stop", stop, 200)
label = frame.add_label("")
reset_button = frame.add_button("Reset", reset, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()
