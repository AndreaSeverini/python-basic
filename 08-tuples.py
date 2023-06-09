# Example 1: When to use tuples?
# Tuples are used to store multiple items in a single variable, similar to lists.
# The main difference is that tuples are immutable, meaning they cannot be modified once created.
# You can use tuples when you have a collection of items that should not be changed.
# Here's an example:

print("Example 1: When to use tuples?")
person = ("John", 25, "USA")
print("Person details:", person)
print("\n")

# Example 2: Main built-in methods for tuples
# Tuples have fewer built-in methods compared to lists due to their immutability.
# However, they still provide some useful methods.
# Here are a few commonly used tuple methods:

print("Example 2: Main built-in methods for tuples")
numbers = (1, 2, 3, 4, 5)

# Index method
index_of_4 = numbers.index(4)
print("Index of 4:", index_of_4)

# Count method
count_of_2 = numbers.count(2)
print("Count of 2:", count_of_2)

# Length of tuple
length = len(numbers)
print("Length of tuple:", length)
print("\n")

# Example 2: Main built-in methods for tuples (continued)
# Tuples have fewer built-in methods compared to lists due to their immutability.
# However, they still provide some useful methods.
# Here are a few more commonly used tuple methods:

print("Example 2: Main built-in methods for tuples (continued)")
person = ("John", 25, "USA")

# Accessing tuple elements
name = person[0]
age = person[1]
country = person[2]
print("Name:", name)
print("Age:", age)
print("Country:", country)

# Tuple unpacking
name, age, country = person
print("Unpacked values - Name:", name)
print("Unpacked values - Age:", age)
print("Unpacked values - Country:", country)

# Concatenating tuples
fruits = ("apple", "banana", "orange")
combined_tuple = person + fruits
print("Combined tuple:", combined_tuple)

# Checking for an element in a tuple
contains_banana = "banana" in combined_tuple
print("Contains 'banana':", contains_banana)

# Converting a tuple to a list
fruits_list = list(fruits)
print("Converted to list:", fruits_list)

# Converting a list to a tuple
fruits_tuple = tuple(fruits_list)
print("Converted back to tuple:", fruits_tuple)
print("\n")
