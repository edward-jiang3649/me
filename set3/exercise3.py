"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
import random


def super_asker(low, high, message):

    while True:
        try:
            ask_for_number = int(input(message))
            print(f"​​{ask_for_number}​​​​​​​​ is a number")
            if low < ask_for_number < high:
                return ask_for_number
        except Exception:
            print("no")


def advancedGuessingGame():

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")

    lowerBound = super_asker(-1000, 1000, "Enter a lower bound: ")
    upperBound = super_asker(lowerBound + 1, 1000, "Enter an upper bound: ")

    actualNumber = random.randint(lowerBound + 1, upperBound - 1)

    while True:
        guessedNumber = super_asker(lowerBound, upperBound, "Guess a number: ")
        print("The number you guessed is {​​​​​​​​}​​​​​​​​,".format(guessedNumber))
        if guessedNumber == actualNumber:
            print("You guessed it!! It was {​​​​​​​​}​​​​​​​​".format(actualNumber))
            return "You got it!"
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        elif guessedNumber > actualNumber:
            print("Too big, try again :'(")

    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
