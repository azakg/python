import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
end_of_game = False
chosen_word = random.choice(word_list)
length_of_word = len(chosen_word)
display = []
lives = 6

for i in range(length_of_word):
    display.append('_')

while not end_of_game:
    print(f"Pssst, chosen word is: {chosen_word}")
    guess = input("Guess a letter: ")

    for i in range(length_of_word):
        if guess == chosen_word[i]:
            display[i] = guess
    if "_" not in display:
        print("You win")
    print(f"{''.join(display)}")
    if guess not in chosen_word:

        lives -= 1
    if lives ==0:
        print("You lose")
        end_of_game = True
    print(stages[lives])


