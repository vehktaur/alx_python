"""
rectangle module for the rectangle class
"""


from models.base import Base

class Rectangle(Base):
    """
    rectangle class that inherits from the base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization function for the rectangle class
        """
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
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
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
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
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
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
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
        public area method that returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        rectangle display public method
        """
        for row in range(self.__y):
            print()
        else:
            for row in range(self.__height):
                for column in range(self.__x):
                    print(" ", end="")
                else:
                    for column in range(self.__width):
                        print("#", end="")
                    else:
                        print()

    def __str__(self):
        """
        rewrite default str method string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        update function to update the default arguments and id
        """
        args_length = len(args)
        kwargs_length = len(kwargs)

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            elif key == "x":
                self.__x = value
            else:
                self.__y = value

        if args_length > 0:
            self.id = args[0]
        if args_length > 1:
            self.__width = args[1]
        if args_length > 2:
            self.__height = args[2]
        if args_length > 3:
            self.__x = args[3]
        if args_length > 4:
            self.__y = args[4]
