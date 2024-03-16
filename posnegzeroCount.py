list = []
a = int(input("Enter the number of elements you want to insert:"))
for i in range(0, a):
    k = int(input("Enter the elements:"))
    list.append(k)


def expanding(l):
    diff = 0
    length = len(l)
    a = b = 0
    exp = []
    flag = 0

    for i in range(0, length-1):
        a = l[i]
        b = l[i + 1]
        diff = abs(a - b)
        exp.append(diff)

    length1 = len(exp)

    for i in range(0, length1-1):
        if a[i]<a[i+1]:
            flag==1
        else:
            flag==0

    if flag==1:
        print("True")
    elif flag==0:
        print("False")


print(expanding(list))
