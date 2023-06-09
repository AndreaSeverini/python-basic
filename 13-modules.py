# Importing modules
from Modules import calculus  # imported from the Modules folder
import Modules.calculus as my_func
from Classes.Geometry.square import Square
from Classes.Geometry.triangle import Triangle

# Using functions from the calculus module
add = calculus.add_integer(3, 5)  # Calling the add_integer function from the calculus module
print(add)  # Output: 8

add2 = calculus.add_integer(3, '2')  # Passing mismatching types to the add_integer function
print(add2)  # Output: Mismatching types

add3 = my_func.add_integer(1, 2)  # Calling the add_integer function using the alias my_func
print(add3)  # Output: 3

multiply = calculus.multiply_integer(3, 5)  # Calling the multiply_integer function from the calculus module
print(multiply)  # Output: 15

multiply2 = calculus.multiply_integer(3, '5')  # Passing mismatching types to the multiply_integer function
print(multiply2)  # Output: Mismatching types


# Refactoring inheritance classes example with modules

pol = Square()  # Creating an object of the Square class
pol.set_val(10, 10)  # Setting the width and height of the Square object
print(pol.area())  # Output: 100 (Calculating and printing the area of the Square)

pol2 = Triangle()  # Creating an object of the Triangle class
pol2.set_val(10, 10)  # Setting the width and height of the Triangle object
print(pol2.area())  # Output: 100 (Calculating and printing the area of the Triangle)
