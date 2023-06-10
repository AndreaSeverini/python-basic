# EXCEPTION HANDLING

# Built-in Exceptions
result = None
x = int(input('Number 1: '))
y = int(input('Number 2: '))

try:
    result = x / y
except ZeroDivisionError as e:  # Handling a specific exception class: ZeroDivisionError
    print('Zero division Error')
except Exception as e:  # Handling a general exception class: Exception
    print('Error Occurs:', type(e))
else:  # Executed only if no exceptions occur
    print('Else')
finally:  # Executed every time, regardless of exceptions
    # Example: Putting data in a database, writing logs, etc.
    print('Finally')

print('Result =', result)

# In this example, we demonstrate exception handling in Python.

# We ask the user to input two numbers, x and y.

# Inside the try block, we attempt to perform the division operation x / y.
# If a ZeroDivisionError exception occurs (when y is 0), the code inside the corresponding except block will be executed,
# printing the message 'Zero division Error'.

# If any other exception occurs, the code inside the general except block will be executed.
# The type of the exception will be printed using the `type(e)` expression.

# If no exceptions occur, the code inside the else block will be executed, printing 'Else'.

# Regardless of whether an exception occurs or not, the code inside the finally block will be executed,
# printing 'Finally'.
# This block is useful for performing cleanup operations that need to be executed regardless of exceptions.

# The result of the division operation is stored in the `result` variable and printed at the end.

# User-Defined Exceptions

class DrinkException(Exception):
    def __init__(self, arg):
        self.msg = arg

class Coffee:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            raise DrinkException('Too hot to drink')  # Raising a user-defined exception: DrinkException
        elif self.__temperature < 65:
            raise ValueError('Too cold to drink')  # Raising a built-in exception: ValueError
        else:
            print('Enjoy your coffee time!')

drink = Coffee(100)
drink2 = Coffee(20)
drink3 = Coffee(70)
drink.drink_coffee()  # Raises a DrinkException
drink2.drink_coffee()  # Raises a ValueError
drink3.drink_coffee()  # No exception raised

# In this example, we demonstrate user-defined exceptions and how to raise built-in exceptions.

# We define a custom exception class called DrinkException that inherits from the base Exception class.
# The DrinkException class has an __init__ method to initialize the exception message.

# We define a Coffee class that takes the temperature of the coffee as an input.

# The drink_coffee method checks the temperature and raises exceptions based on the temperature range:
# - If the temperature is greater than 85, it raises a DrinkException, indicating that the coffee is too hot to drink.
# - If the temperature is less than 65, it raises a ValueError, indicating that the coffee is too cold to drink.
# - Otherwise, it prints 'Enjoy your coffee time!' indicating that the coffee is at a suitable temperature.

# We create three instances of the Coffee class with different temperature values and call the drink_coffee method on each instance.

# - For the first instance (drink), the temperature is 100, which raises a DrinkException.
# - For the second instance (drink2), the temperature
