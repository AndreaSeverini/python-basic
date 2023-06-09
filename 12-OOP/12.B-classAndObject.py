print("Example: Diving Deep with Classes and Objects in Python")


# Class definition

class Student:

    def __init__(self):
        """
        The __init__ method is a special method in Python classes.
        It is called automatically when a new object is created from the class.
        The self parameter refers to the newly created object itself.
        It allows us to access and assign values to the object's attributes.
        """
        self.name = 'Andrea'
        self.age = 29
        self.marks = 28

    def talk(self):
        """
        The talk method is a regular method defined within the class.
        It can be called on objects created from the class.
        The self parameter in the talk method refers to the object on which the method is called.
        It allows us to access the object's attributes and perform actions using the object's data.
        """
        print('Name -', self.name)
        print('Age -', self.age)
        print('Marks -', self.marks)


# Object instantiation
student = Student()  # Creating an object of the Student class

student.talk()  # Calling the talk method of the student object

# In this example, we define a class called Student.

# The __init__ method is a special method in Python classes.
# It is called automatically when a new object is created from the class.
# The method definition starts with the def keyword, followed by __init__ (with double underscores),
# and the self parameter as the first parameter.
# The self parameter refers to the newly created object itself.
# It allows us to access and assign values to the object's attributes.

# Inside the __init__ method, we set the initial values for the object's attributes.
# In this case, we assign the name 'Andrea', age 29, and marks 28 to the attributes of the object.

# When we create an object of the Student class using the statement "student = Student()",
# the __init__ method is automatically called and the attributes of the object are initialized.

# The self parameter is used to refer to the object itself within the class methods.
# In the talk method, we use self.name, self.age, and self.marks to access the attributes of the object.

# We can then call the talk method on the student object using the dot notation (student.talk()).
# This will print the values of the name, age, and marks attributes of the object.

# The output will be:
# Name - Andrea
# Age - 29
# Marks - 28

# Self and memory allocation

# In Python, when an object is created from a class, memory is allocated to store the object and its attributes.
# The self parameter in Python's class methods is a convention that refers to the object itself.

# When you create an object from a class and call a method on that object, such as student.talk(),
# the self parameter in the talk() method is automatically passed as a reference to the object
# that the method is being called on. This allows the method to access the attributes
# and behavior of that specific object.

# Here's a breakdown of how memory allocation and the self parameter work:

# Object creation:
# When you create an object from a class, memory is allocated to store the object.
# The memory includes space for the object's attributes and any other internal data structures required by the object.

# Method call:
# When you call a method on the object, such as student.talk(),
# the method is executed in the context of that specific object.
# The object is automatically passed as the first argument to the method.

# self parameter:
# The self parameter is a reference to the object itself.
# It allows the method to access the object's attributes and perform actions using the object's data.
# By convention, the first parameter of a method in a class is named self,
# although you can technically choose any valid variable name.
# However, it is recommended to stick with the convention of using self to improve code readability
# and maintain consistency.

# Accessing attributes:
# Within the method, you can use self to access the object's attributes.
# For example, self.name refers to the name attribute of the object, self.age refers to the age attribute,
# and so on. The self parameter acts as a reference to the current object, allowing you to access
# and manipulate its data.

# By using the self parameter, Python ensures that each method call on an object operates on the correct instance
# of the class.
# It allows multiple objects of the same class to exist simultaneously, each with its own set of attributes
# and behavior.
# It's important to note that the self parameter is implicitly passed by the Python runtime
# when you call a method on an object.
# You don't need to explicitly provide the argument when calling the method.
# Overall, the self parameter plays a crucial role in enabling object-oriented programming in Python
# by providing a reference to the object itself within class methods.
# It allows methods to access and manipulate the object's attributes and behavior,
# contributing to the object's unique state and functionality.
