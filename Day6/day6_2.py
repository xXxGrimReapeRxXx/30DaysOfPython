# Python Input Functions

name = input("What's your name ? ")
print(f"Hello,{name}")


age = int(input("What is your age ? "))
print(f"You are {age} years old!")

# taking multiple inputs in a single line
# we can use the split() function along with the input function

name, age = input("Enter your name and age:").split()
print(f"Name : {name}, Age : {age}")
