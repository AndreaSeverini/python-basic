# Example 1: Using dictionaries with APIs
# Dictionaries are commonly used to work with APIs, where data is often returned as key-value pairs.
# Dictionaries provide a convenient way to store and access data based on unique keys.
# Here's an example:

print("Example 1: Using dictionaries with APIs")
# Simulating API response
api_response = {
    "status": "success",
    "data": {
        "name": "John",
        "age": 25,
        "country": "USA"
    }
}

# Accessing data from the API response
status = api_response["status"]
data = api_response["data"]
name = data["name"]
age = data["age"]
country = data["country"]

print("Status:", status)
print("Name:", name)
print("Age:", age)
print("Country:", country)
print("\n")

# Example 2: Main built-in methods for dictionaries
# Dictionaries have several built-in methods that allow you to manipulate and work with them.
# Here are a few commonly used dictionary methods:

print("Example 2: Main built-in methods for dictionaries")
person = {
    "name": "John",
    "age": 25,
    "country": "USA"
}

# Accessing keys and values
keys = person.keys()
values = person.values()
print("Keys:", keys)
print("Values:", values)

# Accessing items (key-value pairs)
items = person.items()
print("Items:", items)

# Checking if a key exists
has_name = "name" in person
has_gender = "gender" in person
print("Has 'name' key:", has_name)
print("Has 'gender' key:", has_gender)

# Removing an item
removed_age = person.pop("age")
print("Removed age:", removed_age)
print("Updated dictionary:", person)

# Updating/adding items
person["city"] = "New York"
print("Updated dictionary with city:", person)

# Clearing the dictionary
person.clear()
print("Cleared dictionary:", person)
print("\n")

# Additional Theory: Dictionaries in Python
# - Dictionaries are unordered collections of key-value pairs.
# - Keys in a dictionary must be unique and immutable (strings, numbers, tuples), while values can be of any type.
# - Dictionaries are enclosed in curly braces {} and each key-value pair is separated by a colon :.
# - You can access the value associated with a key by using square brackets [] and specifying the key.
# - Dictionaries are mutable, meaning you can modify, add, or remove key-value pairs.
# - Some important methods for dictionaries include keys(), values(), items(), pop(), update(), and clear().

# Example of dictionary creation
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

# Accessing value associated with a key
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])

# Modifying a value
student["age"] = 21
print("Updated age:", student["age"])

# Adding a new key-value pair
student["university"] = "ABC University"
print("Updated dictionary with university:", student)

# Removing a key-value pair
removed_major = student.pop("major")
print("Removed major:", removed_major)
print("Updated dictionary:", student)
