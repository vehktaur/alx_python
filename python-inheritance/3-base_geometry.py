"""
fourth python inheritance task
"""


class BaseGeometry():
    """
    created here is an empty class
    that does nothing
    """

    def __dir__(self):
        variables = super().__dir__()
        new_variables = []
        for var in variables:
            if var != "__init_subclass__":
                new_variables.append(var)
        return new_variables
