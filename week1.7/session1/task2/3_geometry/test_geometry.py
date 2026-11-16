# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle
import math

def test_point_constructor():
    '''
    Test if creating a point returns an x and y value
    '''
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    '''
    Test if calling a Point's distance method returns correct values
    '''
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    '''
    Test if calling a Point's distance_to method returns correct values
    '''
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    
    # complete the implementation for
    # testing distance_to()
    assert p1.distance_to(p2) == 5.0
    

# Write test functions to test the __init__(), 
# area() and perimeter() methods in Circle class
# you can use the default value for centre coordinates
def test_circle_init():
    '''
    Test if creating a circle returns a radius and centre Point value
    '''
    c = Circle(5, Point(3, 4))
    assert c.radius == 5
    assert c.centre == Point(3, 4)

def test_circle_area():
    '''
    Test if calling a circle's area method returns the circle's correct area
    '''
    c = Circle(5, Point(3, 4))
    assert c.area() == math.pi * c.radius ** 2

def test_circle_perimeter():
    '''
    Test if calling a circle's perimeter method returns the circle's correct perimeter
    '''
    c = Circle(5, Point(3, 4))
    assert c.perimeter() == 2.0 * math.pi * c.radius

test_point_constructor()
test_point_distance()
test_point_distance_to
test_circle_init()
test_circle_area()
test_circle_perimeter()