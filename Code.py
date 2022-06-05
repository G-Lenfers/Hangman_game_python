# -*- coding: utf-8 -*-
"""
###   Course info   ###
Pirple.com
Python is Easy
09 - Importing
Project #2: Hangman

###   Student/Author info   ###
Guilherme Lenfers Dornelles
09/08/2021
Santa Catarina - Brazil

###   Code info   ###
Hangman Game
The code has two options implemented
    1 - Single player mode
    2 - Two players mode
        
###   Table of Contents   ###
    1. Packages
    2. Functions
    3. Initializing variables
    4. Main
"""

####################
###   PACKAGES   ###
####################

#Be able to deal with diacritics
from re import sub

#Picks up a random word for single player mode
from random import choice

#####################
###   FUNCTIONS   ###
#####################

#All-in-one print function
def Printing_and_Drawing(wrong_letters, correct_letters, word):
    
    print() #Stay a bit away from user input
    First_Print(wrong_letters)
    Draw_Hangman(len(wrong_letters))
    Second_Print(word, correct_letters)
    print() #Stay a bit away from the underscores above

#Function for clearing the screen
def Clear_Screen():
    """
    The author has been developing this code through Spyder environment in 
    Windows 10. Any of the following commands was able to hide the secret 
    word provided by the first player by clearing the screen. However, by 
    doing so, it voids the next input prompt, producing undesired results.
    
    An alternative would be displaying asterisks as the player keeps
    typing. The author tried the getpass method from the getpass package.
    Unfortunately, the Kernel displays the following warning:
    "Warning: QtConsole does not support password mode, the text you type 
    will be visible." 
    According to Carlos Cordoba (a developer of Spyder): "This is a 
    limitation of Spyder/QtConsole, not of getpass itself."
    
    Instead of solving this, the author figured out it would be much 
    simpler to print a bunch of new lines and hoping the players will
    have a decent amount of sportsmanship to not scroll up the console
    and seeing what was the secret word.
    
    If you are running this code in another terminal or Operational
    System, you can uncomment any of the following comands to clear up
    the screen
    """
    print("\n\n\n\n\n\n\n\n\n\n\n\n" + 
          "\n\n\n\n\n\n\n\n\n\n")
    
    #print(chr(27) + "[2J") #clear terminal

    #print("\033[H\033[J") 
    
    #print(chr(12))

    #import os
    #os.system('cls')
    
    #This one needs the following package pre-loaded
    #from IPython import get_ipython
    #try:
    #    get_ipython().magic('clear')
    #except:
    #    pass


#Function for printing the wrongly guessed letters
def First_Print(guesses):
    print("You have tried the following letters:")
    for letter in guesses:
        print(letter.capitalize(), "- ", end="")
    print()

#Function for drawing the hangman
def Draw_Hangman(tries):
    
    #Initializing hangman's body variables
    complete_body = ["O", "|", "`--", "--´", "/", "\\"]
    blank_body = [" ", " ", "   ", "   ", " ", "  "]
    actual_body = []

    #Getting to know how many body parts our function should draw
    for i in range(len(complete_body)):
        if i+1 <= tries:
            actual_body.append(complete_body[i])
        else:
            actual_body.append(blank_body[i])
    
    #Printing
    print("  - - - - - - - -")
    print("  |             |")
    print("  |             ", end="")
    print(actual_body[0]) #head
    print("  |         ", actual_body[2] + #left arm
          actual_body[1] + #torso
          actual_body[3])  #right arm
    print("  |            ", actual_body[1]) #torso
    print("  |            ", actual_body[1]) #torso
    print("  |           ", actual_body[4],  #left leg
          actual_body[5]) #right leg
    print("  |          ", actual_body[4], #left leg
          " ", actual_body[5]) #right leg
    print("  |")
    print("--------")
    print()


#Function for printing the correctly guessed letters
#It also prints underscore if the player has not guessed it yet
def Second_Print(word, guesses):
    
    for letter in word:
        
        #The player guessed it correctly
        if letter in guesses:
            print(letter.capitalize()+ " ", end="")
            
        #There is a blank space in the secret word
        elif letter == " ":
            print("  ", end="")
            
        #The player does not know this letter yet
        else:
            print("_ ", end="")
    
    #We must avoid errors with the last print having end=""
    print() 


