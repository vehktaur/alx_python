"""
fourth python inheritance task
"""


class BaseGeometry(object):
    """
    created here is an empty class
    that does nothing
    """
    def __dir__(self):
        return [attr for attr in dir(self) if not "__init_subclass__"]
