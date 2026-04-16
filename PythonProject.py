#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Describe how to play your game, including any rules
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Higher or lower - with a twist
# The game will present the user with a card - example, A♠ and how much it's worth: 56. The cards worth/point depends on its number and its suit. The higher
# the number, the more points the card gains [Jake (J) - 11, Queen (Q) - 12, King (K) - 13, Ace (J) - 14]. The suits multiples the number [♠ = 4, ♥ = 3, ♣ = 2, ♦ = 1] - 
# for example, A = 14 and the suit ♠ (x4) will multiple 14 by 4. In total the cards is worth 56 points. After you have recieved your card, the game will allow the user
# to decide if they would like to play that card against their opponent (the computer). To win against the opponent, the user must have a higher card point than it's opponent.
# If the user, plays their card and it's higher than the opponents card, the user will gain a point. If the user plays, but its card's worth is not higher than the 
# computer's card, the user will lose a point. If the player does not play their card, they will gain no point, and the computer will reveal its card. The user will
# have the opportunity to play again and continue with their point or end the game. 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#   Describe how you tested your code
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# For each piece of function, I tested them differently depending on the input.
# 
# No input needed from the user:
# ------------------------------
# Testing: intro() - Checked if the text are presented well and readable for the users
# Testing: card_number() - checked if the number/letter is picked at random
# Testing: card_suit() - checked if the suits are picked at random
# Testing: card_points(card_num, card_suit) 
#   - tested the for loop to check if the number is matching with the card_number
#   - check if the if statement works correctly is the card_number is a letter
#   - used print statements to identify if the points have been multipled correctly depending on the suits
#   - checked if the variable points is being returned correctly
# Testing: card() - checked if all the previous functions return as an array
# Testing: compare(users_card_points, computer_card_points, computers_card_num, computers_card_suit)
#   - Using normal data types to check if the points are being compared correctly (points are being created depending if user wins [+1] or loses [-1])
#   - Identified if the return value is being return correctly
# Errors faced:
#   - Displaying points: scores were being calculated incorrectly 
#   - Adding/Subtracting player scores was difficult to handle
#   - Scores were not being updated correctly
# Problem identified: Due to the point system being created inside a function, it caused the points to reset everytime it's called
# Changes made:
#  - removed the point system outside the compare() function. 
#  - added return values (1 or 2 or none) to identify how the points need to be changed
# Testing: leaderboard() 
#   - checked if file is being opened 
#   - checked if file is being appended with the correct username and point
#   - checked if username and point is being correctly stored in the dictionary
#   - checked if the lb dictionary is being returned 
# Changes made:
#   - was going to use a list - but might have been difficult to store (working with a 2d list)
# Inputs required from the user:
# ------------------------------
# Testing: main_game() 
#   - checked if card() function works within the main_game() function
#   - Checking if user wants to play their card or not:
#       -> Normal Data: 'y' or 'y' = (Expected Output: use the compare() function/continue)(Actual Output: use the compare() function/continue)
#                       'n' or 'N' = (Expected Output: Display computer's card/continue game)(Actual Output: Display computer's card/continue game)
#       -> Erroneous Data: 1 or ! = (Expected Output: Display error message)(Actual Output: Display error message)
#   - If user played with their card, check if the compare() function is working and returning the correct number
#   - Checked if points are being calculated correctly (not starting from zero/adding or subtracting)
#   - If user does not play, checked if computer's card is being displayed and no changes made to the players_score variable
# Testing: user()
#   - checked if user can input their username
#   - checked if user likes their name or not:
#    -> Normal Data: 'y' or 'y' = (Expected Output: Welcome User)(Actual Output: Welcome User)
#                    'n' or 'N' = (Expected Output: Allow user to change name)(Actual Output: Allow user to change name)
#    -> Erroneous Data: 1 or ! = (Expected Output: Display error message)(Actual Output: Display error message)
# Testing: Main Program
#   - checked if each function returns the right values and store it into the variable (Print out each variable)
#   - Tested User input:
#       -> Normal Data: 'y' or 'y' = (Expected Output: Play game)(Actual Output: Play game)
#                       'n' or 'N' = (Expected Output: Display players score/leaderboard)(Actual Output: Display players score/leaderboard)
#       -> Erroneous Data: 1 or ! = (Expected Output: Display error message)(Actual Output: Display error message)
#
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Allow randomisation
import random
#Allow delay 
import time

