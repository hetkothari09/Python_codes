
fos = float(input("Enter marks for fos:"))
mbs = float(input("Enter marks for mbs:"))
dbms = float(input("Enter marks for dbms:"))
python = float(input("Enter marks for python:"))
cg = float(input("Enter marks for cg:"))

total = fos + mbs + dbms + python + cg
percent = (total/500) * 100

print("Total Marks = ", total)
print("Percentage = ", percent, "%")

if (percent>=90):
    print("First Class!!!")
elif (percent>=70 and percent<90):
    print("Distinction!")
elif (percent>=35 and percent<70):
    print("Pass!")
else:
    print("FAIL!")
