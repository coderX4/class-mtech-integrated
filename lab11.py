class point:
    def __init__(s):
        s.x1 = int(input("Enter the x1 coordinate: "))
        s.y1 = int(input("Enter the y1 coordinate: "))
        s.x2 = int(input("Enter the x2 coordinate: "))
        s.y2 = int(input("Enter the y2 coordinate: "))
    def midpoint(s):
        x = (s.x1 + s.x2) / 2
        y = (s.y1 + s.y2) / 2
        p = (x,y)
        print("Mid point of two lines:",p)
    def length(s):
        d = (((s.x2 - s.x1)**2 + ((s.y2 -s.y1)**2))) ** 0.5
        print("Distance of two lines:",d)
obj = point()
obj.midpoint()
obj.length()