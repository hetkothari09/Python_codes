
a = int(input("Enter a number: "))
c = input("Enter the operation you want to perform: ")
b = int(input("Enter second number: "))

if c == '+':
    result = a + b
    print("The addition of two numbers is : ", result)

elif c == '-':
    result = a - b
    print("The subtraction of two number is : ", result)

elif c == '*':
    result = a * b
    print("The multiplication of two numbers is : ", result)

elif c == '/':
    result = a / b
    print("The division of the two numbers is : ", result)

else:
    print("Invalid Operation!")


