class point:
    def __init__(s):
        s.x1 = int(input("Enter the x1 coordinate: "))
        s.y1 = int(input("Enter the y1 coordinate: "))
        s.x2 = int(input("Enter the x2 coordinate: "))
        s.y2 = int(input("Enter the y2 coordinate: "))
class Location(point):
    location = 0
    destination = 0
    def __init__(self):
        super().__init__()

    def midpoint(s):
        x = (s.x1 + s.x2) / 2
        y = (s.y1 + s.y2) / 2
        location = (x,y)
        print("Mid point of two lines:",location)
    def length(s):
        destination = (((s.x2 - s.x1)**2 + ((s.y2 -s.y1)**2))) ** 0.5
        print("Distance of two lines:",destination)
obj = Location()
obj.midpoint()
obj.length()