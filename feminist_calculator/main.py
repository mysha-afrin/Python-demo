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
windows.minsize(width=700, height=600)
title_label = Label(text = "Faminist", fg = GREEN, bg = "#E4AFAF", font = (FONT_NAME, 50))
title_label.grid(row=0, column=1)
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)

create_image = PhotoImage(file = "feminist_calculator/feminism.png")
canvas.create_image(100, 112, image=create_image)
class FeministCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Feminist Calculator")

        self.total = 0
        self.entered_number = 0

        self.label = Label(master, text="Feminist Calculator", font=("Helvetica", 16))
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.add_button = Button(master, text="+", command=self.add)
        self.add_button.pack()

        self.subtract_button = Button(master, text="-", command=self.subtract)
        self.subtract_button.pack()

        self.multiply_button = Button(master, text="*", command=self.multiply)
        self.multiply_button.pack()

        self.divide_button = Button(master, text="/", command=self.divide)
        self.divide_button.pack()

        self.result_label = Label(master, text="Result: 0")
        self.result_label.pack()

    def add(self):
        self.entered_number = float(self.entry.get())
        self.total += self.entered_number
        self.update_result()

    def subtract(self):
        self.entered_number = float(self.entry.get())
        self.total -= self.entered_number
        self.update_result()

    def multiply(self):
        self.entered_number = float(self.entry.get())
        self.total *= self.entered_number
        self.update_result()

    def divide(self):
        self.entered_number = float(self.entry.get())
        if self.entered_number != 0:
            self.total /= self.entered_number
            self.update_result()
        else:
            self.result_label.config(text="Error: Division by zero")

    def update_result(self):
        self.result_label.config(text=f"Result: {self.total}")








windows.mainloop()


