from tkinter import * 
from tkinter import messagebox
import random

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return
    with open("password manager/data.txt", "a") as data_file:
        data_file.write(f"{website} / {email} / {password}\n")
    website_entry.delete(0, END)
    password_entry.delete(0, END)

def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = "0123456789"
    symbols = '!#$%&()*+'
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)



window = Tk()
window.minsize(width = 400, height = 300)
window.title("Password Manager")
window.config(padx=20, pady=20)
window.configure(bg="white")

logo_img = PhotoImage(file = "C:\\Users\\USER\\Python-demo-1\\password manager\\logo.png")
canvas = Canvas(width=200, height=200,bg = "white", highlightthickness=0)
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 1, column = 1)

website_label = Label(text= "Website:", bg = "white")
website_label.grid(row=2, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=2, column=1, columnspan=2)

email_label = Label(text = "Email :", bg = "white")
email_label.grid(row=3, column=0)
email_entry = Entry(width=35)
email_entry.grid(row= 3, column = 1 , columnspan=2)
email_entry.insert(0, "myshaafrinjeba916@gmail.com")

password_label = Label(text= "Password:", bg = "white")
password_label.grid(row=4,column=0)
password_entry = Entry(width = 21)
password_entry.grid(row=4, column= 1, columnspan=1)

generate_pass_button = Button(text= "Generate Password", bg = "blue", fg = "black", command = generate_password)
generate_pass_button.grid(row=4, column=2)

add_button = Button(text= "Add", width=36, bg = "blue", fg = "black", command = save_password)
add_button.grid(row=5, column=1, columnspan =2)

window.mainloop()