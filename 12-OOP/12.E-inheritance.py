print("Example: Diving Deep into Inheritance")

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


class Square(Polygon):
    """
    The Square class is derived from the base class Polygon.
    It inherits the attributes and methods of the base class.
    """
    def area(self):
        """
        The area method is defined in the Square class.
        It calculates and returns the area of a square based on the width and height inherited from the base class.
        """
        return self.get_width() * self.get_height()


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


pol = Square()
pol.set_val(10, 10)
print(pol.area())  # Output: 100

pol2 = Triangle()
pol2.set_val(10, 10)
print(pol2.area())  # Output: 100

# In this example, we define a base class called Polygon.

# The Polygon class has two private variables, __width and __height, which are not directly accessible from outside
# the class. These variables are intended to be used within the class and its derived classes.

# The Polygon class also has three methods:
# - set_val: Sets the values of the private variables __width and __height.
# - get_width: Returns the value of the private variable __width.
# - get_height: Returns the value of the private variable __height.

# We then define two derived classes, Square and Triangle, which inherit from the base class Polygon.

# The Square class overrides the area method inherited from the base class. It calculates the area of a square
# using the inherited width and height attributes.

# The Triangle class also overrides the area method inherited from the base class. It calculates the area of a triangle
# using the inherited width and height attributes.

# We create an object of the Square class using "pol = Square()".
# We can then call the set_val method to set the width and height values to 10 using "pol.set_val(10, 10)".

# Finally, we call the area method of the Square object using "print(pol.area())".
# This calculates and prints the area of the square, which is 100 in this case.

# This demonstrates inheritance in Python, where the derived classes (Square and Triangle) inherit attributes and
# methods from the base class (Polygon), and can override those methods to provide specific implementations.

# The output will be:
# 100


# MULTIPLE INHERITANCE

class Shape:
    __color = None

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class TriangleComplex(Polygon, Shape):
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


pol3 = TriangleComplex()
# We can now use both method of the parent class
pol3.set_val(10, 10)
pol3.set_color('blue')
print(pol3.get_color(), pol3.area())  # Output: 100