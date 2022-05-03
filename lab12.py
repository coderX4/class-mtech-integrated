class Complex:
    my_list=[]
    def __init__(self):
        self.x = 0
        self.y = 0
        self.c = 0
    def read(self):
        self.x = int(input("Enter the real part: "))
        self.y = int(input("Enter the imaginary part: "))
        self.c = complex(self.x, self.y)
        Complex.my_list.append(self.c)
    def add():
        d = sum(Complex.my_list)
        return d
    def subtract():
        e= Complex.my_list[0] - Complex.my_list[1]
        return e
    def display():
        print("Addition :",Complex.add())
        print("Subtraction :",Complex.subtract())
ch='y'
print("Chose a function.")
while ch == 'y':
    choice = int(input("1. Enter the number. \n"
          "2. Add the number. \n"
          "3. Subtract the number. \n"
          "4. Display the data. \n"))
    if choice == 1:
        obj=Complex()
        obj.read()
    elif choice == 2:
        print(Complex.add())
    elif choice == 3:
        print(Complex.subtract())
    elif choice == 4:
        Complex.display()
    else:
        print("Wrong choice.")
        print("\n")
    ch = input("Enter y to Continue or n to kill. ")
    print("\n")




