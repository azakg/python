import sys
import checking
import saving

loop1 = True
list_of_accounts = []
while loop1:
    question1 = input("What you want to do?\n Open account, type A. \n Search account, type S. \nQuit, type Q. \n")

    if question1 == 'A':
        question2 = input("What type of bank account you want to open? \n If Checking type C \n If Savings type S")
            if question2 == 'C' or question2 == 'c':
                name = input("Type your name: \n")
                f_name = input("Type your family name: \n")
                amount = input("Type how much you want ot put money: \n")
                list_of_accounts.append(checking.Checking(name, f_name, amount))

            else:
                name = input("Type your name: \n")
                f_name = input("Type your family name: \n")
                amount = input("Type how much you want ot put money: \n")
                list_of_accounts.append(saving.Saving(name, f_name, amount))

    elif question1 == 'S':
        s_name = input("Type the name of the user")
        for list1 in list_of_accounts:
            if s_name == list1

    elif  question1 == 'Q':
        sys.exit()