print("Example 5: Object-Oriented Programming Concepts")


# Class definition
class Animal:

    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


# Inheritance
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


# Inheritance
class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Object instantiation
dog = Dog("Buddy")  # Creating an object of the Dog class
cat = Cat("Whiskers")  # Creating an object of the Cat class

# Polymorphism
animals = [dog, cat]  # Storing objects in a list
for animal in animals:
    print(animal.name + " says " + animal.make_sound())
    # Polymorphism: The make_sound method behaves differently based on the object's class


# Abstraction and Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


# Object instantiation
account = BankAccount("123456789", 1000)  # Creating an instance of the BankAccount class

# Using encapsulated methods
account.deposit(500)  # Depositing an amount into the account
account.withdraw(200)  # Withdrawing an amount from the account
account.display_balance()  # Displaying the account balance

# In this example, we define a class called Animal as the base class, which has an __init__ method
# and a make_sound method.
# Then, we create two derived classes, Dog and Cat, which inherit from the Animal class
# and override the make_sound method.

# We then instantiate objects of the Dog and Cat classes, demonstrating the concept of objects.
# The objects are stored in a list, and we iterate over them to demonstrate polymorphism,
# where the same method name make_sound behaves differently based on the object's class.

# Next, we introduce abstraction and encapsulation through the BankAccount class.
# It has private attributes (account_number and balance) and public methods (deposit, withdraw, and display_balance)
# to interact with those attributes. The methods provide an abstraction layer for working with the bank account
# and encapsulate the internal implementation details.

# Finally, we create an instance of the BankAccount class, perform some operations (deposit, withdrawal),
# and display the account balance using the encapsulated methods.
