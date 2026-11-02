# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

from geometry import Point, Circle

p = Point(3, 4)
c = Circle(5, p)

a = Point(2,2)
b = Point(0,0)
ca = Point(10, 25)

def inside(point, circle):
    if (point.distance_to(circle.getCentre())) < circle.getRadius():
        return "The point is inside the cirlce"
    else:
        return "The point is outside the cirlce"

print(inside(a, c))