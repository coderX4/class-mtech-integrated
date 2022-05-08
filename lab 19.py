class Student:
    def __init__(self):
        self.name = input("Enter the name of student: ")
        self.age = int(input("Enter the age : "))
    def display1(self):
        print("Name of student :",self.name)
        print("Age of student :",self.age)
class Marks(Student):
    def __init__(self):
        super().__init__()
        self.m1 = int(input("Enter marks in maths : "))
        self.m2 = int(input("Enter marks in physics : "))
        self.m3 = int(input("Enter marks in python : "))
    def display2(self):
        Student.display1(self)
        print("Marks in maths: ",self.m1)
        print("Marks in physics :", self.m2)
        print("Marks in python :", self.m3)
class Result(Marks):
    def __init__(self):
        super().__init__()
        self.total = 0
    def display3(self):
        self.total = self.m1 + self.m2 + self.m3
        Marks.display2(self)
        print("Total of marks in 3 subjects :",self.total)
obj=Result()
obj.display3()


