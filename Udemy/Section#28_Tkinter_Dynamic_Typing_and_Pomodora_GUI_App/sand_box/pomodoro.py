from tkinter import *
import math

YELLOW = "#f7f5dd"

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 112, text="00:00", fill="white", font=( "Courier", 35, "bold"))
canvas.pack()

window.mainloop()