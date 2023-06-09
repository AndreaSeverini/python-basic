# Example 1: What are functions and when to use them?
# Functions are reusable blocks of code that perform specific tasks.
# They help in organizing code, promoting reusability, and enhancing readability.
# You can define your own functions in Python to solve specific problems or perform specific operations.
# Here's an example:

print("Example 1: What are functions and when to use them?")
# Function to calculate the square of a number
def square(num):
    return num * num

# Using the function
result = square(5)
print("Square of 5:", result)
print("\n")

# Example 2: Parameters, Arguments, and Return
# Functions can have parameters (placeholders) to receive values, which are known as arguments.
# Parameters define the input values that a function expects, and arguments are the actual values passed to a function.
# Functions can also return values using the return statement.
# Here's an example:

print("Example 2: Parameters, Arguments, and Return")
# Function to add two numbers and return the result
def add_numbers(a, b):
    return a + b

# Using the function
sum_result = add_numbers(2, 3)
print("Sum of 2 and 3:", sum_result)
print("\n")

# Example 3: Formal and Actual Arguments (positional, *args, **kwargs)
# Functions can have different types of arguments: formal arguments (parameters), positional arguments, *args (variable-length arguments), **kwargs (keyword arguments).
# Formal arguments are defined in the function signature, and positional, *args, and **kwargs are used when calling the function.
# Here's an example:

print("Example 3: Formal and Actual Arguments (positional, *args, **kwargs)")
# Function to demonstrate different types of arguments
def print_arguments(arg1, arg2, *args, **kwargs):
    print("Positional Argument 1:", arg1)
    print("Positional Argument 2:", arg2)
    print("Variable-length Arguments (*args):", args)
    print("Keyword Arguments (**kwargs):", kwargs)

# Using the function
print_arguments("Hello", "World", "Extra", "Arguments", name="John", age=25)
print("\n")


