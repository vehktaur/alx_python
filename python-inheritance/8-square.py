"""
8th python inheritance task
"""

from _7_rectangle import Rectangle

class Square(Rectangle):
    """
    This class will print a square with dimensions
    of the provided size
    """

    def __init__(self, size):
        self.__size = super().integer_validator("size", size)
        super().__init__(size, size)


a = Square(4)
print(a)
print(issubclass(Square, Rectangle))