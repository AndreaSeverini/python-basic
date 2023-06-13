# INTRODUCTION


# The three important functions are random.random(), random.randint(), random.choice()
# They are useful to get random values or to randomly choice from different items

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(random.choice(numbers))

print(random.randint(1, 9))  # both number included

print(random.randint(100000, 999999))  # random OTP example

print(random.random())  # floating point number in the range [0.0, 1.0)

# Import the random module to use its functions for generating random numbers
import random

# Define a list of uppercase letters
upper = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
         'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
         'Z', 'X', 'C', 'V', 'B', 'N', 'M']

# Define a list of lowercase letters
lower = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
         'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
         'z', 'x', 'c', 'v', 'b', 'n', 'm']

# Define a list of numbers
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Define a list of special characters
special = ['|', '!', '$', '%', '&', '/', '=', '?', '^',
           '*', '_', '-']

# Generate the password by randomly selecting one character from each list
# Here, random.choice() is used to select a random item from the list
# '+' operator is used to concatenate the randomly selected characters into a single string
password = random.choice(upper) + random.choice(lower) + random.choice(num) + random.choice(special) \
           + random.choice(upper) + random.choice(lower) + random.choice(num) + random.choice(special)

# Print the generated password
print(password)
