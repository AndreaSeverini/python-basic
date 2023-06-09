from Modules import calculus
# imported from Modules folder
import Modules.calculus as my_func
from Classes.Geometry.square import Square
from Classes.Geometry.triangle import Triangle

add = calculus.add_integer(3, 5)
print(add)
add2 = calculus.add_integer(3, '2')
print(add2)
add3 = my_func.add_integer(1,2)
print(add3)
multiply = calculus.multiply_integer(3, 5)
print(multiply)
multiply2 = calculus.multiply_integer(3, '5')
print(multiply2)


# Refactoring inheritance classes example with modules

pol = Square()
pol.set_val(10, 10)
print(pol.area())  # Output: 100

pol2 = Triangle()
pol2.set_val(10, 10)
print(pol2.area())  # Output: 100
