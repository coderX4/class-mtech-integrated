from math import gcd
class Fraction:
	numerator=0
	denominator=0
	def __init__(self):
		self.n=0
		self.d=0
	def getdata(self):
		self.n=int(input("Enter the numerator :"))
		self.d=int(input("Enter the denominator :"))
		print("Numerator / Denominator = {} / {}".format(self.n,self.d))
	def show(self):
		a = gcd(self.n,self.d)
		self.n//=a
		self.d//=a
		print("Numerator / Denominator = {} / {}".format(self.n,self.d))

ob = Fraction()
ob.getdata()
ob.show()
