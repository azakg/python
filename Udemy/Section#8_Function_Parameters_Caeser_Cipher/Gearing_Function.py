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

# def great_with(name, location):
#     #name = name
#     #location = location
#     print(f"Hello {name}, your location is {location}")
#
# great_with( location = "North Olmsted", name ="Azamat")

def calculate_love_score(name1, name2):
    name3 = name1.lower() + name2.lower()
    t = name3.count("t")
    r = name3.count("r")
    u = name3.count("u")
    e = name3.count("e")

    l = name3.count("l")
    o = name3.count("o")
    v = name3.count("v")
    e2 = name3.count("e")

    print(int(str(t + r + u + e) + str(l + o + v + e2)))

calculate_love_score("Kanye West", "Kim Kardashian")

