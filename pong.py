http://www.codeskulptor.org/#user23_wrbYaL3ZlvtW6nA_26.py

# Pong: The Game
# Kyle Shannon
# November 10, 2013


import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 12
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

hit_count = 0

score1 = 0
score2 = 0

ball_vel = [1, 1]
ball_pos = [WIDTH / 2, HEIGHT / 2]

paddle1_pos = [3,160,3,240]
paddle2_pos = [596,160,596,240]

paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global hit_count, ball_pos, ball_vel # these are vectors stored as lists
    hit_count = 0
    ball_pos[0] = WIDTH // 2
    ball_pos[1] = HEIGHT // 2
    
    if direction == RIGHT:
         ball_vel[0] = random.randrange(120/60, 240/60)
         ball_vel[1] = - random.randrange(120/60, 240/60)
    elif direction == LEFT:
         ball_vel[0] = - random.randrange(120/60, 240/60)
         ball_vel[1] = - random.randrange(120/60, 240/60)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
   
    score1 = int(0)
    score2 = int(0)
    
    paddle1_pos = [3,160,3,240]
    paddle2_pos = [596,160,596,240]
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(random.choice([True, False]))
    
def hit_count():
    global hit_count
    if hit_count == 3:
        print "yay"

# Draws ball, paddle and gutters onto camvas and updates/handles collisions
def draw(c):
    global hit_count, score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    # draw midline and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 2, "Lime")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 2, "Lime")
        
    # update ball
    ball_pos [0] += ball_vel [0]
    ball_pos [1] += ball_vel [1]
    
    #Collision and Reflection off of Top and Bottom Walls
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    #Test to see if ball passes into gutter
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos[1] <= ball_pos[1] <= paddle1_pos[3]:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += 1
            hit_count += 1
        else:
            score2 += 1
            spawn_ball(RIGHT)
   
    if ball_pos[0] >= WIDTH - (BALL_RADIUS + PAD_WIDTH):
        if paddle2_pos[1] <= ball_pos[1] <= paddle2_pos[3]:
            ball_vel[0] =-  ball_vel[0]
            ball_vel[0] -= 1
            hit_count += 1
        else:
            score1 += 1
            spawn_ball(LEFT)
            

      
    # draw ball
    c.draw_circle(ball_pos, 10, 5, 'WHITE', 'WHITE')
    
    # updating paddle's vertical position, and checking to see if paddle_vel
    # moves paddle off canvas. If true, dissalow move.
    if (paddle1_pos [1] + paddle1_vel >= 0) and (paddle1_pos [3] + paddle1_vel <= HEIGHT):
        paddle1_pos [1]  += paddle1_vel
        paddle1_pos [3]  += paddle1_vel

    if (paddle2_pos [1] + paddle2_vel >= 0) and (paddle2_pos [3] + paddle2_vel <= HEIGHT):
        paddle2_pos [1]  += paddle2_vel
        paddle2_pos [3]  += paddle2_vel
    
    # draw paddles
    c.draw_line ((paddle1_pos[0],paddle1_pos[1]),
                     (paddle1_pos[2],paddle1_pos[3]),8, "yellow")
    c.draw_line ((paddle2_pos[0],paddle2_pos[1]),
                     (paddle2_pos[2],paddle2_pos[3]),8, "yellow")    
    
    # draw scores on canvas
    c.draw_text(str(score1), (230, 50), 40, 'white')
    c.draw_text(str(score2), (350, 50), 40, 'white')
    
# When 'w, s, up, down' are pressed down paddle_vel increases        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 6
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel =+ 6
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel =- 6
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel =+ 6

# When 'w, s, up, down' are not pressed paddle_vel is 0        
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

# Starts new game and resets score 1 & 2 back to 0      
def button_handler():
    new_game()
        

# create frame & button
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('New Game', button_handler)

# start frame
new_game()
frame.start()



