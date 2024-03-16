def addition(num1, num2):
    num1+=num2
    return num1

def subtraction(num1, num2):
    num1-=num2
    return num1

def multiplication(num1, num2):
    num1*=num2
    return num1

def division(num1, num2):
    num1/=num2
    return num1

def module(num1, num2):
    num1%=num2
    return num1


print("""You can perform operations such as:
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      5. Module """
      )

choice = int(input("Enter your choice of operation:"))
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

switcher={
    1: addition(num1, num2),
    2: subtraction(num1, num2),
    3: multiplication(num1, num2),
    4: division(num1, num2),
    5: module(num1, num2)
}

def switch(operation, num1, num2):
    return switcher.get(operation, (num1, num2))

print(switch(choice, num1, num2))
