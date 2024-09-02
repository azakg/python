from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Lable", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click me", command = button_clicked)
#button.pack()
button.grid(column=1, row=1)

button2 = Button(text="Click me", command = button_clicked)
button2.grid(column=2, row=0)

#Entry

input = Entry(width=10)
print(input.get())
#input.pack()
input.grid(column=3, row=2)

window.mainloop()