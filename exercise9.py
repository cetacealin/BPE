'''Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.'''

import random

number = random.randint(1, 9)
guess = 0

def guessing_game():
    number = random.randint(1, 9)
    guess = 0
    while (guess != number):
        guess = int(input("Guessing Game! Enter a number from 1-9: "))

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("You win!")

def main():
    guessing_game()

main()




