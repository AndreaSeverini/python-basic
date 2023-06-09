from Classes.Geometry.polygon import Polygon


class Triangle(Polygon):
    """
    The Triangle class is derived from the base class Polygon.
    It inherits the attributes and methods of the base class.
    """
    def area(self):
        """
        The area method is defined in the Triangle class.
        It calculates and returns the area of a triangle based on the width and height inherited from the base class.
        """
        return self.get_width() * self.get_height() * 1/2