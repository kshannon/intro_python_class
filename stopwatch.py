# "Stopwatch: The Game"
# Kyle Shannon  
# Oct 31, 2013

import simplegui

# define global variables
count = 0
wins = 0
tries = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(count):
    global D
    num = int(count / 10) 
    if count == 0:
        A = 0
        sec_string = str(0) + "0"
        D = 0
    elif count != 0:
        A = num / 60 
        sec = num % 60
        if sec < 10:
            sec_string = "0" + str(sec)
        else:
            sec_string = str(sec) 
        D = str(count)[-1:]
    return str(A) + ":" + str(sec_string) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    timer.start()

def stop_button():
    global wins, tries, count
    if timer.is_running():
        tries += 1   
    if timer.is_running() and count % 10 == 0:
        wins = wins + 1 
    timer.stop()
  
def restart_button():
    global count, wins, tries
    timer.stop()
    count = 0
    wins = 0
    tries = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(count), [95, 150], 50, "White")
    canvas.draw_text("Wins = " + str(wins) + " / " + "Tries = " +
                     str(tries), [100, 50], 20, "Yellow")

# create frame
frame = simplegui.create_frame("Stopwatch Game!", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
start = frame.add_button('Start', start_button, 100)
stop = frame.add_button('Stop', stop_button, 100)
restart = frame.add_button('Restart', restart_button, 100)

# start frame
frame.start()




