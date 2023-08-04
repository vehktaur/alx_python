"""
fourth python inheritance task
"""


class BaseGeometryMeta(type):
    def __dir__(self):
        variables = super().__dir__()
        new_variables = [var for var in variables if var != "__init_subclass__"]
        return new_variables

class BaseGeometry(metaclass=BaseGeometryMeta):
    """
    created here is an empty class
    that does nothing
    """
    def __dir__(self):
        variables = super().__dir__()
        new_variables = [var for var in variables if var != "__init_subclass__"]
        return new_variables
