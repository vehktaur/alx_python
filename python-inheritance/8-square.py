"""
8th python inheritance task
"""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """
    This class will print a square with dimensions
    of the provided size
    """

    def __init__(self, size):
        self.__size = super().integer_validator("size", size)
        super().__init__(size, size)


print(issubclass(Square, Rectangle))
