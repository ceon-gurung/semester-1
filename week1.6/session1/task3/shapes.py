# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour

class Circle:
    def __init__(self, radius, centre, colour):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be an int or a float")
        if radius <= 0:
            raise ValueError("radius must be greater than 0")

        if not isinstance(centre, Point):
            raise TypeError("position must be a Point")
        
        super().__init__()
        self.radius = radius
        self.centre = centre
        self.colour = colour

    def __str__(self):
        return self.colour + " circle, radius " + str(self.radius) + " at " + str(self.centre)

    def area(self):
        return math.pi * self.radius ** 2

    def perimiter(self):
        return math.pi * self.radius * 2

# Implement your Circle class here
# Make sure that it inherits properly from Shape!
