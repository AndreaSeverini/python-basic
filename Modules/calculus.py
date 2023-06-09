# This function adds two integers
def add_integer(x, y):
    # Check if both x and y are integers using isinstance()
    if not isinstance(x, int) or not isinstance(y, int):
        # If either x or y is not an integer, return an error message
        return 'Mismatching types'
    # If both are integers, return their sum
    return x + y


# This function multiplies two integers
def multiply_integer(x, y):
    # Check if both x and y are integers using isinstance()
    if not isinstance(x, int) or not isinstance(y, int):
        # If either x or y is not an integer, return an error message
        return 'Mismatching types'
    # If both are integers, return their product
    return x * y
