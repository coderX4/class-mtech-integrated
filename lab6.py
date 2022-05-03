1class Employee:
    emp = 0
    my_list = []

    def __init__(self):
        self.n = ""
        self.d = ""
        self.s = 0

    def getdata(self):
        self.n = input("Enter the name of employee :")
        self.d = input("Enter the designation :")
        self.s = int(input("Enter the salary :"))
        Employee.my_list.append(self.s)

    def average():
        print("Number of employee:", len(Employee.my_list))
        print(sum(Employee.my_list) / len(Employee.my_list))

    def display(self):
        print("Name:", self.n)
        print("Designation:", self.d)
        print("Salary:", self.s)


my_data = []
ch = 1
while ch == 1:
    print('''1.Add  new Employee
2.Display Info
3.Display average salary
    ''')
    choice = int(input("Enter your choice:"))
    obj = Employee()
    if choice == 1:
        obj.getdata()
        my_data.append(obj)
    elif choice == 2:
        for i in my_data:
            print("Info of employee")
            i.display()
            print(" ")
    elif choice == 3:
        Employee.average()
    else:
        print("Wrong choice.")
    print("")
    ch = int(input("Want to continue  \n"))

print("All set.")




