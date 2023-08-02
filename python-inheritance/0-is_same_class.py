"""
first python inheritance task
"""


def is_same_class(obj, a_class):
    """
    This checks if the class of the object 
    is the same as the class of the class
    """
    return obj.__class__ is a_class.__class__