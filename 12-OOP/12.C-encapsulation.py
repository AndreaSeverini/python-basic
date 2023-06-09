print("Example: Diving Deep with Encapsulation in Python")

class Speed:
    def __init__(self):
        self.vel = 10
        self.__new_speed = 80  # private variable

    def get_new_speed(self):  # public method to get private variable
        """
        The get_new_speed method is a public method that provides access to the private __new_speed variable.
        It acts as a getter method and returns the value of the private variable.
        """
        return self.__new_speed

    def set_new_speed(self, new_speed):
        """
        The set_new_speed method is a public method that allows setting a new value for the private __new_speed variable.
        It acts as a setter method and assigns the provided value to the private variable.
        """
        self.__new_speed = new_speed

s = Speed()

s.set_new_speed(100)
print(s.get_new_speed())  # Output: 100

# In this example, we define a class called Speed.

# Within the class, we have two instance variables: vel and __new_speed.
# The vel variable is a public variable that can be accessed directly.
# The __new_speed variable is a private variable indicated by the double underscores prefix.

# Encapsulation is achieved by using private variables and providing public methods to access and modify them.
# The private variable __new_speed cannot be accessed directly from outside the class.

# The get_new_speed method is a public method that acts as a getter method for the private __new_speed variable.
# It returns the value of the private variable when called.

# The set_new_speed method is a public method that acts as a setter method for the private __new_speed variable.
# It allows setting a new value for the private variable.

# When we create an object of the Speed class using the statement "s = Speed()",
# the __init__ method is automatically called, initializing the vel and __new_speed variables.

# We can then use the set_new_speed method to modify the value of the private variable.
# In this case, we set the new speed to 100 using "s.set_new_speed(100)".

# To retrieve the value of the private variable, we use the get_new_speed method.
# Calling "print(s.get_new_speed())" prints the value of the private variable, which is 100 in this case.

# This demonstrates encapsulation, where the internal implementation details (private variable) are hidden
# and controlled through public methods (getter and setter methods).

# The output will be:
# 100

