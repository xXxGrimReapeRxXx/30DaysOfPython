# While Loops
# Iterating over a block of code as long as the test expression (condition is true)

counter = 0
while counter < 5:
    print(counter)
    counter += 1

# TO terminate it we use break statement

counter = 0 
while counter < 5:
    print(counter)
    if counter == 3:
        break
    counter += 1
# Continue statement
print("Continue statement")
# The continue statement in Python returns the control to the
# beginning of the loop. The continue statement rejects
# all the remaining statements in the current iteration
# of the loop and moves the control back to the top of the loop.

counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue
    print(counter)
# The else Statement with While Loop:
# Python supports having an else statement
# associated with a loop statement.
# The else block just after for/while is executed
# only when the loop is NOT terminated by a break statement.

 
counter = 0
while counter <=5:
    print(counter)
    counter += 1
else:
    print("End of while loop")

# nested loops


print("nested loops")

i = 0
while i < 3:
    j = 0
    while j < 3:
        print(i, j)
        j += 1
    i += 1

# To better understand :
i = 0
while i < 3:
    print(f"Outer loop: i = {i}")
    j = 0
    while j < 3:
        print(f"  Inner loop: i = {i}, j = {j}")
        j += 1
    i += 1
