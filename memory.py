#http://www.codeskulptor.org/#user24_AOZj2sDzN2_19.py

# Memory: The Game
# Kyle
# Nov. 15, 2013

import simplegui
import random

# Created 2 lists of 0 - 7 then shuffle them together.
set_1 = range(8)
set_2 = range(8)
cards = set_1 + set_2
random.shuffle(cards)
exposed = [False] * 16
state = 0
turns = 0
card1 = 0
card2 = 0

# helper function to initialize globals
def new_game():
    global cards, turns, state, exposed
    state = 0
    turns = 0
    random.shuffle(cards)
    exposed = [False] * 16
     
# define event handlers
def mouseclick(pos):
    global cards, exposed, state, turns, card1, card2
    
    card_clicked = pos[0] // 50
    
    if exposed[card_clicked] == True:
        print "Click on another card Please"
        return
    elif exposed[card_clicked] == False:
        exposed[card_clicked] = True
        if state == 0:
            state = 1
            card1 = card_clicked
            #print state
            #print "card1:", [card1]
        elif state == 1:
            state = 2
            card2 = pos[0]//50
            exposed[card_clicked] = True
            turns += 1
            #print state
            #print "card2:", [card2]

        elif state == 2:
             if cards[card1] != cards[card2]:
                exposed[card1] = False
                exposed[card2] = False
             card1 = pos[0]//50
             #print "card1:", [card1]
             state = 1 
             #print state       
        return card_clicked
    #print state
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed
    ctr_pos = [15, 65]
    up_left_crn = [0, 0] 
    btm_left_crn = [0, 100]
    btm_right_crn = [50, 100]
    up_right_crn = [50, 0]
    
    for n in range(len(cards)):
        if exposed[n] == True:
            canvas.draw_text(str(cards[n]), ctr_pos, 40, 'white')
            canvas.draw_polygon([up_left_crn, btm_left_crn, btm_right_crn,
                                 up_right_crn], 4, 'White')
        elif exposed[n] == False:
            canvas.draw_polygon([up_left_crn, btm_left_crn, btm_right_crn,
                                 up_right_crn], 4, 'White', 'Green')
        up_left_crn[0] += 50
        btm_left_crn[0] += 50
        btm_right_crn[0] += 50
        up_right_crn[0] += 50
        ctr_pos[0] = ctr_pos[0] + 50
     
    label.set_text("Turns = "+ str(turns))
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()







