'''
import tkinter as tk

win=tk.Tk()
win.title("Python GUI App")
Lbl=tk.Label(win, text="Button Not Click!")
Lbl.pack()

def click():

    Lbl.configure(foreground="red")
    Lbl.configure(text="Button Clicked!")

'''

import tkinter as tk
from tkinter import *

window=tk.Tk()
window.title("First GUI in Python!")
l1=tk.Label(text="Hello Python!",
            fg="cyan",
            bg="black",
            width=30,
            height=30
            )

window.geometry('500x500')

'''
btn=Button(window, text="Click Me to see the magic ;)",
           command=window.destroy)
'''

btn=tk.Button(window, text="Click Me to see the magic ;)",
              command=window.destroy,
              fg="red",
              bg="cyan"
              )

def click():
    action.configure(text="Why Tho?")
    l1.configure(text="Button Clicked!")

action=tk.Button(window, text="Why Tho???", command=click,
                 fg="red",
                 bg="cyan"
                 )

action.pack()
btn.pack()
l1.pack()
window.mainloop()
