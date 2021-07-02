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

    lower_Bound = super_asker(-1000000, 100000, "Enter an lower bound: ")
    upper_Bound = super_asker(lower_Bound, 100000, "Enter an upper bound: ")

    actual = random.randint(lower_Bound, upper_Bound)

    guard = 0
    while guard < 1000:
        guard += 1
        guess = super_asker(lower_Bound, upper_Bound, "Guess a number in this range")
        if guess == actual:
            return "You got it"
        elif guess < actual:
            print("Too Low, Guess Higher")
        elif guess > actual:
            print("Too High, Guess Lower")

    if __name__ == "__main__":
        print(advancedGuessingGame())


def super_asker(
    low=int(input("Enter lower bound number: ")),
    high=int(input("Enter higher bound number: ")),
):

    numbers = range(low, high)
    num = input("Please input an integer: ")
    while type(num) != int:
        num = input("Error. Please input an INTEGER: ")
        while num in numbers:
            return num + "is an integer"
    else:
        return "false"
