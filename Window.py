from Components import Button, Combobox, Display
import tkinter as tk
from tkinter import font

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Visualizador de fuentes Tkinter")
        self.resizable(0, 0)
        self.eval('tk::PlaceWindow . center')
        self.grid_columnconfigure(0, weight = 1)
        self.config(padx = 10, pady = 10, bg = "gray10")

        self.display = Display(self)
        self.btn_prev = Button(self, text = "Anterior")     
        self.btn_next = Button(self, text = "Siguiente") 
        self.combobox = Combobox(self, values = list(font.families()))  
        self.combobox.set(self.combobox["values"][0])

        self.print_components()

    def change_font(self):
        font = self.combobox.get()
        self.display.config(font = (font, 18))

    def go_prev(self):
        font_index = self.combobox.current()
        self.combobox.set(self.combobox["values"][font_index - 1])
        self.change_font()


    def go_next(self):
        font_index = self.combobox.current()
        if self.combobox.current() < len(self.combobox["values"]) - 1:
            self.combobox.set(self.combobox["values"][font_index + 1])
        else:
            self.combobox.set(self.combobox["values"][0])
        self.change_font()


    def print_components(self):
        self.display.grid(column = 2, row = 1, sticky = "esnw", ipady = 10, ipadx = 10)
        self.combobox.grid(column = 2, row = 0, sticky = "ew")
        self.btn_prev.grid(column = 0, row = 0, sticky = "w", pady = 10)
        self.btn_next.grid(column = 1, row = 0, sticky = "e", pady = 10, padx = 10)