#Introduction/Rules
def intro():
    """
    Greets the user and displays rules
    
    Parameters:
    None
    
    Returns:
    None
    """
    print(""" \t\t\t\t\t -- CARD GAME --

    WELCOME! This is a very simple card game.

    ------
    RULES:
    ------
    - You will recieve a card, displayed like this: A♠
    - You will decide if you want to continue playing that card or resign..
    - How will you know if your card is good?
        -> Numbers - higher the number, higher the points [Example: 2 = 2 points]
        -> Jack [J] - 11
        -> Queen [Q] - 12
        -> King [K] - 13
        -> Ace [J] - 14

        -> The suits will multiple the points.. 
        Example: A♠ - A [Ace] = 14, ♠ = 4 -> 14*4 = 56
            - ♠ = 4
            - ♥ = 3
            - ♣ = 2
            - ♦ = 1
    - Your opponent is.. THE COMPUTER!! """)
    
    time.sleep(2) # Delays for 2 seconds 
    
    print("Now you are ready to play!")


# Pick Random Card - card_number() and card_suit()
def card_number():
    """
    Chooses a number/letter randomly
    
    Parameters:
    None
    
    Returns:
    num_choice: the choosen number/letter (1)
    """
    # Card Number Options
    num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    # Randomise - Picks a card number
    num_choice = random.choice(num)
    
    # returns the card number
    return num_choice

def card_suit():
    """
    Chooses a suit randomly
    
    Parameters:
    None
    
    Returns:
    suits_choice: the choosen suit (1)
    """
    # Card suit options
    suits = ["♠", "♣", "♥", "♦"]
    # Randomise - Picks a card
    suits_choice = random.choice(suits)
    
    # returns the suit number
    return suits_choice

# Create points
def card_points(card_num, card_suit):
    """
    Uses the num and suit to identify how much the card is worth
    
    Parameters:
    card_num: card_number() - uses this function to gain the number
    card_suit: card_suit() - uses this function to gain the suit
    
    Returns:
    point: card's worth in total
    """
    
    # Sets card point to 0
    point = 0
     
    num = ["2","3","4","5","6","7","8","9","10"]
    # Identify the card number to assign the points
    for i in range(len(num)):
        if card_num == num[i]:
            point = num[i]
        
        # If the card number is J,Q,K,A 
        elif card_num == 'J':
            point = 11
        elif card_num == 'Q':
            point = 12
        elif card_num == 'K':
            point = 13
        elif card_num == 'A':
            point = 14

    # Multiples the points depending on suit
    if card_suit == "♠":
        point = int(point)*4
    elif card_suit == "♥":
        point = int(point)*3
    elif card_suit == "♣":
        point = int(point)*2

    #Return the points
    return point

# Combine card and suits together as well as get points
def card():
    """
    Combines the card_num, card_suit and card_points to create the card for the player/computer 
    
    Parameters:
    None
    
    Returns:
    num, suits, points: return as a list
    """
    
    # Call each function and assign the return value into a variable
    num = card_number()
    suit = card_suit()
    points = card_points(num, suit)
    
    # Returns a list
    return num, suit, points


# Compare both card points - users and computers
def compare(users_card_points, computer_card_points, computers_card_num, computers_card_suit):
    """
    Compares users and computer's cards 
    
    Parameters:
    users_card_points: points calculated from card_points() function
    computer_card_points: points calculated from card_points() function
    computers_card_num: a list value from card() function -> card_num created by card_num()
    computers_card_suit: a list value from card() function -> card_suit created by card_suit()
    
    Returns:
    1 - if user wins 
    2 - if user loses
    none - if it's a draw
    """
    
    # If users card is greater than computers card
    if int(users_card_points) > int(computer_card_points):
        # Display winner
        print("USER HAS A HIGHER CARD!")
        # Display computer's card
        print(f"Computer's Card: {computers_card_num+computers_card_suit} (Points: {computer_card_points})")
        # Returns a number (1 = User won) - to identify the point system in the main_game() function  
        return 1
    
    # If users card is less than computers card    
    elif int(users_card_points) < int(computer_card_points):
        # Display winner
        print("COMPUTER HAS A HIGHER CARD!")
        # Display computer's card
        print(f"Computer's Card: {computers_card_num+computers_card_suit} (Points: {computer_card_points})")
        # Returns a number (2 = User lost) - to identify the point system in the main_game() function  
        return 2
        
    else:
        # Display draw
        print("It's a DRAW!")
        # Nothing to return - main_game() function will take 'None' as draw

