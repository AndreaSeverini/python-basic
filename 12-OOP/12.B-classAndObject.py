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
