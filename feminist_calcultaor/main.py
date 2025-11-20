import tkinter as tk
from tkinter import *
import math
import os
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#e9e4b0"

BUTTON_COLOR = "#F7CAC9"
FONT_NAME = "Courier"
windows = Tk()
windows.title("Feminist Calculator")
windows.config(padx = 200, pady = 200, bg = "#E4AFAF")
windows.minsize(width=600, height=600)
title_label = Label(text = "I am not feminist", fg = GREEN, bg = "#E4AFAF", font = (FONT_NAME, 40))
title_label.grid(row=0, column=1)
canvas = Canvas(width = 600, height = 600, bg = "#E4AFAF", highlightthickness=0)
create_image = PhotoImage(file = os.path.join(os.path.dirname(__file__), "feminism.png"))
canvas.create_image(300, 300, image=create_image)


canvas.grid(row=1, column=1)
#create_image = PhotoImage(file = "feminism.png")
#canvas.create_image(100, 112, image=create_image)





windows.mainloop()


