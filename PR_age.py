age = int(input("Enter your age:"))

if age<=0:
    print("Enter a Valid Age!")
elif age>=1 and age<=6:
    print("Infant!")
elif age>=7 and age<=13:
    print("Child!")
elif age>=14 and age<=18:
    print("Teenager!!")
else:
    print("You are a grown up or an ADULT!")