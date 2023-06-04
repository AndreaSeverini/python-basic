# Example 1: while loop
# The "while" loop allows you to repeatedly execute a block of code as long as a condition remains true.
count = 0
print("Example 1: while loop")
while count < 5:
    print("Current count:", count)
    print("Executing the code inside the while loop")
    count += 1
print("Exited the while loop\n")

# Example 2: for statement + in operator
# The "for" statement with the "in" operator allows you to iterate over a sequence
# and execute a block of code for each item in the sequence.
fruits = ["apple", "banana", "orange"]
print("Example 2: for statement + in operator")
for fruit in fruits:
    print("Current fruit:", fruit)
    print("Processing the current fruit inside the for loop")
print("Exited the for loop\n")

# Example 3: break and continue statements
# The "break" statement allows you to exit a loop prematurely, while the "continue"
# statement allows you to skip the rest of the current iteration and move to the next one.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Example 3: break and continue statements")
for num in numbers:
    print("Current number:", num)
    if num == 5:
        print("Encountered the number 5. Breaking out of the loop.")
        break  # Exit the loop when num is equal to 5
    if num % 2 == 0:
        print("Encountered an even number. Skipping the rest of the iteration.")
        continue  # Skip the rest of the iteration when num is even
    print("Processing the current number inside the loop")
print("Exited the for loop")
