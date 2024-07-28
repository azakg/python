import random
from text import logo

print(logo)


def game(level):
    attempts = 0
    if level == 'hard':
        attempts = 10
    else:
        attempts = 5
    chosen_number = random.randint(1,100)

    while True:
        print(f"You have {attempts} attempts remaining to guess the number")
        attempts -=1
        if attempts > 0:
            guess = int(input("Make a guess: "))
            if guess < chosen_number:
                print("Too low\nGuess again")
            elif guess > chosen_number:
                print("Too high\nGuess again")
            else:
                print(f"Congratulation you win, guessed number was: {chosen_number}")
                break
        else:
            print(" You loose, you have 0 attempts")
            break





print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level_of_the_game = input("Choose a difficulty. Type 'easy' or 'hard': ")
game(level_of_the_game)