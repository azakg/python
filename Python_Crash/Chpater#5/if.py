cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#if not equal "!="
requested_topping = "mushrooms"
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#magic number
answer = 17
if answer !=42:
    print("That is not the correct answer. Please try again!")

#Checking Weather a Value is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'maria'
if user not in banned_users:
    print(f"\n{user.title()}, you can post a response if you wish")

######################################################################
print("######################################################################")
age = 17
if age >=18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you ate too young to vote.")
    print("Please register to vote as soon as you turn 18!")

######################################################################
#if-elif-else Chain
print("######################################################################")
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
