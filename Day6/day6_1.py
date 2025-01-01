#   File Reading and Writing

# Opening a File: 
# Python has a built-in function open() to open a file.
# This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.



# Read the file print
file = open("Day6/testfile.txt" ,"r")
print(file.read())


# Write to a File
# the write() functions writes any string to an open file.
# The file must be opened in write "W" , append "a" or exclusive creation "x" mode

file = open("Day6/testfile.txt", "a")
file.write("added x")
# After finished with a file use close() function to free up resources that were tied with the file

file.close()

#     Using with Statement: The best way to close a file is by using the with statement.
# This ensures that the file is closed when the block inside the with statement is exited. 
# Example:  # Open and read a file with open("testfile.txt", "r") as file: print(file.read())

with open("Day6/testfile.txt", "r") as file:
    print(file.read())

