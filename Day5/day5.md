
Day 5: For Loops in Python 🌟🎉🚀

Hello, Pythonista! 🎉👨‍💻👩‍💻 Welcome to Day 5 of the 30 days of Python code challenge! Today, we're diving into for loops in Python.
For Loops in Python 🔄

In Python, "for" loops are used for sequential traversal. It falls under the category of definite iteration, meaning that the number of times the loop is executed is defined in advance.

    For loop with Lists:

For loop can iterate over the elements of a given list.

Example:

# Iterating through a list fruits = ['apple', 'banana', 'cherry'] for fruit in fruits: print(fruit)

    For loop with Strings:

Similar to lists, for loop can iterate over the characters of a string.

Example:

# Iterating through a string for letter in 'Pythonista': print(letter)

    For loop with the range() function:

If you need to iterate over a sequence of numbers, the built-in function range() is handy.

Example:

# Iterating through a range for i in range(5): print(i)

    For loop with Dictionaries:

In Python, we can use for loop to iterate over the keys of a dictionary.

Example:

# Iterating through a dictionary info = {'name': 'Python', 'version': '3.9.1'} for key in info: print(key, info[key])

    Nested For loops:

A nested loop is a loop inside a loop. You can use one or more loop inside any for loop, while loop etc.

Example:

# Nested for loop for i in range(3): for j in range(3): print(i, j)

    The break and continue Statements:

The break statement stops the loop before it has looped through all the items, while the continue statement stops the current iteration and continues with the next.

Example:

# Using break and continue for num in [20, 11, 9, 66, 4, 89, 44]: if num%2 == 0: continue if num > 50: break print(num)
Exercise 🏋️‍♀️🤓🎯🏁

    Create a list of your 5 favorite foods. Write a for loop that prints "I love [food]" for each food in the list.

    Use the range() function to print the numbers from 0-9.

    Create a nested loop that prints a pattern of asterisks that looks like a rectangle. The rectangle should be 5 asterisks tall and 5 asterisks wide.

    Create a list of numbers and print out all the odd numbers using the continue statement.

    Modify the above task to stop the loop if a number greater than 50 is encountered using the break statement.

Happy Coding! 🚀👩‍💻👨‍💻💻🌟
