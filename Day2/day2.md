
Day 2: Basic Python Syntax 🐍
Python Indentation and Comments 💬

In Python, indentation is not just for readability; it is crucial for the functionality of the code. It is used to determine the grouping of statements.

Let's consider the following example:

def greet(name):
    print(f"Hello, {name}!")  # The line with the print statement is indented with four spaces.

greet("Alice")  # No indentation here because this is not inside a function.

Comments are lines that exist in computer programs but are not executed. They are very useful for the person who is reading the code. In Python, anything written after the # symbol on the same line is considered a comment and is ignored by Python when running the code.

#### # This is a comment. Python will ignore it when running the code.
print("Hello, World!")  # This is also a comment.

     
Exercise

    Write a function called multiply that takes two arguments and returns their product. Make sure to use proper indentation. (To be done by the teacher)

    Write comments explaining what your function does, and what each line of code inside it does.





Notebook 2: Python Statements, Line Continuation, and Quotations 📃

# Python Statements, Line Continuation, and Quotations 📃

In Python, a statement is a unit of code that the Python interpreter can execute. For instance, `a = 1` is an assignment statement. 

If the statement is long, we can break it into multiple lines with the line continuation character (\\).

```python
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a)  # Will print the sum from 1 to 9.

Python allows the use of single quotes ('), double quotes ("), and triple quotes (''' or """) to denote a string.

# All of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

     

The above will produce the same output
Exercise

    Write a long mathematical expression (at least five operations) and split it over multiple lines using the line continuation character (\\).

    Create three strings, one with single quotes, one with double quotes, and one with triple quotes. Make sure each string contains at least one apostrophe (').



Notebook 3: Python Variables and Data Types 🔢

# Python Variables and Data Types 🔢

Variables are containers for storing data values. In Python, a variable is created the moment you first assign a value to it.

```python
x = 5
y = "Hello, World!"

Python has various data types. Here are a few common ones: integers, float (real numbers), string (text), list (an ordered collection of items), tuple (an ordered, immutable collection of items), and dictionary (an unordered collection of data in a key:value pair form).

# Integer
x = 5
print(type(x))

# Float
y = 5.0
print(type(y))

# String
z = "Hello"
print(type(z))

# List
a = [1, 2, 3, 4]
print(type(a))

# Tuple
b = (1, 2, 3, 4)
print(type(b))

# Dictionary
c = {"one": 1, "two": 2, "three": 3}
print(type(c))

     
Exercise

    Create the following variables and print their types:
        An integer named my_int
        A float named my_float
        A string named my_string
        A list named my_list
        A tuple named my_tuple
        A dictionary named my_dict

    Check the type of each variable to make sure it matches what you expect.

