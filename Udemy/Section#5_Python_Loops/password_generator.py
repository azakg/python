import random
import string

def shuffle(l, s, n):
    letters = ""
    symbols = ""
    numbers = ""
    for i in range(int(l)):
        letters += random.choice(string.ascii_letters)
    for i in range(int(s)):
        symbols += random.choice(string.punctuation)
    for i in range(int(n)):
        numbers += random.choice(string.digits)

    chars = list(letters + symbols + str(numbers))
    random.shuffle(chars)
    final = ''.join(chars)
    print(f"This is your password: {final}")


print("Wellcome to the PyPassword Generator")
letters_number = int(input("How many letters would you like in your password? "))
symbols_number = int(input("How many symbols would you like in your password? "))
numbers_number = int(input("How many numbers would you like in your password? "))

shuffle(letters_number, symbols_number, numbers_number)


