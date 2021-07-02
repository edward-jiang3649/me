"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():

    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\n Welcome to the guessing game!")
    print("A number between _ and _ ?")

    low = super_asker(-1000000, 100000, "Enter an lower bound: ")
    high = super_asker(low, 100000, "Enter an upper bound: ")

    actual = random.randint(low, high)

    guard = 0
    while guard < 1000:
        guard += 1
    guess = super_asker(low, high, "Guess a number in this range")
    if guess == actual:
        return "You got it"
    elif guess < actual:
        print("Too Low, Guess Higher")
    elif guess > actual:
        print("Too High, Guess Lower")

    if __name__ == "__main__":
        print(advancedGuessingGame())


def super_asker(low, high, message):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    while True:
        try:
            askfornumber = input(message)
            print(askfornumber, "here")
            askfornumber = int(askfornumber)
            print("{} is a number".format(askfornumber))
            if low < askfornumber < high:
                print("well done, {} is within range".format(askfornumber))
                return askfornumber
        except Exception as e:
            print(f"{e} is not a number **")
