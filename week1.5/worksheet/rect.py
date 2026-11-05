# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if not isinstance((width or height), int):
            raise TypeError("Width or height is not of type int")

        if width <= 0 or height <= 0:
            raise ValueError("Width or height must be greater than 0")

        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(self):
        '''
        Returns a boolean value, if this rectangle is a square or not
        '''
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        '''
        Returns the area of this rectangle
        '''
        return (self.width * self.height)

    def perimeter(self):
        '''
        Returns the perimeter of this rectangle
        '''
        return (2 * (self.width + self.height))