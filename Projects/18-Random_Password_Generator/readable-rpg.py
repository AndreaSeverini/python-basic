# READABLE PASSWORD GENERATOR
# Import the random module to generate random selections and numbers
import random

# Define a list of special characters that will be included in the password
special = ['|', '!', '$', '%', '&', '/', '=', '?', '^', '*', '_', '-']

# Initialize an empty list to store the eligible words from the text file
w_list = []

# Open the text file in read mode
with open("text.txt", 'r') as txt:
    # Read all lines from the file into the 'data' variable
    data = txt.readlines()

    # Iterate over each line in 'data'
    for line in data:
        # Split each line into individual words and iterate over them
        words = line.split()
        for item in words:
            # If a word is longer than 5 characters, capitalize it and add it to 'w_list'
            if len(item) > 5:
                w_list.append(item.capitalize())

# Choose a random word from 'w_list'
word = random.choice(w_list)

# Choose a random special character from the 'special' list
sc = random.choice(special)

# Generate a random two-digit number and convert it to a string
num = str(random.randint(10, 99))

# Combine the chosen word, special character, and number to create the password
password = word + sc + num

# Print the generated password
print(password)

# This script reads words from a text file and creates a password composed of:
# 1) a capitalized word that is more than 5 characters long,
# 2) a special character,
# 3) a two-digit number.
# The words are read from the text file, and those that are longer than 5 characters
# are capitalized and stored in 'w_list'. One word is then randomly chosen from this list.
# A special character is also randomly chosen from the 'special' list.
# The two-digit number is generated using the random.randint() function.
# The password is then printed to the console.


