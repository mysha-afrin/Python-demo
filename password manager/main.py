from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

#------------------------------Password Generator ---------------------#
def generate_password():
    letters = 'abcdefghijklmnopqrstwuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    return "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
#------------------------------Save Password --------------------------#

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }




#------------------------------UI Setup------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = "password manager\logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)

website = Label(text = "Website:")
website.grid(row = 1, column= 0)



website_entry = Entry(width = 30)
website_entry.grid(row = 1, column = 1, columnspan=1)

email = Label(text = "Email/Username:")
email.grid(row = 2, column = 0)

email_entry = Entry(width = 35)
email_entry.grid(row = 2, column= 1, columnspan=2)

password = Label(text = "Password:")
password.grid(row = 3, column= 0)

password_entry = Entry(width = 21)
password_entry.grid(row = 3, column = 1)

generate_password_button = Button(text = "Generate password", width = 14, command=generate_password)
generate_password_button.grid(row = 3, column = 2)

add_button = Button(text = "Add", width = 36)
add_button.grid(row = 4, column = 1, columnspan=2)

search_button = Button(text =" Search", width = 14)
search_button.grid(row = 1, column = 2)

window.mainloop()