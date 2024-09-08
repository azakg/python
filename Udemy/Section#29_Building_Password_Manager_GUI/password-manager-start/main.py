import string
from tkinter import *
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    #symbol = ''.join(random.choices(string.ascii_letters, k=7))
    # return symbol
    password_entry.insert(0, ''.join(random.choices(string.ascii_letters, k=7)))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_entry():
    with open("data.txt", "a") as file:
        file.write(f"\n{website_entry.get()} | {email_entry.get()} | {password_entry.get()} ")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
#canvas.pack()

#__________________________________Lables_____________________________#

website = Label(text="Website:")
website.grid(column=0, row=1)

email_userName = Label(text="Email/Username:")
email_userName.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

#_____________________________Entry__________________________________#

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "azakgzuu@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#_____________________________Buttom__________________________________#

generate_password_button = Button(text="Generate Password", command=generator)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=get_entry)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()