# Python Basics
![Python Basics](images/python.webp)

Welcome to the "python-basic" repository! This repository aims to provide a comprehensive guide to Python's main concepts and usage. Whether you are a beginner getting started with Python or an experienced developer looking to refresh your Python skills, this repository is designed to be your go-to resource.

## Table of Contents

- [00. Main](#00-main)
- [01. Variables](#01-variables)
- [02. Data Types](#02-data-types)
- [03. Operators](#03-operators)
- [04. Control Statements](#04-control-statements)
- [05. Loops](#05-loops)
- [06. Strings and Characters](#06-strings-and-characters)
- [07. Lists](#07-lists)
- [08. Tuples](#08-tuples)
- [09. Dictionaries](#09-dictionaries)
- [10. Slicing and Indexing](#10-slicing-and-indexing)
- [11. Functions](#11-functions)
- [12. Object-Oriented Programming (OOP)](#12-object-oriented-programming-oop)
  - [12.A OOP Intro](#12a-oop-intro)
  - [12.B Diving Deep into Classes and Objects](#12b-diving-deep-into-classes-and-objects)
  - [12.C Diving Deep into Encapsulation](#12c-diving-deep-into-encapsulation)
  - [12.D Diving Deep into Public And Private Method](#12d-diving-deep-into-public-and-private-method)
  - [12.E Diving Deep into Inheritance](#12e-diving-deep-into-inheritance)
  - [12.F Using Super()](#12f-using-super)
  - [12.G Composition and Aggregation](#12g-composition-and-aggregation)
  - [12.I Polymorphism and Overloading Operators](#12i-polymorphism\-and-overloading-operators)
- [13. Create and Import Modules](#13-create-and-import-modules)
- [14. Errors and Errors' Handling](#14-errors)
- [15. Exceptions' Handling](#15-exceptions-handling)
- [16. Input/Output File Handling](#16-inputoutput-file-handling)
- Projects
  - [17. Multiple Face Detection](#17-multiple-face-detection)
  - [18. Random Password Generator](#18-random-password-generator)
  - [19. Pandas Overview](#19-pandas-overview)
  - [20. Coinmarketcap API](#20-cinmarketcap-api)
  - [21. Tkinter Portfolio App](#21-tkinter-portfolio-app)
- [Additional Resources](#additional-resources)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Preface:

Hey there! I'm in the process of learning Python and this repo is my notepad and guidebook rolled into one.
Firstly, it's my personal journey. Starting from square one and gradually tackling more complicated stuff, I'm tracking my progress right here. It's all about learning, problem-solving, and growing as a coder.
Python is like a Swiss Army knife of coding languages - it's versatile and popular in so many fields, from machine learning to web development. The aim of this repo is to cut through the noise and get down to the nitty-gritty basics of Python in a way that's easy to understand, no matter your experience level.
Secondly, I'm hoping this repo can be a helpful resource for others too. Whether you're just kicking off your Python adventure or looking to firm up your understanding, I hope the stuff I've got here can give you a bit of a leg up.
So, let's get stuck into this Python learning journey together, shall we?

### Getting Started

Before diving into the content, make sure you have the latest version of Python installed on your computer. If not, visit the [official Python website](https://www.python.org/downloads/) to download and install Python. You may also want to have a code editor installed. Some popular options include [VS Code](https://code.visualstudio.com/download), [Sublime Text](https://www.sublimetext.com/3), and [PyCharm](https://www.jetbrains.com/pycharm/download/).
### Python Naming Convention (Classes, Variables, Functions, Methods...)

The Python Naming Convention topic covers the guidelines and best practices for naming various elements in Python, such as classes, variables, functions, methods, constants, and modules. Following consistent naming conventions improves code readability and maintainability, making it easier for developers to understand and collaborate on Python projects.

#### Classes:

- Class names should use the `PascalCase` naming convention, where each word starts with an uppercase letter and there are no underscores between words.
- Class names should be descriptive and indicate the purpose or nature of the class. For example, `Car`, `Person`, or `Rectangle`.

```python
class MyClass:
    pass
```

#### Variables:

Variable names should use lowercase letters and words should be separated by underscores (`snake_case`).
Variable names should be descriptive and indicate the purpose or content of the variable. For example:

```python
my_variable = 42
name = "John Doe"
```
#### Functions and Methods:

- Function and method names should use lowercase letters and words should be separated by underscores (`snake_case`).
- Function and method names should be descriptive and indicate the action or purpose of the function or method. For example:

```python
def calculate_area(length, width):
    return length * width

def print_message(message):
    print(message)
```

#### Constants:

- Constants are variables that have fixed values and are not meant to be changed.
- Constant names should use uppercase letters and words should be separated by underscores (`UPPER_CASE`).
- Constants should be declared at the module level and should have a meaningful name that reflects their purpose. For example:

```python
PI = 3.14159
MAX_VALUE = 100
```

#### Modules:

- Module names should use lowercase letters and words should be separated by underscores (`snake_case`).
- Module names should be short, meaningful, and describe the purpose of the module. For example:

```python
import math_utils
import string_operations
```

---

It's important to note that these naming conventions are not enforced by the Python interpreter but are widely adopted by the Python community to promote consistency and readability in code. Adhering to these conventions makes your code more understandable to others and helps maintain a clean and uniform coding style.

Following these conventions also aligns with the recommendations outlined in the official Python style guide, known as PEP 8. It's highly recommended to review the full PEP 8 style guide for further details on naming conventions and other aspects of Python coding style.

---

## 00. Main
The main section provides an overview and introduction to the repository. It explains the purpose of the repository, which is to serve as a comprehensive learning resource for Python. The repository covers Python's main concepts and usage to help readers gain a solid understanding of the language. The content in this section sets the foundation for the topics covered in subsequent sections.

---

## 01. Variables
The Variables section covers the concept of variables in Python, a fundamental concept in programming. It explains what variables are, how to declare and assign values to variables, and their usage. This section provides a detailed explanation of variable naming conventions, variable types, and examples of how to use variables in Python programs. It also covers variable scoping and the differences between global and local variables.

---

## 02. Data Types
The Data Types section explores the various built-in data types in Python, which include numbers, strings, lists, tuples, dictionaries, and more. It provides a comprehensive explanation of each data type, including their characteristics, how to create instances of these data types, and common operations or methods associated with them. This section also discusses type conversion and type checking in Python.

---

## 03. Operators
The Operators section discusses the different types of operators in Python, which include arithmetic, comparison, logical, assignment, and more. It covers the syntax and usage of each operator, providing examples to illustrate their behavior. This section also explains operator precedence and associativity to help readers understand how operators are evaluated in expressions.

---

## 04. Control Statements
The Control Statements section explains the usage of control statements in Python, including if, if-else, and nested if statements. It covers the syntax and structure of control statements, including the use of conditional expressions and logical operators. This section provides examples to demonstrate the flow of control in different scenarios and highlights the importance of indentation in Python to define code blocks.

---

## 05. Loops
The Loops section covers the use of loops in Python, which include while loops and for loops. It explains the syntax and usage of each type of loop, providing examples to illustrate how they can be used to iterate over sequences or perform repetitive tasks. This section also introduces the `in` operator and demonstrates its use in conjunction with loops. Additionally, it covers the break and continue statements to control the flow of the loop.

---

## 06. Strings and Characters
The Strings and Characters section delves into working with strings in Python. It covers string manipulation, including concatenation, formatting, and common string methods such as `split()`, `join()`, `lower()`, `upper()`, and more. This section also explains string indexing and slicing to extract specific characters or substrings from strings. It covers string formatting techniques using placeholders or f-strings and introduces regular expressions for advanced string manipulation.

---

## 07. Lists
The Lists section focuses on lists in Python, which are versatile and commonly used data structures. It covers list creation, accessing elements, modifying lists, and using built-in list methods. This section explains the syntax for creating lists, accessing individual elements or sublists using indexing and slicing, and modifying lists using methods such as `append()`, `insert()`, `remove()`, and more. It also covers list comprehensions and techniques for working with nested lists.

---

## 08. Tuples
The Tuples section explores tuples in Python, which are immutable sequences. It covers tuple creation, accessing elements, modifying tuples, and using built-in tuple methods. This section explains the syntax for creating tuples, accessing elements using indexing, and the immutability of tuples. It covers tuple packing and unpacking, tuple assignment, and methods such as `count()` and `index()` for tuple manipulation. Additionally, it discusses the advantages of using tuples compared to other data structures.

---

## 09. Dictionaries
The Dictionaries section explains dictionaries in Python, which are key-value pairs and provide efficient data retrieval. It covers dictionary creation, accessing elements, modifying dictionaries, and using dictionary methods. This section explains the syntax for creating dictionaries, accessing elements using keys, adding, updating, or removing key-value pairs, and utilizing dictionary methods such as `keys()`, `values()`, `items()`, and more. It also discusses dictionary comprehension and techniques for working with nested dictionaries.

---

## 10. Slicing and Indexing
The Slicing and Indexing section demonstrates how to index and slice sequences like strings, lists, and tuples in Python. It covers the concept of indexing and slicing, explaining the syntax and providing examples of extracting specific elements or substructures from sequences. This section also introduces negative indexing to access elements from the end of a sequence. Additionally, it explores advanced slicing techniques like specifying step size and using slicing to create new sequences.

---

## 11. Functions
The Functions section covers the concept of functions in Python, which allow you to encapsulate reusable blocks of code. It explains how to define and use functions, including parameters, arguments, and return values. This section covers different types of arguments, such as positional arguments, keyword arguments, variable-length arguments, and keyword variable-length arguments. It also discusses local and global variables, explaining their scope and how to modify global variables within functions.

---

## 12. Object-Oriented Programming (OOP)
The Object-Oriented Programming (OOP) section covers the fundamental principles of OOP in Python. It explores topics such as classes, objects, inheritance, encapsulation, and polymorphism. This section provides a deeper understanding of OOP concepts and demonstrates how to design and implement object-oriented solutions in Python.

- ### 12.A OOP intro
   This file provides an introduction to OOP in Python. It explains the core concepts of OOP, including classes, objects, attributes, and methods. It demonstrates how to define classes and create objects from them. It also discusses the concepts of inheritance, encapsulation, and polymorphism, providing practical examples to illustrate their usage.

- ### 12.B Diving Deep into Classes and Objects
   This file delves deeper into the concepts of classes and objects in Python. It explores topics such as class constructors, instance variables, class variables, instance methods, class methods, and static methods. It provides examples and explanations to help readers understand how to work with these different aspects of classes and objects.

- ### 12.C Diving Deep into Encapsulation
   This file explores the concept of encapsulation in Python. It explains the importance of encapsulation for data hiding and abstraction. It discusses access modifiers such as public, protected, and private and demonstrates how to use them to control access to class members. It also provides examples to showcase the benefits of encapsulation in maintaining code integrity and enhancing code maintainability.

- ### 12.D Diving Deep into Public And Private Method
   This file delves deeper into the concept of public and private methods in Python classes. It explains the difference between public and private methods and their significance in encapsulation. It demonstrates how to define private methods using naming conventions and showcases the advantages of using private methods in terms of code organization and readability.

- ### 12.E Diving Deep into Inheritance
   This file explores the concept of inheritance in Python. It explains how to create subclasses by inheriting properties and methods from parent classes. It covers topics such as single inheritance, multiple inheritance, method overriding, and method resolution order. It provides examples to demonstrate how inheritance can be used to create hierarchical relationships between classes and promote code reuse.

- ### 12.F Using Super()
   This topic covers how to use the `super()` function in Python to invoke methods from parent classes. It explains the concept of method resolution order (MRO) and demonstrates how to use `super()` to call the `__init__` method of parent classes. It provides an example that showcases the usage of `super()` to achieve method overriding and maintain the correct order of method execution in a class hierarchy.

- ### 12.G Composition and Aggregation
  #### Composition
  Composition is a fundamental concept in object-oriented programming (OOP). It embodies a class relationship where one class (the _composite_ or _container_ class) incorporates an instance of another class (the _component_ or _content_ class). In this relationship, the composite class oversees the creation and lifecycle of the component class.
  The component class is part of the composite class, implying that the composite class is often not functional without the component class.
  #### Aggregation
  Aggregation is another type of object-oriented class association. Here, one class (_aggregator_) contains a reference to an instance of another class (the _part_). However, in this relationship, the aggregator does not manage the lifecycle of the part class. 
  The part class is associated with the aggregator, but they maintain their own lifecycles, implying that the part can exist independently of the aggregator. Hence, the relationship is sometimes described as a "has-a" relationship (the aggregator _has a_ part).
  #### Differences
  The crucial difference between composition and aggregation lies in the level of dependency between the classes. In composition, the composite class and component class are tightly coupled as the composite class manages the lifecycle of the component class, implying a higher level of dependency.
  In contrast, in aggregation, the aggregator and part classes are loosely coupled. The aggregator class has a reference to the part class, but does not manage its lifecycle, indicating a lower level of dependency.

- ### 12.H Abstract Classes
  In Python, abstract classes serve as "blueprints" for other classes. They are defined using the `abc` module. An abstract class can contain both regular methods (with implementation) and abstract methods (without implementation).
  An abstract method is defined by the decorator `@abstractmethod` and contains no implementation. This decorator indicates that the method must be implemented by any non-abstract child class.
  Attempting to create an instance of an abstract class results in an error. Instead, the abstract class should be subclassed, and at least all of its abstract methods should be implemented. 
  This mechanism can be used to ensure that a class adheres to a certain interface, or in other words, that it includes particular methods with specific parameters. 
  This means, when you define a child class from an abstract base class, the child class must provide the concrete implementation for all the abstract methods defined in the abstract base class. 

- ### 12.I Polymorphism and Overloading Operators
  Polymorphism in Python demonstrates how a function can behave differently depending on the form of the object it interacts with. In simple words, it allows the same operation to work differently with various types of objects.
  Python enables operator overloading, which is a fantastic example of polymorphism. Operator overloading allows the same operator to exhibit different behavior based on the context. 
  In the `Doc` class we've created, which represents a document with a certain number of pages, we've overloaded the "*", and ">" operators. This means these operators can now interact not just with standard types like integers but with our `Doc` objects too!
  Now, the "*" operator returns the product of the page counts of two `Doc` objects. The ">" operator allows us to compare if one document is larger than another based on their page count.
  Remember, if you're working with different classes, you'll need to define these special methods (`__mul__`, `__gt__`) in those classes as well. Happy coding!

---

## 13. Create and Import Modules
This topic covers how to create and import modules in Python. Modules allow you to organize your code into separate files, making it easier to manage and reuse. It explains the process of importing modules using the `import` statement and demonstrates how to use functions and classes from imported modules. It also covers refactoring code with modules to improve code organization and reusability. 

---

## 14. Errors
In programming, we generally categorize errors into three types: Compile-time, Run-time, and Logical Errors.

* **Compile-Time Errors:** These errors are usually syntax or semantics mistakes that cause the compiler to raise an error. Examples can include missing colons or indentation errors in Python.

* **Run-Time Errors:** Also known as exceptions (when handled), these errors occur during the execution of the program. They can lead to program crashes and can sometimes be hard to track down. Examples include out of memory errors, trying to open a file that doesn't exist, or attempting to divide by zero.

* **Logical Errors:** These errors occur when the program's logic is flawed. This often results from a misunderstanding of the problem you're trying to solve or poor design decisions. The program runs without crashing, but it doesn't produce the expected result. This can make logical errors particularly hard to identify and fix.

The goal of effective error handling is to anticipate potential sources of errors and handle them gracefully, avoiding program crashes and ensuring that your code behaves predictably even in the face of unexpected conditions.

---

## 15. Exceptions' Handling
Dealing with errors is a critical part of programming, and Python provides several tools for handling exceptions, which are essentially runtime errors. Here, we categorize exceptions as either built-in or user-defined.

* **Built-in Exceptions:** Python has a variety of built-in exception classes that get raised when certain errors occur during the execution of your program. Examples include `ZeroDivisionError`, `TypeError`, `ValueError`, and many more. Python's `try/except` blocks are used to catch and handle these exceptions. If the code inside a `try` block causes an exception to be raised, that exception is caught and the corresponding `except` block is executed.

* **User-Defined Exceptions:** You can also define your own exception classes in Python, which can be useful if you want to raise and catch errors that are specific to your application's domain. To define a custom exception, you typically create a new class that inherits from the base `Exception` class. You can then raise your custom exception with the `raise` statement.

* **Else and Finally Clauses:** Besides `try` and `except`, Python's exception handling mechanism also includes `else` and `finally` clauses. The `else` clause lets you specify a block of code that will be executed if the `try` block does not raise an exception, while the `finally` clause lets you specify a block of code that will be executed no matter what - whether an exception is raised or not. This can be useful for cleanup activities that should always be performed, like closing a file or a network connection.

Overall, handling exceptions properly is a crucial part of writing robust, reliable Python code. It helps you deal with unexpected situations and ensures that your program doesn't crash when it encounters an error.

---

## 16. Input/Output File Handling
Working with files is a common task in programming, and Python provides robust facilities for file handling, which includes reading from and writing to files.

Here are the basic steps for working with files in Python:

1. **Open the file**: Use the built-in `open()` function, specifying the filename and the mode as arguments. The mode can be 'r' (read), 'w' (write), 'a' (append), or a combination of these.

2. **Perform operations on the file**: Once the file is open, you can read from it (if it was opened in read mode) or write to it (if it was opened in write or append mode). You read from a file with the `read()`, `readline()`, or `readlines()` method, and write to a file with the `write()` method.

3. **Close the file**: After you're done with a file, it's important to close it using the `close()` method. This frees up system resources.

In addition to the standard way of handling files (open, operate, close), Python provides a shortcut using the `with` statement. This automatically takes care of closing the file once you're done with it, even if exceptions occur within the `with` block.

Overall, Python's file handling capabilities make it easy to work with data stored in files. You can easily read data from files for processing, and write processed data back to files for storage.

---

# Projects

## 17. Multiple Face Detection
This section introduces an important concept in image processing and computer vision: multiple face detection. The implementation involves the OpenCV library, a powerful tool for computer vision tasks, and the Haar Cascade classifier, a machine learning-based approach for object detection.

- **Face Detection and OpenCV:**
Face detection refers to identifying and locating faces in a given image. This technique is commonly used in various applications including surveillance, facial recognition software, and even on social platforms for tagging friends. Here are some useful resources for further understanding:
  - [OpenCV Face Detection: Visual Guide](https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/)
  - [Face Detection using Haar Cascades](https://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html)

- **Haar Cascade Classifier:**
The Haar Cascade is a classifier primarily used for object detection. Trained with numerous positive and negative images, the classifier is capable of detecting objects in images or video streams. The Haar Cascade implemented within OpenCV is mainly used for face detection, but it can be adjusted for any object detection.
 
In this project:

**1. Importing Libraries:**
The script begins by importing the required libraries, `cv2` for computer vision tasks and `glob` for retrieving file pathnames.

**2. Initialize the Haar Cascade Classifier:**
The Haar Cascade face detector, provided by OpenCV, is initialized.

**3. Define Maximum Image Size:**
A maximum size is set for the largest dimension (width or height) of an image.

**4. Image Retrieval and Iteration:**
The script retrieves all `.png` images within the current directory. It then iterates through each image.

**5. Image Scaling:**
If an image's width or height exceeds the maximum size, the image is scaled down while maintaining its aspect ratio.

**6. Grayscale Conversion:**
Each image is converted to grayscale. The Haar Cascade face detector primarily works with grayscale images.

**7. Contrast Enhancement:**
Histogram equalization is applied to the grayscale image, enhancing its contrast and facilitating face detection.

**8. Noise Reduction:**
Gaussian blur is applied to the grayscale image, reducing its noise and enhancing face detection efficiency.

**9. Face Detection:**
Face detection is performed using the Haar Cascade face detector. It adjusts the scaleFactor and minNeighbors parameters based on the image.

**10. Face Identification:**
For each detected face, a rectangle is drawn on the original color image to visually identify the face's location.

**11. Image Display and Transition:**
Each processed image is displayed for 2000 ms before transitioning to the next image. After each display, the image window is closed to prepare for the next image.

---

## 18. Random Password Generator
This section delves into the implementation of a random password generator, a fundamental tool in data security and privacy. In modern technology, passwords are essential for user authentication and protection of sensitive data. However, creating a strong password that's hard to crack, yet easy to remember, can be a daunting task. That's where a random password generator comes in. This program demonstrates how to use Python to generate random passwords.

The examples provided here showcase two ways to create a random password generator:

1. **Using Random Choices From Defined Lists:** The first example constructs a password by combining randomly selected elements from predefined lists. This includes upper case letters, lower case letters, numbers, and special characters. The `random` module in Python provides functions like `random.choice()`, `random.randint()`, and `random.random()` that are used to select these random elements.

2. **Readable Password Generator Using Text Files:** The second example creates a password that's easier to remember, yet maintains complexity. This method reads words from a text file, capitalizes words that are longer than five characters, and combines a randomly chosen word with a special character and a two-digit number. The generated password, while still random, will be more readable and memorable for the user.

These password generators demonstrate the versatility of Python and the power of the `random` module. By simply adjusting parameters or changing the method of generation, you can create a password that fits specific security requirements or personal preferences.

For additional knowledge on random number generation in Python, consider the following resources:
- [Python random module](https://docs.python.org/3/library/random.html)
- [Generating Random Data In Python](https://realpython.com/python-random/)

---

## 19. Pandas Overview

In this section, we will be providing an overview of Pandas, a powerful and versatile library for data manipulation and analysis in Python. It introduces DataFrames, which are two-dimensional, size-mutable, heterogeneous tabular data structures with labeled axes.

**1. Introduction to Pandas:**
- Pandas, built on the Numpy package, primarily uses a data structure known as a DataFrame. DataFrames are basically multi-dimensional arrays with attached row and column labels, capable of holding heterogeneous data types.

**2. Creating DataFrames:**
- DataFrames can be created from lists, with each sub-list representing a row in the DataFrame, or dictionaries, where the keys become column names and their corresponding values form the data for those columns.

**3. Operations on DataFrame Columns:**
- Various operations can be performed on DataFrame columns, such as retrieving the maximum value in a column. Furthermore, DataFrame objects possess numerous methods and attributes that can be used to manipulate and analyze the data.

**4. Reading Data from Various Formats:**
- The Pandas library is versatile in reading data from a wide variety of formats including CSV, Excel, and JSON files, all of which can be read into DataFrames.

**5. Slicing the DataFrame:**
- Pandas offers powerful slicing functionalities. The `.loc` method allows slicing by labels, while the `.iloc` method slices based on integer indexes.

**6. Modifying the DataFrame:**
- Columns can be removed or added from/to the DataFrame with ease. Additionally, operations can be performed directly on DataFrame columns.

**7. Transposing the DataFrame:**
- The DataFrame can be transposed, i.e., switching the rows and columns, using the `.T` attribute. New columns can be added to the transposed DataFrame in a similar manner to the original DataFrame.

---

## 20. Coinmarketcap API
This script helps users track the profit or loss of their cryptocurrency investments. It provides a high-level snapshot of the performance of the user's portfolio, based on the latest market prices. It first fetches the top 5 latest cryptocurrencies from the CoinMarketCap API, then it goes through the user's portfolio (defined in the 'coins' list) to see if the user has any of these top cryptocurrencies. If a match is found, it calculates the current market value of the user's holding in that cryptocurrency as well as the profit or loss since the user's investment. Finally, it adds up all the profits and losses across all cryptocurrencies in the user's portfolio to present the total profit or loss. This tool is useful for users to stay informed about their cryptocurrency investments and make informed decisions based on the latest market data.

1. **API Request**
    - An API request is made using the requests library. The request is made to the CoinMarketCap API, with parameters to get the latest 5 cryptocurrencies, converted to USD.

2. **Parsing JSON Data**
    - The json.loads() function is used to parse the JSON content from the API response.

3. **Printing Cryptocurrency Details**
    - Printing the symbol and price of the first cryptocurrency in the list.

4. **Defining Your Portfolio**
    - A list of coins that you own, with details such as the symbol of the coin, the amount you own, and the price you paid per coin.

5. **Calculating Total Profit/Loss**
    - Initializing the total profit/loss variable.
    - Looping through the first 5 cryptocurrencies in the API response and your list of owned coins to calculate the total profit/loss.

6. **Printing Total Profit/Loss**
    - Print the total profit/loss for the entire portfolio.

### Running the Script
Replace "YOUR_API_KEY" with your actual API key from CoinMarketCap for the API calls to work. Run the script and check your profit or loss based on the current prices of cryptocurrencies.

---

## 21. Tkinter App GUI for Portfolio visualization
This project involves using the CoinMarketCap API to fetch and display data about cryptocurrencies in a GUI.

1. **Import Libraries**
    - Import necessary libraries like Tkinter, Requests, and Json.

2. **Define Helper Functions**
    - `font_color()`: Determines the color of the font based on whether a value is positive or negative.
    - `my_portfolio()`: Makes a request to the CoinMarketCap API, calculates profits or losses for each coin in your portfolio, and displays this information in the GUI.

3. **Setup GUI using Tkinter**
    - Instantiate the main window, set title and (optional) icon.
    - Define and grid headers for each column in the portfolio: Coin Name, Price, Coin Owned, Total Amount Paid, Current Value, P/L per coin, Total P/L with coin.
    - Call `my_portfolio()` function to fetch and display data in the GUI.

4. **Run the Application**
    - Start the main Tkinter event loop.
    - Print line separator in the console.

5. **Notes for Deployment**
    - Install `pyinstaller` using pip for packaging the script into an executable.
    - Substitute your own API key in the REST API endpoint searchParams.
    - Create an executable using `pyinstaller --windowed --name=MyApp main.py`.
    - Run the executable to start the application.



This section focuses on fetching and analyzing cryptocurrency data using the CoinMarketCap API. It includes interacting with the API, parsing JSON responses, and using the data to compute profit or loss for a cryptocurrency portfolio.

**1. Libraries Used:**
- 'requests': This library is used for making HTTP requests in Python.
- 'json': This library is used for parsing JSON strings and converting Python data structures to JSON format.

**2. API Request:**
- An API request is sent to CoinMarketCap API to fetch the latest 5 cryptocurrencies data.

**3. Parsing JSON Response:**
- The JSON response received from the API is parsed and used to extract cryptocurrency information.

**4. Displaying Cryptocurrency Details:**
- The symbol and price of the first cryptocurrency in the list are printed out.

**5. Cryptocurrency Portfolio:**
- A portfolio of owned cryptocurrencies is defined, containing information such as symbol, amount owned, and the price paid per coin.

**6. Calculating Profit/Loss:**
- For each cryptocurrency in the portfolio, if the symbol matches with any of the top 5 cryptocurrencies fetched from the API, the total amount paid for the coin, current value, profit/loss per coin, and total profit/loss for this coin are calculated and printed.

**7. Portfolio Performance:**
- The total profit/loss for all coins in the portfolio is calculated and printed, providing a high-level snapshot of the portfolio's performance.

---

## 21. Tkinter Portfolio App

---

## Additional Resources

For those looking to delve deeper into Python, here are some additional resources:

- [Official Python Documentation](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Codecademy Python Course](https://www.codecademy.com/learn/learn-python-3)

## Contributing

Contributions to this repository are more than welcome! Here's a simple guide on how you can contribute:

1. Fork this repository
2. Clone your forked repository to your local machine
3. Create your feature branch: `git checkout -b feature/YourFeatureName`
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature/YourFeatureName`
6. Submit a pull request

## Contact

If you have any questions, suggestions, or just want to connect, feel free to reach out:

- Twitter: [AndreaSeverini](https://twitter.com/AndreSeverini)

Happy coding and enjoy learning Python!
