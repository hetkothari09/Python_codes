import os

path="C:\\Users\\vasudevay\\Documents\\python.txt"

if os.path.exists(path):
    print("That location exits!")
    if os.path.isfile(path):
        print("That is a File!")
    elif os.path.isdir(path):
        print("That is a directory!")
    else:
        print("That is not a File!")
else:
    print("That location doesn't exits!")

