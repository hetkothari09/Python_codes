from tkinter import *
import tkinter.messagebox

def submitact():
    if username.get=="HetKothari" and password.get=="bhaibhai":
        tkinter.messagebox.showinfo(title="Welcome", text="Hello, You have logged in successfully"+username.get+" .")
    else:
        tkinter.messagebox.showinfo(title="",text="Invalid Credentials!")

root=Tk()
root.title=("Python Exam")
root.geometry("300x450")
     
l1=Label(text="Enter Username:",)
l1.place(x=23,y=45)
username=Entry(root, width=30)
username.place(x=150,y=40)
l2=Label(text="Enter pass:")
l2.place(x=23,y=45)
password=Entry(root,width=30)
password.place(x=150,y=50)
submitbtn=Button(root,text="Login",bg="cyan",command=submitact)
submitbtn.place(x=100,y=200,width=50)
root.mainloop()
