import tkinter.messagebox
from tkinter import *

def submitact():
    if username.get() == "HetKothari" and password.get() == "bhaibhai":
        tkinter.messagebox.showinfo(title="Welcome", message="Login Successful, welcome "+username.get()+" .")
    else:
        tkinter.messagebox.showinfo(title=None, message="Invalid Credentials ")

root = Tk()
root.title("PT2 Python")
root.geometry("450x300")
l1= Label(text="Enter Username: ", )
l1.place(x=50, y=20)
username = Entry(root, width=35)
username.place(x=150, y=20)
l2 = Label(text="Enter password: ")
l2.place(x=50, y=50)
password = Entry(root, width=35, show="*")
password.place(x=150, y=50)
submitButton = Button(root, text="login", bg="cyan", command=submitact)
submitButton.place(x=150, y=100, width=55)
root.mainloop()
