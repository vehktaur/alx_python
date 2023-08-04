"""
8th python inheritance task
"""


class BaseGeometryMeta(type):
    def __dir__(self):
        variables = super().__dir__()
        new_variables = [
            var for var in variables if var != "__init_subclass__"]
        return new_variables


class BaseGeometry(metaclass=BaseGeometryMeta):
    """
    non empty class
    """

    def __dir__(self):
        variables = super().__dir__()
        new_variables = [
            var for var in variables if var != "__init_subclass__"]
        return new_variables

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return value


class Rectangle(BaseGeometry):

    """
    This creates a rectangle object
    """

    def __init_subclass__(cls):
        return object.__init_subclass__()

    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
    def area(self):
        print(f"[Rectangle] {self.__width} / {self.__height}")


