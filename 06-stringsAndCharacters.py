# Example 1: Comments and Docstrings
# Comments are used to add explanatory notes or annotations to the code. They are ignored by the Python interpreter.
# Docstrings are used to document functions, classes, or modules. They can be accessed using the __doc__ attribute.
# Here's an example:

# This is a single-line comment

"""
This is a multi-line comment
"""

def greet(name):
    """
    This function greets the person with the given name.
    """
    print("Hello, " + name + "!")

print("Example 1: Comments and Docstrings")
greet("Alice")
print(greet.__doc__)  # Accessing the docstring of the greet function
print("\n")

# Example 2: String methods
# Strings are sequences of characters and have many associated methods for manipulation.
# Here are a few commonly used string methods:

# String length
message = "Hello, World!"
print("Example 2: String methods")
print("Length of message:", len(message))

# Accessing individual characters
print("First character of message:", message[0])
print("Last character of message:", message[-1])

# String slicing
print("Slice from index 7 to the end:", message[7:])
print("Slice from index 7 to 12:", message[7:12])

# Concatenating strings
greeting = "Hello"
name = "Alice"
full_message = greeting + ", " + name + "!"
print("Concatenated message:", full_message)

# Changing case
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())

# Finding substrings
print("Index of 'World':", message.index("World"))
print("Count of 'l':", message.count("l"))
print("\n")

# Example 2: String methods (continued)
# Strings are sequences of characters and have many associated methods for manipulation.
# Here are a few more commonly used string methods:

# Removing whitespace
message = "  Hello, World!  "
print("Example 2: String methods (continued)")
print("Original message:", message)
print("Stripped message:", message.strip())
print("Left-stripped message:", message.lstrip())
print("Right-stripped message:", message.rstrip())

# Checking the start and end of a string
print("Starts with 'Hello':", message.startswith("Hello"))
print("Ends with 'World!':", message.endswith("World!"))

# Splitting a string
words = message.split(",")
print("Split string:", words)

# Joining strings
joined_message = "-".join(words)
print("Joined string:", joined_message)

# Replacing substrings
replaced_message = message.replace("World", "Python")
print("Replaced message:", replaced_message)

# Checking for character types
print("Is 'Hello' alphanumeric?", "Hello".isalnum())
print("Is '123' numeric?", "123".isnumeric())
print("Is 'Hello' alphabetic?", "Hello".isalpha())

# Formatting strings
name = "Alice"
age = 25
formatted_message = "My name is {} and I'm {} years old.".format(name, age)
print("Formatted message:", formatted_message)
print("\n")
