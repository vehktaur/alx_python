"""
rectangle module for the rectangle class
"""

class Base:
    """
    Base class for all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization function with id attribute set
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects



class Rectangle(Base):
    """
    rectangle class that inherits from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization function for the rectangle class
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter function for the width private instance attribute
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter function for the width private instance attribute        
        """
        self.__width = width

    @property
    def height(self):
        """
        getter function for the height private instance attribute
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter function for the height private instance attribute
        """
        self.__height = height

    @property
    def x(self):
        """
        getter function for the x private instance attribute
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter function for the x private instance attribute
        """
        self.__x = x

    @property
    def y(self):
        """
        getter function for the x private instance attribute
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter function for y private instance attribute
        """
        self.__y = y
