# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Kothari"

def display_name():
    name = "Het"            # local scope bcz declared inside function
    print(name)

display_name()
print(name)