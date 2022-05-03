class employee:
    def __init__(self, a, name, eid):
        self.n = name
        self.e = eid
        self.a = a

    def show(self):
        print("Employee number",self.a)
        print("Name: ", self.n)
        print("E-mail: ", self.e)


class empl(employee):

    def __init__(self, a, name, eid, salary):
        employee.__init__(self, a, name, eid)
        self.s = salary

    def show(self):
        employee.show(self)
        print("Salary: ", self.s)

ob1 = empl(1,"Tushar", "Tushar@gmail.com", 200000)
ob1.show()
ob2 = empl(2,"Deep", "deep@gmail.com", 2045670)
ob2.show()
ob3 = empl(3,"Rishita", "rishita@gmail.com", 400000)
ob3.show()
ob4 = empl(4,"Adii", "adii@gmail.com", 200000)
ob4.show()
ob5 = empl(5,"Saurabh", "saurabh@gmail.com", 200000)
ob5.show()
