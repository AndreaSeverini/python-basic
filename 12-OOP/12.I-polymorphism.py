# POLYMORPHISM - Overloading Operators

class Doc:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):  # Overloading the basic + operator
        return self.pages + other.pages

    def __mul__(self, other):  # Overloading the basic * operator
        return self.pages * other.pages

    def __gt__(self, other):   # Overloading the basic > operator
        return self.pages > other.pages


d1 = Doc(100)
d2 = Doc(150)

print(d1 + d2)  # Output: 250 (Equivalent to d1.__add__(d2))
print(d1 * d2)  # Output: 15000 (Equivalent to d1.__mul__(d2))
print(d1 > d2)  # Output: False (Equivalent to d1.__gt__(d2))

# In this example, we have a class called Doc.

# The Doc class has an __init__ method that initializes the number of pages of a document.

# We then proceed to overload some basic operators using special methods:

# - The __add__ method overloads the + operator. When the + operator is used with two Doc objects,
#   it will invoke this method and return the sum of their page counts.

# - The __mul__ method overloads the * operator. When the * operator is used with two Doc objects,
#   it will invoke this method and return the product of their page counts.

# - The __gt__ method overloads the > operator. When the > operator is used with two Doc objects,
#   it will invoke this method and return True if the page count of the left-hand side object is greater than
#   the page count of the right-hand side object, and False otherwise.

# We create two Doc objects, d1 and d2, with page counts of 100 and 150, respectively.

# We then demonstrate the polymorphic behavior of the overloaded operators:

# - The expression d1 + d2 invokes the __add__ method and returns the sum of their page counts, which is 250.
# - The expression d1 * d2 invokes the __mul__ method and returns the product of their page counts, which is 15000.
# - The expression d1 > d2 invokes the __gt__ method and compares their page counts,
# returning False since 100 is not greater than 150.

# This demonstrates polymorphism and operator overloading, where the same operator can behave differently
# depending on the type of objects involved. The special methods (__add__, __mul__, __gt__) provide the
# necessary functionality for the operators to work with the specific objects of the Doc class.

# Note that if you have different starting classes, you need to define
# the corresponding special methods (__add__, __mul__, __gt__)
# for each class involved in the operation.
