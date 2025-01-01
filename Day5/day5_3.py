# If-else statements

# if..elif..else
# used for decision making, control flow of execution based on certain conditions.

x = 5
if x > 0:
    print("x is positive")


# An if/else pair says: "If this expression is
# true, run this indented block of code.
# Otherwise, run this code instead."

x = -5
if x > 0:
    print("x is positive")
else:
    print("x is not positive")


# elif checks multiple expressions for truth and executes the code when
# one of them is true

x = 0
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


# Nested , check for a specific condition after a condition resolves to true

x = -6
if x > 0:
    if x % 2 == 0:
        print("x is a positive even number")
    else:
        print("x is positive odd number")
else:
    print("x is not positive")
