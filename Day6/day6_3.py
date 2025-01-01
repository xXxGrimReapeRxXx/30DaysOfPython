# Basic print() function prints the specified message to the screen
print("Python Learning!")

# sep parameter determines how multiple arguments (values) are separated

print("Hello", "Python", sep="//")

# end paramenter determines what is printed at the end. Defaul is set to newline
print("Hello Python", end="!@")

# Print Formatted String:
# We can format the print output using the string's format method or f-string (formatted string literals).
name = "pythonista"
print(f"Hello,{name} !")

# Print and input functions can be used together to created interactive programs

name = input("What's your name")
print(f"Hello, {name} !")