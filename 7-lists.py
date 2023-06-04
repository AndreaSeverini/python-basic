# Example 1: When to use lists?
# Lists are used to store multiple items in a single variable.
# You can use lists when you have a collection of items that you want to keep together and manipulate as a group.
# Here's an example:

print("Example 1: When to use lists?")
fruits = ["apple", "banana", "orange"]
print("List of fruits:", fruits)
print("\n")

# Example 2: Main built-in methods for lists
# They have many built-in methods that allow you to manipulate and work with them.
# Here are a few commonly used list methods:

print("Example 2: Main built-in methods for lists")
numbers: list[int] = [1, 2, 3, 4, 5, 6]

# Append method
print("Appended 6 to numbers:", numbers)

# Insert method
numbers.insert(0, 0)
print("Inserted 0 at the beginning of numbers:", numbers)

# Remove method
numbers.remove(3)
print("Removed 3 from numbers:", numbers)

# Pop method
popped_number = numbers.pop()
print("Popped number:", popped_number)
print("Updated numbers after popping:", numbers)

# Index method
index_of_4 = numbers.index(4)
print("Index of 4:", index_of_4)

# Count method
count_of_2 = numbers.count(2)
print("Count of 2:", count_of_2)

# Sort method
numbers.sort()
print("Sorted numbers:", numbers)

# Reverse method
numbers.reverse()
print("Reversed numbers:", numbers)

# Copy method
numbers_copy = numbers.copy()
print("Copy of numbers:", numbers_copy)

# Clear method
numbers.clear()
print("Cleared numbers:", numbers)
print("\n")
