class Parent:
    def __init__(self, name):
        print('Parent Constructor', name)


class ParentB:
    def __init__(self, name):
        print('ParentB Constructor', name)


class Child(Parent, ParentB):
    def __init__(self):
        print('Child Constructor')
        # Parent.__init__(self, "Andrea")  # Without super()
        super().__init__("Andrea")  # Using super()
        ParentB.__init__(self, "Luca")


child = Child()
# Method Resolution Order
print(Child.__mro__)
# (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.ParentB'>, <class 'object'>)

# In this example, we have three classes: Parent, ParentB, and Child.

# The Parent class has an __init__ method that takes a name parameter and prints a message.
# The ParentB class also has an __init__ method that takes a name parameter and prints a message.

# The Child class inherits from both Parent and ParentB classes.

# Inside the Child class's __init__ method, we use the super() function to call the __init__ method of the parent classes.
# By using super().__init__("Andrea"), the __init__ method of Parent is called, which prints "Parent Constructor Andrea".
# Then, we explicitly call the __init__ method of ParentB using ParentB.__init__(self, "Luca"),
# which prints "ParentB Constructor Luca".

# When we create an instance of Child using child = Child(), the constructors of the parent classes are called
# in the order specified by the Method Resolution Order (MRO).
# In this case, it first calls the __init__ method of Parent, followed by the __init__ method of ParentB.

# The line print(Child.__mro__) outputs the Method Resolution Order (MRO) for the Child class.
# It shows the sequence in which the classes will be searched for a particular method or attribute.
# In this case, the MRO is (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.ParentB'>, <class 'object'>).

# The output will be:
# Child Constructor
# Parent Constructor Andrea
# ParentB Constructor Luca
# (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.ParentB'>, <class 'object'>)
