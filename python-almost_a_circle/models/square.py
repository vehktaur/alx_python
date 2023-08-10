"""
Square class module which inherits from rectangle class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    square class which inherits from the rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        square initialization method
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        square custom string representation
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        size getter method
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter method
        """
        self.width = value
