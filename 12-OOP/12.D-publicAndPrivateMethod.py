print("Example: Diving Deep with Public and Private Methods in Python")

class Ex:
    def __init__(self):
        self.a = 10
        self._b = 50  # partially private
        self.__c = 100  # private

    def public_func(self):
        """
        The public_func method is a public method that can be accessed from outside the class.
        It can access all the attributes of the class, including public, partially private, and private variables.
        """
        print(self.a)
        print(self._b)
        print(self.__c)

    def __private_func(self):
        """
        The __private_func method is a private method that is intended to be used within the class only.
        It is not accessible from outside the class.
        """
        print('Private Func')

s = Ex()

s.public_func()  # Accessing the public_func method

# s.__private_func()  # This will result in an AttributeError because the method is private

# In this example, we define a class called Ex.

# Within the class, we have three instance variables: a, _b, and __c.
# The variable a is a public variable that can be accessed directly.
# The variable _b is a partially private variable indicated by a single underscore prefix.
# The variable __c is a private variable indicated by the double underscores prefix.

# Public and partially private variables can be accessed from outside the class.
# Private variables, however, are intended to be used only within the class.

# The public_func method is a public method that can be accessed from outside the class.
# It can access all the attributes of the class, including public, partially private, and private variables.
# In this case, the method prints the values of the variables a, _b, and __c.

# The __private_func method is a private method that is intended to be used within the class only.
# It is not accessible from outside the class.

# When we create an object of the Ex class using the statement "s = Ex()",
# the __init__ method is automatically called, initializing the variables a, _b, and __c.

# We can then access the public_func method of the object by calling "s.public_func()".
# This will print the values of the variables a, _b, and __c.

# However, if we try to call the __private_func method from outside the class, like "s.__private_func()",
# it will result in an AttributeError because the method is private and cannot be accessed externally.

# This demonstrates the concept of public and private methods, where public methods can be accessed from outside
# the class, and private methods are intended for internal use within the class.

# The output will be:
# 10
# 50
# 100
