import sys
import random

import game_list

while True:
    game_start = input("Do you want to start game, type 'y' or 'n': ")
    if game_start.lower() == 'n':
        sys.exit()
    elif game_start.lower() == 'y':
        gamer_choice = int(input("What is your choice 0, 1 or 2: "))
        print(f"Your choice: \n{game_list.list[gamer_choice]}\n")
        computer_choice = random.randint(0,2)
        print(f"Computer choice {game_list.list[computer_choice]}")
        if gamer_choice ==0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and gamer_choice == 2:
            print("You lose!")
        elif gamer_choice < computer_choice:
            print("You lose!")
        elif gamer_choice > computer_choice:
            print("You win!")
        elif gamer_choice == computer_choice:
            print("Drow, try again.")

        # if gamer_choice == computer_choice:
        #     print("Drow, try again.")
        # elif gamer_choice < computer_choice and computer_choice != 2 or computer_choice == 0 and gamer_choice == 2:
        #     print("Computer won!")
        # elif computer_choice < gamer_choice and gamer_choice != 2 or gamer_choice == 0 and computer_choice ==2:
        #     print("You won!")



