# Maxwell Rider
# September 23 2020

# A very simple number guessing game where you guess a number between 1 and 100 
# and the computer tells you if its too high or too low
# This is simply to help boost my python knowledge as I am very much a beginner as of writting this

from __future__ import print_function
import random

def higherOrLower():
    numToGuess = random.randint(1, 100)
    userNum = None
    
    while userNum != numToGuess:
        userNum = int(input("Guess my number (between 1 and 100): "))
        if userNum > numToGuess:
            print("To high!")
        elif userNum < numToGuess:
            print("To low")
        else:
            break   
    print("You got my number!")

if __name__ == "__main__":
    higherOrLower()
    playAgain = input("Want to play again? Y/N: ")
    
    if playAgain == "Y" or playAgain == "y":
        higherOrLower()
    else:
        print("Thanks for playing!")