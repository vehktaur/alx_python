"""
Base.py module for python almost a circle project
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
