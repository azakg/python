from pathlib import Path
# wish = input("What you want to do? read/write file? ")
#
# if wish == "r":
#     file = open("my_file.txt", "r")
#     print(file.read())
# elif wish == "w":
#     text = input("What you want to write?: \n")
#     file = open("my_file.txt", "w")
#     file.write(text)
# elif wish == "a":
#     text = input("What you would like to add to the file?: \n")
#     file = open("my_file.txt", "a")
#     file.write(f"\n{text}")


# Other Method of reading writing files
game_is_on = True

while game_is_on:
    wish = input("What you want?")
    if wish == "r":
        with open("my_file.txt", "r") as file:
            print(file.read())
    elif wish == "w":
        with open("my_file.txt", "w") as file:
            text = input("What you want write?")
            file.write(text)
    elif wish == "a":
        with open("my_file.txt", "a") as file:
            text = input("What you want append?")
            file.write(f"\n{text}")
    elif wish == "x":
        break
