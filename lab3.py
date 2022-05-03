class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        A=self.length*self.width
        print("Arae of rectangle:",A)
dimension=Rectangle(20,40)
dimension.area()
dimension1=Rectangle(3,6)
dimension1.area()