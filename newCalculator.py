# calculator

a = int(input("Enter a number : "))
c = input("Enter the operation you want to perform : ")
b = int(input("Enter a second number : "))

if c == '+':
    result = a + b
    print("The answer is : " + str(result))
elif c == '-':
    result = a - b
    print("The answer is : " + str(result))
elif c == '*':
    result = a * b
    print("The answer is : " + str(result))
else:
    result = a / b
    print("The answer is : " + str(result))
