class SEPIA:
    def __init__(self,name,var):
        self.name = name
        self.var = var
    def show(self):
        print("Name :",self.name)
        print("Attribute is :",self.var)
obj = SEPIA("KIA",200)
obj.show()
print("Check if object has variable or not..",hasattr(obj,'name'))
getattr(obj,'name')
setattr(obj,'name',"SUV")
setattr(obj,'var', 500)
print("After setting the values....",)
obj.show()
delattr(obj,'name')
obj.show()
