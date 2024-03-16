class Demo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __del__(self):
        print("Object Destroyed!")

d1=Demo(2, 1)
d2=Demo(4, 5)
