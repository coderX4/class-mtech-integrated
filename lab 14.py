class Bank_account:
    def __init__(self):
        self.b=0
        self.ac=input("Enter the Account number: ")
    def deposit(self):
        am=int(input("Enter amount to deposit: "))
        self.b+=am
        print("Balance after deposit:",self.b)
        return self.b
    def withdraw(self):
        am=int(input("Enter amount to withdarw: "))
        if am > self.b:
            print("Insufficiant balance")
        else:
            self.b-=am
        print("Balance after withdraw:", self.b)
        return self.b
    def get_balance(self):
        print("Balance :",self.b)
bal = Bank_account()
bal.deposit()
bal.withdraw()
bal.get_balance()
