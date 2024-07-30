import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order):
    menu = 'a'
    # Assign order name to menu variable
    if order == 'e':
        menu = 'espresso'
    elif order == 'l':
        menu = 'latte'
    elif order == 'c':
        menu = 'cappuccino'

# Check just "Espresso"
    if menu == "espresso":
        if MENU[menu]['ingredients']['water'] > resources['water']:
            return "water"
        elif MENU[menu]['ingredients']['coffee'] > resources['coffee']:
            return "coffee"
        else:
            return "ok"
# Check 'latte' and 'cappuccino'
    else:
        if MENU[menu]['ingredients']['water'] > resources['water']:
            return "water"
        elif MENU[menu]['ingredients']['milk'] > resources['milk']:
            return "milk"
        elif MENU[menu]['ingredients']['coffee'] > resources['coffee']:
            return "coffee"
        else:
            return "ok"


def decrease_resource(order_type):
    # Espresso
    if order_type == 'e':
        # Water
        num1 = resources['water']
        num2 = MENU['espresso']['ingredients']['water']
        num3 = num1 - num2
        resources['water'] = num3
        # Coffee
        num3 = resources['coffee']
        num4 = MENU['espresso']['ingredients']['coffee']
        num5 = num3 - num4
        resources['coffee'] = num5
    # Latte
    elif order_type == 'l':
        # Water
        num1 = resources['water']
        num2 = MENU['latte']['ingredients']['water']
        num3 = num1 - num2
        resources['water'] = num3
        # Milk
        num1 = resources['milk']
        num2 = MENU['latte']['ingredients']['milk']
        num3 = num1 - num2
        resources['milk'] = num3
        # Coffee
        num3 = resources['coffee']
        num4 = MENU['latte']['ingredients']['coffee']
        num5 = num3 - num4
        resources['coffee'] = num5
    elif order_type == 'c':
        num1 = resources['water']
        num2 = MENU['cappuccino']['ingredients']['water']
        num3 = num1 - num2
        resources['water'] = num3
        # Milk
        num1 = resources['milk']
        num2 = MENU['cappuccino']['ingredients']['milk']
        num3 = num1 - num2
        resources['milk'] = num3
        # Coffee
        num3 = resources['coffee']
        num4 = MENU['cappuccino']['ingredients']['coffee']
        num5 = num3 - num4
        resources['coffee'] = num5


def print_order(order):
    # Decrease resources
    if order == 'e':
        decrease_resource(order)
        print("There your espresso ☕️. Enjoy!")
    elif order == 'l':
        decrease_resource(order)
        print("There your latte ☕️. Enjoy!")
    elif order == 'c':
        decrease_resource(order)
        print("There your cappuccino ☕️. Enjoy!")



def payment(order):

    price = 0
    total_get = 0
    refund = 0
    if order == 'e':
        price = MENU['espresso']['cost']
    elif order == 'l':
        price = MENU['latte']['cost']
    elif order == 'c':
        price = MENU['cappuccino']['cost']

    print("Please insert coins")

    while True:
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many pennies?: "))
        total_get = (quarters * 0.25) + (dimes * 0.10)+(nickles * 0.05) + (pennies * 0.01)
        if total_get > price:
            print(f"Here is your ${round((total_get - price), 2)} in change.")
            break
        elif total_get == price:
            break
        elif total_get < price:
            print(f"Not enough money. Here's money back {total_get}")





def initial():

    while True:
        order = input("What would you like? (espresso/latte/cappuccino), Type 'e', 'l', 'c': ")
        if order == 'off':
            break
        elif order == 'report':
            for key, volume in resources.items():
                print(f"{key.title()}: {volume}ml")
        elif order in ['e', 'l', 'c']:
            check_result = check_resources(order)
            if check_result == 'ok':
                payment(order)
                print_order(order)
            else:
                print(f"Sorry there is not enough {check_result}")
        else:
            print("Type 'e' or 'l' or 'c'")





initial()