from art import logo
from art import vs
import random
from game_data import data

# ask_and_check
def ask():
    print(logo)
    rand_a = random.randint(0, 49)
    rand_b = random.randint(0, 49)
    print(f"Compare A: {data[rand_a]['name']}, a {data[rand_a]['description']}, from {data[rand_a]['country']}")
    print(vs)
    print(f"Compare B: {data[rand_b]['name']}, a {data[rand_b]['description']}, from {data[rand_b]['country']}")
    print(data[rand_a]['follower_count'])
    print(data[rand_b]['follower_count'])
    guess = input("Who has more followers? Type 'A' or 'B': ")
    return check(rand_a, rand_b, guess)

def ask2(score):
    print(logo)
    rand_a = random.randint(0, 49)
    rand_b = random.randint(0, 49)
    print(f"You are right! Current score is: {score}.")
    print(f"Compare A: {data[rand_a]['name']}, a {data[rand_a]['description']}, from {data[rand_a]['country']}")
    print(vs)
    print(f"Compare B: {data[rand_b]['name']}, a {data[rand_b]['description']}, from {data[rand_b]['country']}")
    print(data[rand_a]['follower_count'])
    print(data[rand_b]['follower_count'])
    guess = input("Who has more followers? Type 'A' or 'B': ")
    return check(rand_a, rand_b, guess)

# Check guess
def check(rand_a, rand_b, guess):
   rand_a = data[rand_a]['follower_count']
   rand_b = data[rand_b]['follower_count']
   winner = 'a'
   if rand_a > rand_b:
        winner = 'a'
   else:
        winner = 'b'
   if winner == guess:
        return True

   else:
        return False

def game():
    score = 0
    tmp = 0
    result = True
    while True:
        if score > tmp:
            result = ask2(score)
            tmp = score
        else:
            result = ask()
        if not result:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        else:
            score += 1
            print(f"Your score is {score}")

def game_loop():
    play_answer = True
    while play_answer:
        play_answer = (input('Do you want to play "High/Low Game?" Type "Y" or "N" ')).lower()
        if play_answer == 'y':
            game()
        else:
            play_answer = False

game_loop()
