
Day 3: Python Variables and Assignment Statements 🌟🎉🚀

Hello, Pythonista! 🎉👨‍💻👩‍💻 Welcome to Day 3 of the 30 days of Python code challenge. Today, we will delve into Python variables and assignment statements. Let's get started!
Python Variables 📚

A variable in Python is like a container in the computer's memory where we can store a single value. If you want to use text in Python, you have to use a text string. A text string is a sequence of characters enclosed in quotes. You can use single or double quotes:

Example:

# Assigning a string to a variable message = "Hello, Python!" print(message)

In Python, you can also assign a number (integer and float) to a variable:

# Assigning an integer to a variable age = 20

# Assigning a float to a variable pi = 3.14
Assignment Statements 📝

An assignment statement creates a new variable and gives it a value. Here's an example:

# Assignment statement number = 3

Here, number is a variable, and 3 is the value assigned to it.

Python also allows you to assign values to multiple variables in one line:

# Assigning values to multiple variables a, b, c = 5, 3.2, "Hello"
Variable Names and Keywords 💡

Variable names in Python can be any length and can consist of uppercase and lowercase letters (A-Z, a-z), digits (0-9), and the underscore character (_). They must start with a letter or the underscore character. They cannot start with a number.

Example:

# Valid variable names my_var = 10 _var = "underscore var" Var123 = "Variable with digits"

Python also has a set of keywords that are reserved words that cannot be used as variable names. These keywords are:

# Python Keywords and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield

And here's your small exercise for the day!
Exercise 🏋️‍♀️🤓🎯🏁

    Create three variables: one to store your name, one for your age, and one for your country.

    Then, use the print function to create a sentence about yourself like this:

"I am [Your Name]. I am [Your Age] years old. I'm from [Your Country]."

    Try to create a variable using one of the Python keywords and see the kind of error you get.

Happy Coding! 🚀👩‍💻👨‍💻💻🌟




Day 3 Continued: Python Number and String Data Types 🌟🎉🚀
Number Data Types in Python 🧮

Python supports three types of numbers - int, float, and complex.

int stands for integer. It contains positive or negative whole numbers (without fraction or decimal).

Example:

# Assigning an integer to a variable age = 20

float stands for floating point number. It contains positive or negative decimal numbers.

Example:

# Assigning a float to a variable pi = 3.14

complex numbers are represented in the form x + yj, where x and y are floats and j represents the square root of -1 (which is an imaginary number).

Example:

# Assigning a complex number to a variable complex_number = 3+4j
String Data Type in Python 📝

Strings in Python are identified as a contiguous set of characters represented in the quotation marks.

Example:

# Assigning a string to a variable message = "Hello, Python!"

Python allows for either pairs of single or double quotes.

You can also create multi-line strings using triple quotes (single ''' or double """).

Example:

# Multi-line string about_me = ''' Hello! I'm learning Python. I love it! '''
Type Conversion 🔄

Python allows you to convert data types. The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion.

Example:

# Converting integer to float float_age = float(20)

# Converting float to integer int_pi = int(3.14)

# Converting number to string str_age = str(20)
Exercise 🏋️‍♀️🤓🎯🏁

    Assign your age to a variable as an integer.

    Assign your height to a variable as a float.

    Assign your name to a variable as a string.

    Print your age, height, and name on separate lines.

    Now, convert your age to a float and print it. Then, convert your height to an integer and print it. Try converting your name to an integer and see what happens.

    Write a multi-line string about why you are learning Python and print it.

Happy Coding! 🚀👩‍💻👨‍💻

Day 3 Conclusion: Type Conversion and Interaction 🌟🎉🚀
Type Conversion in Python 🔄

In Python, we can convert one data type to another. We'll cover three primary types of conversion: int, float, and str.

    int(): This function converts a specified value into an integer.

Example:

# Converting float to int x = 3.14 int_x = int(x) print(int_x)

    float(): This function converts a specified value into a floating point number.

Example:

# Converting int to float y = 10 float_y = float(y) print(float_y)

    str(): This function converts a specified value into a string.

Example:

# Converting int to string z = 20 str_z = str(z) print(str_z)

Note: When converting from a float to an int, the number will be rounded down. When converting from a string to an int or float, the string needs to be numerical, or else you'll get an error.
Interaction in Python 🤝

One of the key features of Python is its interactive prompt. You can use the input() function to prompt the user for input. This function reads a line from input, converts it into a string, and returns it.

Example:

# Prompting user for input name = input("What's your name? ") print("Hello, " + name + "!")

Remember that the input() function always returns a string. If you want a numerical value from the user, you'll need to convert that input using int() or float().

Example:

# Prompting user for numerical input age = int(input("How old are you? ")) print("You are " + str(age) + " years old!")
Exercise 🏋️‍♀️🤓🎯🏁

    Prompt the user for two numbers. Convert these numbers to integers and print their sum.

    Prompt the user for their first and last name. Concatenate the names and print a message that says "Hello, [first name] [last name]!"

    Try converting a non-numerical string into an integer and see what kind of error you get.

Remember, errors are part of the learning process! Don't be afraid to make mistakes - they'll help you learn Python better.

Happy Coding! 🚀👩‍💻👨‍💻💻🌟
