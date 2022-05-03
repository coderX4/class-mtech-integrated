class Circle:
    PI = 3.14
    @classmethod
    def area(cls,r):
        return (cls.PI *r*r)
    @classmethod
    def circum(cls,r):
        return (2*cls.PI*r)
    @staticmethod
    def display():
        print("Area of circle:",Circle.area(20))
        print("Circumference of circle:",Circle.circum(20))
Circle.display()