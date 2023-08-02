"""
third python inheritance task
"""


def inherits_from(obj, a_class):
    """
    this function checks if the object
    is an instance of a descendant of the class, 
    either directly or indirectly
    """

    obj_class = obj.__class__
    if issubclass(obj_class, a_class) and obj_class is not a_class:
        return True
    else:
        return False
