# Represents the type of data
# In Python there are two dataTypes
# - Built-in Datatype
# - User-defined Datatype

## BUILT-IN
# None, Numeric, Sequences, Sets, Mapping (Dictionaries)

# None
print("BI - None type")
# It is comparable to null in Javascript
var1 = None
print(var1)
print(type(var1))

# Numeric (Int, Float, Complex, Bool)
print("BI - Int type")
var2 = 5
print(var2)
print(type(var2))

print("BI - Float type")
var3 = 5.5
print(var3)
print(type(var3))

print("BI - Complex type")
var4 = 5 + 5j
print(var4)
print(type(var4))

print("BI - Bool type")
var5 = var3 > var2
print(var5)
print(type(var5))

# Using Bool in if condition
if var5:
    print('True')
else:
    print('False')

# Sequences (String, List, Tuple, Range)
print("BI - String type")
var6 = 'Hello Python'
print(var6)
print(type(var6))

print("BI - List type")
# A list represents a group of elements of DIFFERENT TYPES. Can GROW DYNAMICALLY.
var7 = ['Hello Python', 6, True]
print(var7)
print(var7[0], var7[1])
print(type(var7))