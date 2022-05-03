class Student:
    name = "Deep"
    def display(self):
        print(self.name)
        print("Variable accessed")
object=Student()
object.display()