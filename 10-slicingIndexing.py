# Example 1: Indexing, Slicing, and Negative Indexing with Tuples
print("Example 1: Indexing, Slicing, and Negative Indexing with Tuples")
fruits = ("apple", "banana", "orange", "grape", "kiwi")

# Indexing: Accessing elements by their position
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])

# Slicing: Accessing a range of elements
print("Slice of fruits[1:4]:", fruits[1:4])
print("Slice of fruits[:3]:", fruits[:3])
print("Slice of fruits[2:]:", fruits[2:])

# Negative Indexing: Accessing elements from the end
print("Last fruit:", fruits[-1])
print("Second to last fruit:", fruits[-2])
print("\n")

# Example 2: Indexing, Slicing, and Negative Indexing with Lists
print("Example 2: Indexing, Slicing, and Negative Indexing with Lists")
numbers = [1, 2, 3, 4, 5]

# Indexing: Accessing elements by their position
print("First number:", numbers[0])
print("Third number:", numbers[2])

# Slicing: Accessing a range of elements
print("Slice of numbers[1:4]:", numbers[1:4])
print("Slice of numbers[:3]:", numbers[:3])
print("Slice of numbers[2:]:", numbers[2:])

# Negative Indexing: Accessing elements from the end
print("Last number:", numbers[-1])
print("Second to last number:", numbers[-2])
print("\n")

# Example 3: Indexing, Slicing, and Negative Indexing with Dictionaries
print("Example 3: Indexing, Slicing, and Negative Indexing with Dictionaries")
person = {
    "name": "John",
    "age": 25,
    "country": "USA"
}

# Indexing: Accessing values by their keys
print("Name:", person["name"])
print("Age:", person["age"])

# Slicing and Negative Indexing do not apply to dictionaries
# as they are not ordered collections.
# Dictionaries are accessed using keys and not positions.
# If the key does not exist, it will raise a KeyError.

# Adding explanation about accessing a key that does not exist
print("Accessing a key that does not exist:")
# Uncomment the following line to see the KeyError
# print(person["gender"])

print("\n")
