import random
import sys


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = []
computer = []

def random_distribution_all():
    counter = 1
    while True:
        counter += 1
        random_user = random.randint(0, len(cards))
        user.append(cards.pop(random_user-1))
        random_computer = random.randint(0, len(cards))
        computer.append(cards.pop(random_computer-1))
        if counter > 2:
            break
def random_distribution_user():
    random_user = random.randint(0, len(cards))
    user.append(cards.pop(random_user - 1))

def random_distribution_computer():
    random_computer = random.randint(0, len(cards))
    computer.append(cards.pop(random_computer - 1))

def sum1(list1):
    sum_of_list = 0
    for i in list1:
        sum_of_list += i
    return sum_of_list

question1 = input("Do you want to play a BlackJank game? Type 'y' or 'n': ")
if question1 == 'y':
        random_distribution_all()
else:
    print("Come next time to play.\nBye, bye!")
    sys.exit()

def print_result1():
    print(f"Your cards: {user}, current score: {sum1(user)}")
    print(f"Computer's first card: {computer[0]}")

def print_result2():
    print(f"Your number is {sum1(user)}")
    print(f"Computer number is {sum1(computer)}")
    print("###################################################")
    if sum1(user) <= 21 and sum1(user) > sum1(computer) < 21:
        print("You win 😃")
    elif sum1(computer) <= 21 and sum1(computer) > sum1(user) < 21:
        print("Computer win!")
    elif sum1(user) > 21 and sum1(computer) > 21:
        print("Draw")
    elif sum1(user) <= 21 and sum1(computer) <= 21:
        print("Draw")
    else:
        print("Computer win")


print_result1()

question2 = input("Type 'y' to get another card, type 'n' to pass: ")

if question2 == 'y':
    random_distribution_user()

if sum1(computer) < 17:
    random_distribution_computer()

print_result2()
