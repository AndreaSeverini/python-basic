# INPUT/OUTPUT FILE HANDLING

# 1. Open file
file_handler = open('example.txt', 'w')  # Open the file in write mode (if it doesn't exist, it will be created)

# 2. Perform operations on the file (create, store, retrieve, and delete)
file_handler.write('I am adding a line')  # Write a line to the file

# 3. Close file
file_handler.close()  # Close the file

# Example 2

fh = open('example.txt', 'w')  # Open the file in write mode

for i in range(1, 11):
    fh.write('%d \n' % i)  # Write numbers 1 to 10 to the file, each on a new line

# 3. Close file
fh.close()  # Close the file

# APPENDING

fh = open('example.txt', 'a')  # Open the file in append mode (without deleting existing content)

try:
    for i in range(1, 11):
        fh.write('%d \n' % i)  # Append numbers 1 to 10 to the file, each on a new line
finally:
    fh.close()  # Close the file, ensuring it is closed even if an error occurs

# PYTHON SHORTCUT

# Same operations as before, but using a more concise syntax

with open('demo.txt', 'w') as fh:  # Open the file in write mode using a 'with' statement
    for i in range(1, 11):
        fh.write('%d \n' % i)  # Write numbers 1 to 10 to the file, each on a new line

# READING FROM A FILE

fh_read = open('demo.txt', 'r')  # Open the file in read mode

# print(fh_read.read(3))  # Read up to 3 characters from the file
# print(fh_read.read(10))  # Read from the 3rd to the 13th character from the file

print(fh_read.readline())  # Read a single line from the file
print(fh_read.readlines())  # Read all lines from the file and return them as a list
print(len(fh_read.readlines()))  # Read the number of lines in the file
# print(fh_read.readlines()[0])  # Read the first line at the current pointer position

for line in fh_read:
    print(line)  # Iterate through the lines of the file and print each line

for line in fh_read:
    print(line.split(' '))  # Split each line into a list of words

fh_read.close()  # Close the file

# In this example, we demonstrate input/output file handling in Python.

# To work with files, we follow the following steps:
# 1. Open the file using the `open()` function, specifying the file name and the mode ('r' for read, 'w' for write, 'a' for append, etc.).
# 2. Perform operations on the file, such as writing data to the file using the `write()` method.
# 3. Close the file using the `close()` method to free up system resources.

# In the first part of the code, we open the 'example.txt' file in write mode and write a line of text to it using the `write()` method. Then we close the file.

# In the second part, we open the 'example.txt' file in write mode and use a loop to write numbers 1 to 10 to the file
