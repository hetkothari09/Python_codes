import tkinter
from tkinter import *
from tkinter import ttk

root=Tk()
r=IntVar()
root.geometry("450x450")
list1=["one", "two", "three"]
l = ttk.Combobox(root, values=list1).place(x=50,y=35)
l1=Listbox(root, width=35)
l1.insert(1, "het")
l1.insert(2, "hett")
l1.insert(3, "hetty")
l1.place(x=160, y=140)
r1=Radiobutton(root, text="het", value=1, variable=r).place(x=35, y=80)
r2=Radiobutton(root, text="hettt", value=2, variable=r).place(x=135, y=80)


root.mainloop()