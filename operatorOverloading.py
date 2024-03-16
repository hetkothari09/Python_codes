class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, o):
        return self.a + o.a

obj1=A(3)
obj2=A(4)
obj3=A("Python")
obj4=A("Programming")

print(obj1+obj2)
print(obj3+obj4)