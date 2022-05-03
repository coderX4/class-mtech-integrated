class Numbers:
    MULTIPLIER = 30

    def __init__(s, x, y):
        s.x = x
        s.y = y

    def add(s):
        return (s.x + s.y)

    @classmethod
    def multiply(cls, a):
        return (cls.MULTIPLIER * a)

    @staticmethod
    def subtract(b, c):
        return (b - c)

    def value(s):
        s = (s.x, s.y)
        print(type(s))

        print("Tuple containing value of x and y:", s)


obj = Numbers(20, 50)
print("ADDition:", obj.add())
print("MUlTIPLICATION:", Numbers.multiply(30))
print("SUBTRACTION:", Numbers.subtract(40, 20))
obj.value()