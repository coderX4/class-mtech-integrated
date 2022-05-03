class A(object):
    def __new__(cls):
        print("new method creating instance")
        return super(A,cls).__new__(cls)

    def __init__(self):
        print("init method")
        self.n="Deep"
    def __str__(self):
        return self.n+" (Str function used)"
object=A()
print(object) #str function call

class ABC:
    '''Class  for __repr__ , __doc__ , __name__ , __bases__ , __dict__'''
    def __init__(self,v1,v2,st):
        self.v1=v1
        self.v2=v2
        self.st=st
    def __repr__(self):
        return self.st
    def display(self):
        print("Variable 1:",self.v1)
        print("Variable 2:",self.v2)
obj=ABC(10,30.34,"repr function",)
print(obj)  # repr function call
obj.display()
print("object.__doc__  :",obj.__doc__)
print("object.__dict__ :",obj.__dict__)
print("class.__name__ :",ABC.__name__)
print("class.__bases__ :",ABC.__bases__)


