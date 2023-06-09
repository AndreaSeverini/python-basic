from abc import ABC, abstractmethod  # Importing the ABC class and the abstractmethod decorator


class Shape(ABC):  # Parent class that is a child of ABC (Abstract Base Class)
    @abstractmethod  # Using the abstractmethod decorator to define abstract methods
    def area(self):
        pass  # Empty function that doesn't do anything

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):  # Child class inheriting from Shape
    def __init__(self, side):
        self.__side = side

    def area(self):  # Implementing the area method in the child class
        return self.__side * self.__side

    def perimeter(self):  # Implementing the perimeter method in the child class
        return 4 * self.__side


# obj_shape = Shape()  # You cannot instantiate an abstract class
obj_square = Square(5)  # Creating an instance of the Square class

print(obj_square.area())  # Output: 25 (Calling the area method of the Square object)
print(obj_square.perimeter())  # Output: 20 (Calling the perimeter method of the Square object)

# In this example, we have a parent class called Shape that is a child of the ABC (Abstract Base Class).

# The Shape class is an abstract class that defines two abstract methods: area and perimeter.
# These abstract methods are declared using the abstractmethod decorator,
# indicating that they must be implemented by the child classes.

# The Square class is a child class of Shape and provides concrete implementations of the area and perimeter methods.
# It also has an __init__ method to initialize the side attribute.

# By overriding the abstract methods area and perimeter in the Square class, we provide specific implementations
# based on the side length of the square.

# Attempting to directly instantiate the Shape class with obj_shape = Shape() will raise an error,
# as abstract classes cannot be instantiated.

# We can create an instance of the Square class with obj_square = Square(5),
# providing a side length of 5 for the square.

# We can then call the area and perimeter methods on the obj_square object,
# which will use the specific implementations provided in the Square class.

# The output will be 25 for the area (side length squared) and 20 for the perimeter (4 times the side length).

# This demonstrates the concept of abstract classes, where the parent class defines abstract methods
# that must be implemented by the child classes. Abstract classes cannot be instantiated directly;
# they provide a blueprint for child classes to follow.
