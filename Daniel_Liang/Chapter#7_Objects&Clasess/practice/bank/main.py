from checking import Checking
from savings import Savings
customers_list = []

go_on = True
while go_on:
    open_account = input("Would you like open account: \n")
    if open_account.title() == "Yes":
        name = input("Type your name: \n")
        family_name = input("Type your family name: \n")
        account_type = input("Which type of account you want to open checking or saving C/S: \n")
        if account_type.title() == "C":
            amount = int(input("Type amount of money: \n"))
            customers_list.append(Checking(name, family_name, account_type, amount ))
        elif account_type.title() == "S":
            amount = int(input("Type amount of money: \n"))
            customers_list.append(Savings(name, family_name, account_type, amount))
    elif open_account == "No":
        go_on = False


request_name = input("Type search name: \n")

for n in customers_list:
    if n.name == request_name:
        print(n.name)