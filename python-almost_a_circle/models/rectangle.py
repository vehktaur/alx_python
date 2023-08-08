"""
rectangle module
"""

from base import Base

"""
rectangle module
"""


class Rectangle(Base):
    """
    rectangle base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        rectangle init function
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter function for width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter function for width
        """
        self.__width = width

    @property
    def height(self):
        """
        getter function for height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter function for height
        """
        self.__height = height

    @property
    def x(self):
        """
        getter function for x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter function for x
        """
        self.__x = x

    @property
    def y(self):
        """
        getter function for x
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter function for y
        """
        self.__y = y