# Main game - which brings all the functions together
def main_game(players_score):
    """
    Combines functions together depending on user's decision to allow for correct game play commands to be executed  
    
    Parameters:
    players_score: players current score
    
    Returns:
    players_score: players new score
    """
    time.sleep(1) #Delays for 1 seconds 
    
    # Calls the card() function - to generare a card for the player
    users_card = card()
    # Display card
    print(f"Your card is... {users_card[0]+users_card[1]}")
    print(f"Your card is worth: {users_card[2]}!")
    
    # Computer's Card
    computers_card = card()
    
    # Player decides if they would like to play with their card or not
    # Avoid errors - while loop added
    flag = True
    while flag:
        choose = input("Would you like to play this card against the computer? (Y or N)")
        # If user wants to play their card
        if choose.upper() == 'Y':
            # Calls the compare() function -> a number is returned
            result = compare(users_card[2], computers_card[2], computers_card[0], computers_card[1])
            
            # The number is compared
            # 1 = User won
            if result == 1:
                # Display score add on
                print("Players Score: +1")
                
                # Update score
                players_score += 1
                return players_score
            
            # 2 = User lost
            elif result == 2:
                # Display score removal
                print("Players Score: -1")
                
                # Update score
                players_score -= 1
                # players score has been changed - return their score
                return players_score
            
            # None = draw
            else:
                print("Players Score: +0")
                return players_score
            
        # If user does not want to play their card    
        elif choose.upper() == 'N':
            # Display computers card
            print(f"Awe.. The Computer's card was: {computers_card[0]+computers_card[1]} \nWorth: {computers_card[2]}") 
            
            # players score has not been changed - return their score
            return players_score
        
        # Human error
        else:
            print("Invalid input. Try again")
            # Loop the question again
            flag = True
        


#Leaderboard - store players name and score
def leaderboard(username, players_score):
    """
    Updates the score.txt file to keep a track of player's scores
    
    Parameters:
    username: their player's name
    players_score: players current score
    
    Returns:
    lb: a dictionary, updates to contain the player's username and score
    """
    
    # leaderboard = lb -> dictionary
    lb = {}
    
    # Open file in append mode 
    with open("score.txt", "a") as score_file:
        # update the score.txt file
        score_file.write(f"{username},{players_score}\n")

    # Open file in read mode 
    with open("score.txt", "r") as score_file:
        # read the file
        for line in score_file:
            # splits the player's name and score
            name, score = line.split(",")
            # append the player's name and score into the lb dictionary
            lb[name] = int(score)

    # return the dictionary
    return lb

# Asks for user's name
def user():
    """
    Player creates their username 
    
    Parameters:
    None
    
    Returns:
    username: player's name
    """
    
    flag = True
    while flag:
        # asks for user's name
        username = input("Enter a username: ")
        print("Your username: ",username)
        
        # confirms if user likes their name
        invalid = True
        while invalid:
            choice = input("Do you like your username? (Y/N)")
            # If user likes their name
            if choice.upper() == "Y":
                # welcome player
                print("WELCOME ",username)
                # return player's name
                return username

            # If user dislikes their name
            elif choice.upper() == "N":
                print("Let's change your name!")
                #avoids the second loop
                invalid = False
                #enables the loop
                flag = True
            
            # Human error
            else:
                # Display error message
                print("Invalid Input!!")
                # enable error
                invalid = True
        


# Play game
# Display rules/intructions
intro()

# Calls user() function to ask for user's name
username = user()

# Set players_score to 0
players_score = 0
# Calls the main_game() function -> stores players scores
players_score = main_game(players_score)
# Display players score
print("Current Score: ",players_score)

# Set flag to True - starts loop
flag = True
while flag:
    valid = True
    # ask for players choice to stop or continue to play
    choice = input("Would you like to play again? (Y or N)")
    while valid:
        # If user wants to continue
        if choice.upper() == "Y":
            # Calls the main_game() function -> stores players scores
            players_score = main_game(players_score)
            # Display players score
            print("Current Score: ",players_score)
            valid = False
        # If user does not want to continue playing
        elif choice.upper() == "N":
            # Display user's final score
            print(f"You're total score is: {players_score}")
            
            # Display leaderboard
            #Grab previous player's name and score
            lb = leaderboard(username, players_score)
                        
            # Display 
            print("Leaderboard: ")
            # Use format() to format the leaderboard table
            
            #---------------------------------------------------------------------
            # Author(s): W3Schools
            # Title: Python String format() Method
            # Version Number: 1
            # Date Accessed: 14 March 2025
            # Type: Example source code
            # Availability:https://www.w3schools.com/python/ref_string_format.asp
            #---------------------------------------------------------------------
            
            print("{:<10} {:>10}".format("Username", "Score"))
            
            # Display username, score in a table
            for key, value in lb.items():
                print("{:<10} {:>7}".format(key, value))
                
            valid = False
            flag = False
        else:
            # Human error - error msg
            print("Invalid Input, try again.")
            # enable loop
            invalid = True