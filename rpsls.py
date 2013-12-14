# Rock-paper-scissors-lizard-Spock: The Game 
# Kyle Shannon
# 10/19/2013



# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


#Function name is number_to_name. Takes in an argument (number) which is an integer
#and returns a string, which corresponds to the number. Using an if/elif/else 

import random

def number_to_name(number):    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"

#Function name is name_to_number. Takes in an argument (name) which is a string
#and returns a number, which corresponds to the name. Using an if/elif/else    
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



def rpsls(name): 
    player_number = name_to_number(name) # Setting player_number to match the numbers

    comp_number = random.randrange(0,5,1) #randomy generate number for computer

    difference = ((player_number - comp_number) % 5) # Compare difference and used modulus becuase each number can win against 2 other numbers and lose to 2 other numbers.
    if (difference == 1 or difference == 2): # Comparing and if diff has remainder 1 or 2 from modulus equation, player wins
        result = "player wins!"
    elif difference ==0: # If no remainder, there is a tie
        result = "Player and Computer tie!"
    else: # if any other remainder computer wins
        result = "Computer wins!"

    print "Player chooses" ,name
    print "Computer chooses" ,number_to_name(comp_number)
    print result 
    print

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



