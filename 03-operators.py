# We need to perform operations from data to get a desired result

# Here  some simple examples of each type of operator:

# 1. Arithmetic Operators:
print('Arithmetic Operators')

a = 10
b = 3

print('a=',a,'b=', b)

print('Addition')
print(a + b)  # Addition: 13
print('Subtraction')
print(a - b)  # Subtraction: 7
print('Multiplication')
print(a * b)  # Multiplication: 30
print('Division')
print(a / b)  # Division: 3.3333333333333335
print('Floor')
print(a // b) # Floor Division: 3
print('Modulo')
print(a % b)  # Modulo: 1
print('Exponentiation')
print(a ** b) # Exponentiation: 1000


# 2. Assignment Operators:
print('Assignment Operators')
x = 5
y = 10

print('x=',x,'y=',y)

print('SUM ASSIGNMENT x = x + y')
x += y  # x = x + y
print('x=',x)  # Output: 15

print('SUB ASSIGNMENT y = y - 3')
y -= 3  # y = y - 3
print('y=',y)  # Output: 7



# 3. Comparison Operators:

print('Comparison Operators')
a = 5
b = 3

print('a=',a,'b=', b)

print('Equal')
print(a == b)  # Equal to: False
print('Not equal')
print(a != b)  # Not equal to: True
print('Greater')
print(a > b)   # Greater than: True
print('Less')
print(a < b)   # Less than: False
print('Greater than or equal')
print(a >= b)  # Greater than or equal to: True
print('Less than or equal')
print(a <= b)  # Less than or equal to: False

# 4. Logical Operators:

print('Logical Operators')
x = True
y = False

print('x=',x,'y=',y)

print('AND')
print(x and y)  # Logical AND: False
print('OR')
print(x or y)   # Logical OR: True
print('NOT')
print(not x)    # Logical NOT: False


# 5. Identity Operators:

print('Identity Operators')

a = 5
b = 5
c = [1, 2, 3]
d = [1, 2, 3]

print('a=',a,'b=', b,'c=',c,'d=', d)

print('Identity equality a is b')
print(a is b)     # Identity equality: True
print('Identity equality c is d')
print(c is d)     # Identity equality: False (different objects)
print('Identity inequality c is not d')
print(c is not d) # Identity inequality: True

# 6. Membership Operators:

print('Membership Operators')
list1 = [1, 2, 3, 4, 5]

print('VIP LIST: ', list1)

print('Membership of 3 in list1')
print(3 in list1)      # Membership: True
print('Non-Membership of 6 in list1')
print(6 not in list1)  # Non-membership: True


# 7. Bitwise Operators:

print('Bitwise Operators')
a = 5  # Binary: 0101
b = 3  # Binary: 0011

print('a=',a, 'Binary: 0101','b=', b,'Binary: 0011')

print('Bitwise AND: 0001')
print(a & b)   # Bitwise AND: 0001 (Decimal: 1)
print('Bitwise OR: 0111')
print(a | b)   # Bitwise OR: 0111 (Decimal: 7)
print('Bitwise XOR: 0110')
print(a ^ b)   # Bitwise XOR: 0110 (Decimal: 6)
print('Bitwise NOT: 1010')
print(~a)      # Bitwise NOT: 1010 (Decimal: -6)
print('Left shift by 1: 1010 (a<<1)')
print(a << 1)  # Left shift by 1: 1010 (Decimal: 10)
print('Right shift by 1: 0010 (a>>1)')
print(a >> 1)  # Right shift by 1: 0010 (Decimal: 2)
