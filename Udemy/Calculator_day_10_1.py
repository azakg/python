# Calculator

operations = {
    "+": "add",
    "-": "sub",
    "*": "mul",
    "/": "dev"
}


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def dev(n1, n2):
    return n1 / n2


num1 = int(input("What is the first number: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("What operation do you want?: ")

num2 = int(input("What is the second number: "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("What operation do you want?: ")
num3 = int(input("What is the next number?: "))

calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(num1, num2), num3)
