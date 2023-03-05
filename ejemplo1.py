# hola_mundo.py

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame = ttk.Frame(root).grid()
ttk.Button(frame, text="Ver",
           command=lambda: print("Hola mundo!")).grid()
root.mainloop()
