def Bmi(height, weight):
    bmi = weight/(height**2)
    return bmi
height = 1.79832
weight = 70

bmi = Bmi(height, weight)

print("The BMI is : ", bmi)

if(bmi < 18.5):
    print("You are underweight!")
elif (bmi>=18.5 and bmi<24.9):
    print("You are HealthY!")
elif (bmi>=24.9 and bmi<30):
    print("You are overweight!")
elif(bmi>30):
    print("You are suffering from obesity!!")