#Function for removing diacritics
def Remove_Diacritics(word):
    
    """
    We are dealing with Brazilian players, so they might come up with
    some diacritics/glyphed words. This Function removes them, allowing
    the code to be able to make comparisons.    
    """
    
    word = sub(u"[àáâã]", "a", word)
    word = sub(u"[èéê]", "e", word)
    word = sub(u"[ìíî]", "i", word)
    word = sub(u"[òóôõ]", "o", word)
    word = sub(u"[ùúûü]", "u", word)
    word = sub(u"[ç]", "c", word)
    
    return word

#Function for comparing the player's guess with the secret word
def Comparing(word, guess):
    
    for letter in word:
        
        #Player's guessed letter is inside the secret word
        if letter == guess:
            return True
    
    #Player have not got it right
    return False
            
#Function for checking if the player has won or lost the game
def End_Game_Checkings(wrong_letters, correct_letters, word):
    
    #In the case player has lost the game
    if len(wrong_letters) == 6:
        
        #Final Printings
        Printing_and_Drawing(wrong_letters, correct_letters, word)
        print("You lost the game")
        print("The secret word was:", word)
        
        #Get out of the main loop
        return False
    
    #In the case player has won the game
    missing = 0
    
    for letter in word:
        if letter in correct_letters:
            pass
        elif letter == " ":
            pass
        else:
            missing += 1
    
    #If there are no more letters to discover, the player has won the game
    if missing == 0:
        
        #Final printings
        Printing_and_Drawing(wrong_letters, correct_letters, word)
        print("Congratulations!!")
        print("You have just won the game!")
        
        #Get out of the main loop
        return False
    
    #The game is still running
    return True
    
            
#Function for choosing a random word from a text file
def Single_Player_Mode():
    
    #File handling
    file = open("banco_de_palavras.txt", "r", encoding="utf-8")
    words = file.readlines()
    file.close()
    
    #removing \n at the end of each item
    words = [line.strip() for line in words]
    
    #Picking up a random word and removing diacritics
    raw_word = choice(words)
    word = Remove_Diacritics(raw_word)
    
    return word

    
#Function for asking another player for an input
def Two_Players_Mode():
    
    #First player picks up a word
    raw_word = input("What secret word will you pick up? ")
    word = Remove_Diacritics(raw_word)
 
    #Hiding it from the second player
    Clear_Screen()
    
    return word


def Main_Game(wrong_letters, correct_letters, word, Playing = True):

    while Playing == True:
    
        #Printing and drawing on the console
        Printing_and_Drawing(wrong_letters, correct_letters, word)
    
        #Ask the player for a letter
        raw_guess = input("Type the letter you think the secret" + 
                          " word contains: ")
        
        #Staying safe in the case player is with CAPS LOCK on
        guess = raw_guess.lower()
        
        #Verifies if guess is inside word
        player_got_right = Comparing(word, guess)
        
        #Updating variables
        if player_got_right == True:
            correct_letters.append(guess)
        else:
            wrong_letters.append(guess)
            
        #Checking if the game has just finished
        Playing = End_Game_Checkings(wrong_letters, correct_letters, word)

##################################
###   INITIALIZING VARIABLES   ###
##################################


#Guesses from the player
correct_letters = []
wrong_letters = []

#Texts for input
text_game_mode = ("Select which mode do you want to play:\n" + 
                  "Type 1 for single player mode\n" +
                  "Type 2 for two players mode\n")

# text_difficulty = ("Select game's difficulty:\n"+
#                        "Type 1 for Normal Mode (6 tries)\n" + 
#                        "Type 2 for Easy Mode (   )\n")

################
###   MAIN   ###
################


#Choosing between single player or 2 players mode
game_mode = input(text_game_mode)

#Single player
if game_mode == "1":
    
    word = Single_Player_Mode()
    Main_Game(wrong_letters, correct_letters, word)
    
#Two Players Mode
elif game_mode == "2":
    
    word = Two_Players_Mode()
    Main_Game(wrong_letters, correct_letters, word)

else:
    #Must run the whole program again
    print("Please type 1 or 2 for choosing the game mode")
