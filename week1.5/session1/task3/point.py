# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Add distance() method here
    def distance(self) :
        return math.sqrt(self.x**2 + self.y**2)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)


# Finally, add code here to demonstrate use of Point
a = Point(3, 4)
b = Point(6, 8)
print(a.distance())
print(a.distance_to(b))