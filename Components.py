import tkinter as tk
from tkinter import ttk, font

class Button(tk.Button):
    def __init__(self, root, **kargs):
        super().__init__(root, **kargs,
                         bg = "orange",
                         borderwidth = 0,
                         padx = 4,
                         pady = 4,
                         cursor = "hand2")


class Combobox(ttk.Combobox):
    def __init__(self, root, **kargs):
        super().__init__(root, **kargs,
                         state = "readonly")


class Display(tk.Entry):
    def __init__(self, root, **kargs):
        super().__init__(root, **kargs,
                         font = ("System", 18),
                         width = 28)
        self.insert(0, "Texto de ejemplo 0123456789")