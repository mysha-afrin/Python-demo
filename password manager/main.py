from tkinter import *
from tkinter import messagebox

import pyperclip
import json







#------------------------------UI Setup------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = "password manager\logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)





window.mainloop()