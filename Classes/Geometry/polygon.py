class Polygon:
    __width = None  # Restricted for Polygon
    __height = None

    def set_val(self, width, height):
        """
        The set_val method is defined in the base class Polygon.
        It allows setting the values of the private variables __width and __height.
        """
        self.__width = width
        self.__height = height

    def get_width(self):
        """
        The get_width method is defined in the base class Polygon.
        It returns the value of the private variable __width.
        """
        return self.__width

    def get_height(self):
        """
        The get_height method is defined in the base class Polygon.
        It returns the value of the private variable __height.
        """
        return self.__height
