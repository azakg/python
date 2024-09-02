from tkinter import *

def convert():
    result_lable.config(text=int(input.get())*1.6)

window = Tk()
window.title("Converter Mi/Km")
window.config(width=300, height=150)
window.config(padx=20, pady=20)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=1)

#Lables
input_lable = Label(text="Miles", font=("Arial", 16, "bold"))
input_lable.grid(column=2, row=1)

output_lable = Label(text="Km", font=("Arial", 16, "bold"))
output_lable.grid(column=2, row=2)

result_lable = Label(text="####", font=("Arial", 16, "bold"))
result_lable.grid(column=1, row=2)

#Button
button = Button(text="Click me", command=convert)
button.grid(column=1, row=3)


window.mainloop()