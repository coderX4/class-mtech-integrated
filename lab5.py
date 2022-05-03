class students:
    def __init__(s,name,marks):
        s.name=name
        s.marks=marks
        s.d=0
    def compute(s):
        print(s.marks)
        for i in range(len(s.marks)):
            s.d = s.d + s.marks[i]
        s.e=s.d/3
        return s.e
    def display(s):
        print("Students Information")
        print("Name:",s.name)
        print("Total marks:",s.d)
        print("Average marks:",s.e)
name=input("Enter the name of student: ")
n=int(input("Enter the marks in maths: "))
m=int(input("Enter the marks in english: "))
o=int(input("Enter the marks in science: "))
marks=[n,m,o]
obj=students(name,marks)
obj.compute()
obj.display()
