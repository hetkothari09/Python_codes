from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("450x450")
r=IntVar()
Radiobutton(root, text="male", value=1, variable=r).place(x=50, y=20)
Radiobutton(root, text="female", value=2, variable=r).place(x=150, y=20)
r1 = Checkbutton(root, text="Cricket").place(x=50, y=40)
r2 = Checkbutton(root, text="Tennis").place(x=150, y=40)

vlist = ["one", "two", "three", "four"]
Combo = ttk.Combobox(root, values=vlist).place(x=50, y=75)

l = Listbox(root, height=5)
l2 = Listbox(root, height=10)

vlist2=["het","het2","het3"]
combo2=ttk.Combobox(root,values=vlist2).place(x=50, y=95)

l.insert(1, "one")
l.insert(2, "two")
l.insert(3, "three")
l.insert(4, "four")
l.place(x=220, y=75)

root.mainloop()
