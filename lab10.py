class Numbers:
	my_list=0
	def __init__(self):
		self.my_list=[]
		self.ch='y'
	def insert(self):
		self.ch='y'
		while self.ch=='y':
			n=input("Enter the element :")
			self.my_list.append(n)
			self.ch=(input("Enter y to add element or n to display largest element: "))
		print(self.my_list)
	def find_max(self):
		max=''
		for i in self.my_list:
			if i > max:
				max=i
		print("Largest element:",max)
ob=Numbers()
ob.insert()
ob.find_max()
