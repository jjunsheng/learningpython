# classes to define new types in python
# Numbers
# Strings
# Booleans
# ---
# Lists
# Dictionaries
# ---
# class , always have upper case for first character for every word, e.g EmailClient
# object is an instance of an class, a class simply is a blueprint or template for creating objects
# objects are the actual instances based on the blue print


class Point:
     def move(self):
         print("move")

     def draw(self):
         print("draw")


point1 = Point()
point1.draw()
point1.move()
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
point2.x = 322
print(point2.x)
