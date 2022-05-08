class Distance:
    def __init__(self):
        self.km = int(input("Enter the kilometer distance : "))
        self.m = int(input("Enter the meter distance : "))

class School(Distance):
    def __init__(self):
        print("Distance of house of school......")
        super().__init__()
    def show(self):
        return (f'{self.km} km and {self.m} meter')
class Office(Distance):
    def __init__(self):
        print("Distance of house of office......")
        super().__init__()
    def show1(self):
        return (f'{self.km} km and {self.m} meter')
l ,l1 = [] ,[]
ch = 'y'
while ch == 'y':
    print(('''1.Add the distances.... 
2.To show distances....'''))
    opt = int(input("Enter your choice : "))
    if opt == 1:
        obj = School()
        obj1 = Office()
        l.append(obj)
        l1.append(obj1)
    if opt == 2:
        print("Distance of house to school....")
        a = 1
        b = 1
        for i in l:
            print(f'Route {a} distance = {i.show()}')
            a += 1
        print("Distance of house to office....")
        for j in l1:
            print(f'Route {b} distance = {j.show1()}')
            b += 1
ch = input("Enter y to continue : ")

