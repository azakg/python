def greating(text):

    if int(text) == 1:
        print("You typed: 1")
    elif int(text) == 2:
        print("You typed: 2")
    else:
        print("You need to type 1 or 2")

Text = ""
while Text != quit:
    Text = input("Please type some text: ")
    greating(Text)