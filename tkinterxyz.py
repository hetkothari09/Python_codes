import tkinter
from tkinter import *
import tkinter.messagebox

def submitact():
    if username.get()=="Het" and password.get()=="Kothari":
        tkinter.messagebox.showinfo(title="Login Successfull!", message="Welcome!")
    else:
        tkinter.messagebox.showinfo(title=None, message="Invalid Credentials!")

root=Tk()
root.geometry("450x300")
root.title("Tkinter@123")
l1=Label(text="Enter username:")
l1.place(x=50, y=30)
username= Entry(root, width=35)
username.place(x=150, y=20)
l2=Label(text="Enter password:")
l2.place(x=50, y=60)
password= Entry(root, width=35, show="*")
password.place(x=150, y=50)
submitbutton = Button(root, text="Submit", bg="cyan", command=submitact)
submitbutton.place(x=150, y=100, width=55)

root.mainloop()