"""
This is concept if the Exception

try:
    Something that might cause an exception
except:
    Dp this if there was an exception
else:
    Do this if there were no exceptions
finally:
    Dp this no matter what happens
"""

# #FileNotFoundError
# try:
#     with open("a_file.txt") as file:
#         file.read()
# except FileNotFoundError:
#     print("This file doesn't exist!")
#
#
# #KeyError
# a_dictionary = {"key": "value"}
# try:
#     value = a_dictionary["asdfasd"]
# except KeyError:
#     print("This key doesn't extst")
#
# #IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# try:
#     print(fruit_list[12])
# except IndexError:
#     print("Index out of range")
#
# #TypeError
# text = "abc"
# try:
#     print(text + "Hello")
# except TypeError:
#     print("This is Type error")
# else:
#     print("Every thing is ok")
#
# #_________________________________Example_________________________________________#
# print("#_________________________________Example_________________________________________#")
# try:
#     file = open("a_file.txt")
#     a_dictionary1 = {"key": "value"}
#     print(a_dictionary1["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)