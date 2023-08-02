"""
first python inheritance task
"""


def is_same_class(obj, a_class):
    """
    This checks if the class of the object 
    is the same as the class of the class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
