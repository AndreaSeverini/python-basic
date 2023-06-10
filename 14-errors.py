# ERRORS AND ERROR HANDLING

# Compile-Time Error

x = 1
print('Hello')  # This line will not be printed due to the compile-time error
if x == 1   # Syntax error: Missing colon (:) at the end of the line
        print('Hello')

# Run-Time Error

def concat(a, b):
    print(a + b)

print('Hello')  # This line will be printed
concat('Hello', 100)  # TypeError: Cannot concatenate 'str' and 'int' objects

# Logical Error

def inc(sal):
    sal = sal * 30/100  # Logical error: Missing the increment part (+ 100% or + sal)
    return sal

sal = inc(1000)
print('The salary will be incremented by: %.2f' % sal)

# In this example, we demonstrate different types of errors: compile-time errors, run-time errors, and logical errors.

# Compile-Time Error: This error occurs during the compilation of the code before it is executed.
# In the code, there is a missing colon (:) at the end of the if statement, resulting in a syntax error.
# Since the code cannot be compiled successfully, the line `print('Hello')` following the if statement will not be executed.

# Run-Time Error: This error occurs during the execution of the code.
# In the code, the `concat` function attempts to concatenate a string (`'Hello'`) with an integer (`100`).
# This results in a TypeError because the `+` operator cannot be used between these two types.
# The line `print('Hello')` preceding the `concat` function will be executed successfully before the error occurs.

# Logical Error: This error occurs when the code does not produce the expected or intended result
# due to incorrect logic or calculation. In the code, the `inc` function calculates a salary increment
# but only multiplies it by 30% without adding the increment amount to the original salary.
# This results in a logical error, where the increment is missing.
# The line `sal = inc(1000)` successfully calls the `inc` function, but the calculated `sal` value
# will be incorrect due to the logical error.

# Error Handling: In this example, we do not demonstrate explicit error handling.
# However, in a real-world scenario, you can use try-except blocks to catch and handle specific types of errors.
# By implementing error handling, you can gracefully handle exceptions and prevent your program
# from abruptly terminating when errors occur.

# This example showcases different types of errors and highlights the importance of understanding
# and addressing them to ensure your code functions as intended.
