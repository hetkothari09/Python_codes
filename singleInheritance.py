class Parent:
    def func1(self):
        print("This is a function of the parent class!")

class Child(Parent):
    def func2(self):
        print("This is a function in child class!")

obj1=Child()
obj1.func1()
obj1.func2()

