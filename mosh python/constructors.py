# constructor is a function that gets called at the time of creating an object
# __intit__ is initialized, construct or create an object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)
print(point.y)