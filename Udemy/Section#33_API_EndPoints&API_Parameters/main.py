from tkinter import*

from django.utils.termcolors import background

window = Tk()
window.title("Привет Азамат")
window.config(padx=175, pady=75)

canvas = Canvas(width=300, height=300)
background_img = PhotoImage(file="phi.png")
canvas.create_image(100,100, image=background_img)
canvas.grid(row=0, column=0)

window.mainloop()