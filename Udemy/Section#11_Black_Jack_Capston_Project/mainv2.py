import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

exit_game = False

def game_cycle():
    your_cards = []
    computer_cards = []
    for i in range(2):
        your_cards.append(cards.pop(random.randrange(0, 52)))
        computer_cards.append(cards.pop(random.randrange(0, 52)))
    print(your_cards)
    print(computer_cards)



while not exit_game:
    desire = input("Would you like to play game 'y', 'n', or quit 'q': ")
    if desire == 'q':
        exit_game = True
    else:
        game_cycle()


