# Guess The Number: The Game
# Kyle Shannon 
# Oct 25th 2013


import simplegui
import math
import random

# initialize global variables used in your code
secret_number = 100
count = 7

# helper function to start and restart the game
def new_game():
    global secret_number
    global count
    count = 7
    secret_number = random.randrange(0, 100)
    return secret_number    

# button that changes range to range [0,100) and restarts
def range100():
    print "Ok you are starting a new game!" 
    print "Guess the number between 0 - 100"
    print
    new_game()
    global count
    count = 7
    global secret_number
    secret_number = random.randrange(0, 100)

# button that changes range to range [0,1000) and restarts
def range1000():
    print "Ok you are starting a new game!" 
    print "Guess the number between 0 - 1000"
    print
    new_game()  
    global secret_number
    secret_number = random.randrange(0, 1000)
    global count
    count = 10
       
# Game logic
def input_guess(guess):

    guess = int(guess) 
    global count
    
    if count == 0:
        print "You guessed:", guess, "That is wrong!"
        print "You are out of guesses!"
        print "Beginning new game... Insert $0.50"
        new_game()
    
    elif guess == secret_number:
        count = count - 1
        print "You guessed:", guess
        print "You Win! with", count, "guesses left"
        print
        print "Ok you get a free bonus round!" 
        print "Guess the number between 0 - 100"
        print
        new_game()
    
    elif guess > secret_number:  
        count = count - 1
        if count == 0:
            print "You guessed:", guess
            print "You are out of guesses!"
            print
            print "Beginning new game... Insert $0.50"
            print "Now pick a number between 1 - 100"
            print
            new_game() 
        else:
            print "You guessed:", guess
            print "You have", count, "guesses remaining."
            print "Try guessing lower." 
            print
    
    else: 
        count = count - 1
        if count == 0:
            print "You guessed:", guess
            print "You are out of guesses!"
            print
            print "Beginning new game... Insert $0.50"
            print "Now pick a number between 1 - 100"
            print
            new_game()
        else:
            print "You guessed:", guess
            print "You have", count, "guesses remaining."
            print "Try guessing higher."
            print
   
# create frame
frame = simplegui.create_frame("Guess The Number!", 300, 200)
button1 = frame.add_button("100 Number Game", range100, 150)
button2 = frame.add_button("1000 Number Game", range1000, 150)
input = frame.add_input("What is your guess?", input_guess, 150)

# call new_game and start frame
frame.start()
new_game()
print "Welcome to 'Guess The Number!' " 
print "Let's begin. Try guessing a number between 1 - 100"
print
