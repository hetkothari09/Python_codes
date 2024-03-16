class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class student(person):
    def __init__(self, name, id, sem, marks1, marks2):
        super().__init__(name, id)
        self.name = name
        self.id = id
        self.sem = sem
        self.marks1 = marks1
        self.marks2 = marks2

    def avgmarks(self):
        avgerage = (self.marks1 + self.marks2) / 2
        print("Average Marks are:", avgerage)

    def getdata(self):
        print("Name of the student:", self.name)
        print("Id of the student:", self.id)
        print("Sem of the student:", self.sem)
        print("Marks1 of the student:", self.marks1)
        print("Marks2 of the student:", self.marks2)
        self.avgmarks()

    def __del__(self):
        print("Object deleted!")


s = []
print("Enter the number of students:")
n = int(input())

for i in range(0, n):
    name = input("Enter the name of the student:")
    id = int(input("Enter the id of the student:"))
    sem = input("Enter the sem of the student:")
    marks1 = int(input("Enter the marks1 of the student:"))
    marks2 = int(input("Enter the marks2 of the student:"))

    s.append(student(name, id, sem, marks1, marks2))

for stud in s:
    stud.getdata()
