# def greating(text):
#
#     if int(text) == 1:
#         print("You typed: 1")
#     elif int(text) == 2:
#         print("You typed: 2")
#     else:
#         print("You need to type 1 or 2")
#
# Text = ""
# while Text != quit:
#     Text = input("Please type some text: ")
#     greating(Text)

#Function with more that 1 input

def great_with(name, location):
    #name = name
    #location = location
    print(f"Hello {name}, your location is {location}")

great_with( location = "North Olmsted", name ="Azamat")