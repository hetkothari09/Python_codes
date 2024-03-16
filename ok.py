# list = []
#
# num = int(input("Enter the number of elements you want to insert in a list: "))
#
# for i in range(0, num):
#     k = int(input("Enter the element:"))
#     list.append(k)
#
#
# def expanding(l):
#     diff = 0
#     length = len(l)
#     a = b = 0
#     chk = []
#     flag = 0
#     for i in range(0, length - 1):
#         a = l[i]
#         b = l[i + 1]
#
#         diff = abs(a - b)
#         chk.append(diff)
#
#     length1 = len(chk)
#
#     for i in range(0, length1 - 1):
#         # check whether chk[i] < chk[i+1]
#         if chk[i]<chk[i + 1]:
#             flag = 1
#         else:
#             flag = 0
#
#     if flag == 1:
#         return True
#     else:
#         return False
#
#
# print(expanding(list))


list=[]
n=int(input("Enter the number of elements:"))

for i in range(0,n):
    k=int(input("enter the element : "))
    list.append(k)

def expanding(l):
    diff=0
    a=b=0
    chk=[]
    flag=0
    length=len(l)

    for i in range(0,length-1):
        a=l[i]
        b=l[i+1]

        diff=abs(a-b)
        chk.append(diff)
        length1=len(chk)

    for i in range(0, length1-1):
        if chk[i]<chk[i+1]:
            flag=1
        else:
            flag=0

    if flag==1:
        return True
    else:
        return False



print(expanding(list))