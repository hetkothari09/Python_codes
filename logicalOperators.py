# logical operators : AND OR

temp = int(input("What is the temperature outside ? : "))


# NOT OPERATOR REVERSES THE STATEMENT i.e TRUE TO FALSE AND VICE VERSA


# if not(temp >= 0 and temp <= 30):
#    print("The temperature is good today!")
#    print("Go outside!")

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")

elif temp < 0 or temp > 30:
    print("The temperature is Bad today!")
    print("Stay Inside!")
