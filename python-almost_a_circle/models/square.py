"""
Square class module which inherits from rectangle class
"""

from rectangle import Rectangle


class Square(Rectangle):
    """
    square class which inherits from the rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        square initialization method
        """
        super().__init__(size, size, x, y, id)
        self.__height = size
        self.__width = size

    def __str__(self):
        """
        square custom string representation
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
