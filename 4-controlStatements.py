# Example 1: if statement
# The "if" statement allows you to execute a block of code conditionally, based on a specific condition.
x = 10
if x > 5:
    print("x is greater than 5")  # This line will only execute if x > 5

# Example 2: if else statement
# The "if else" statement allows you to execute different blocks of code based on a condition.
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")  # This line will execute if x <= 5

# Example 3: if else statement with operators
# You can use comparison operators (e.g., >, <, ==) to create conditions in if and if else statements.
x = 10
y = 5
if x > y:
    print("x is greater than y")  # This line will execute if x > y
else:
    print("x is less than or equal to y")  # This line will execute if x <= y

# Example 4: if elif else and nested if statements
# The "elif" (short for "else if") statement allows you to add more conditions to your code.
# You can also nest if statements within other if statements.
x = 10
y = 5
if x > y:
    print("x is greater than y")  # This line will execute if x > y
elif x < y:
    print("x is less than y")  # This line will execute if x < y
else:
    print("x is equal to y")  # This line will execute if x == y

# Example 5: nested if statements
# You can nest if statements within other if statements to create more complex logic.
x = 10
y = 5
if x > y:
    if x > 0:
        print("x is positive and greater than y")  # This line will execute if x > 0 and x > y
    else:
        print("x is negative")  # This line will execute if x <= 0
else:
    print("x is less than or equal to y")  # This line will execute if x <= y

