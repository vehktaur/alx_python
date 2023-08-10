"""
seventh python inheritance task
"""

BaseGeometry = __import__("5-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """
    This creates a rectangle object
    """

    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
