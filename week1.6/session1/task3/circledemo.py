# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)


from shapes import Shape
from shapes import Circle
from point import Point

p1 = Point(3, 4)
c = Circle(5, p1, "red")
print(c)
print(c.area())
print(c.perimiter())

p2 = Point(2, 50)
print("Moving circle centre to " + str(p2))
print(c)

print("Changing the circle's colour to green...")
c.colour = "green"
print(c)