"""
Just another implementation of the class object
"""


class Square:

    """
    Size validation for the Square class
    """

    def __init__(self, size=0):
        self.size = size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, size):
            if not type(size) is int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        return self.size ** 2
