"""
fifth python inheritance task
"""


class BaseGeometryMeta(type):
    def __dir__(self):
        variables = super().__dir__()
        new_variables = [var for var in variables if var != "__init_subclass__"]
        return new_variables

class BaseGeometry(metaclass=BaseGeometryMeta):
    """
    non empty class
    """
    def __dir__(self):
        variables = super().__dir__()
        new_variables = [var for var in variables if var != "__init_subclass__"]
        return new_variables

    def area(self):
        raise Exception("area() is not implemented")
