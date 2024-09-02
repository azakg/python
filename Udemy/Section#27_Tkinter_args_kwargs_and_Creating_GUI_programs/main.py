from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

#Lable
my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text2")

#Button

def buttion_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=buttion_clicked)
button.pack()



#Entry

input = Entry(width=10)
input.pack()



window.mainloop()