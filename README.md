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
- [13. Create and Import Modules](#13-create-and-import-modules)
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
  ### Composition
  Composition is a fundamental concept in object-oriented programming (OOP). It embodies a class relationship where one class (the _composite_ or _container_ class) incorporates an instance of another class (the _component_ or _content_ class). In this relationship, the composite class oversees the creation and lifecycle of the component class.
  The component class is part of the composite class, implying that the composite class is often not functional without the component class.
  ### Aggregation
  Aggregation is another type of object-oriented class association. Here, one class (_aggregator_) contains a reference to an instance of another class (the _part_). However, in this relationship, the aggregator does not manage the lifecycle of the part class. 
  The part class is associated with the aggregator, but they maintain their own lifecycles, implying that the part can exist independently of the aggregator. Hence, the relationship is sometimes described as a "has-a" relationship (the aggregator _has a_ part).
  ### Differences
  The crucial difference between composition and aggregation lies in the level of dependency between the classes. In composition, the composite class and component class are tightly coupled as the composite class manages the lifecycle of the component class, implying a higher level of dependency.
  In contrast, in aggregation, the aggregator and part classes are loosely coupled. The aggregator class has a reference to the part class, but does not manage its lifecycle, indicating a lower level of dependency.

---

## 13. Create and Import Modules
This topic covers how to create and import modules in Python. Modules allow you to organize your code into separate files, making it easier to manage and reuse. It explains the process of importing modules using the `import` statement and demonstrates how to use functions and classes from imported modules. It also covers refactoring code with modules to improve code organization and reusability. 

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
