# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(*args):
   sum = 0
   for i in args:
       sum += i
   return sum

def addnew(*something):
    sum = 0
    something = list(something)
    something[0] = 0
    for i in something:
        sum += i
    return sum

print(add(1, 2, 4, 5, 6))