"""
second python inheritance task
"""


def is_kind_of_class(obj, a_class):
    """
    this function checks if the object
    is a descendant of the class, either
    directly or indirectly
    """

    if obj.__class__.__name__ == a_class.__name__ or isinstance(obj, a_class):
        return True
    else:
        return False
