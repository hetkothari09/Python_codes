class Father:
    fathername = ""

    def father(self):
        self.fathername

class Mother:
    mothername=""

    def mother(self):
        self.mothername

class Child(Father, Mother):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother name is :", self.mothername)

child1=Child()
child1.fathername= "Baap"
child1.mothername= "Maa"
child1.parents()
