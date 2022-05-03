class Employee():
    name = "Saurabh"
    age = 20
    desig = "Programmer"

    def getdata(self):
        print(f"The name of employee is {Employee.name}"
              f" and his age is {Employee.age}"
              f" and his designation is {Employee.desig}")


class Manager(Employee):
    name = "Deep"
    age = 20
    desig = "Manager"

    def getdata1(self):

        print(f"The name of the manager is {Manager.name}"
              f" and his age is {Manager.age}"
              f" and his designation is {Manager.desig}")
        Employee.getdata(self)

class Team_leader(Employee):
    name = "Keshav"
    age = 20
    desig = "Project Head"

    def getdata2(self):
        print(f"The team leader name is {Team_leader.name}"
              f" and his age is {Team_leader.age}"
              f" and his designation is {Team_leader.desig}")
        Employee.getdata(self)

a1 = Manager()
a1.getdata1()
a2 = Team_leader()
a2.getdata2()