# For loop with Lists
# Can iterate over the elements of a given list

fruits = ['apple','banana','cherry']
for fruit in fruits : print(fruit)

# For loop with Strings

for letter in 'Pythonista':
    print(letter)


# For loop with range() function
# Iterating over a sequence of numbers with the buil-in range() function

for i in range(5):
    print(i)

# For loops with dictionaries
# Ierating over the keys of a dictionary

info = {"name" : 'Python', 'version' :'3.9.1'}
for key in info :
    print(key, info[key])

# Nested For Loops
for i in range(3):
    for j in range(3):
        print(i, j)

# Break and continue statements
# The break statement stops the loop before it
# has looped through all the items, while
# the continue statement stops the current iteration
# and continues with the next.
nums = [20, 11, 9, 66, 4, 89, 44]  # Correctly identify the list and variable name
for num in nums:  # Loop through the list
    if num % 2 == 0:  # Check if the number is even
        if num > 50:  # Nested condition to check if the number is greater than 50
            break  # Break the loop if the condition is met
        continue  # Skip the current iteration for other even numbers
    print(num)  # Print the number if it's odd
