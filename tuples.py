# tuple/class  = collection which is ordered and unchangeable
#                used to group together related data

student = ("Het", 17, "male")

print(student.count("Het"))
print(student.index("male"))
print()

for x in student:
    print(x)

print()
if "Het" in student:
    print("Het is here!")
