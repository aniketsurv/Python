import os

# Check if a file exists
if os.path.exists("example.txt"):
    print("exists")

# # Delete a file
# os.remove("delete.txt")

# # Open a file in read mode
# file = open('example.txt', 'r')

# # Read the entire content of the file
# content = file.read()
# print(content)


# # Read one line from the file
# line = file.readline()
# print(line)

# # Read all lines into a list
# lines = file.readlines()
# print(lines)

# # Open a file in write mode
# file = open('example.txt', 'w')

# # Write a string to the file
# file.write('Hello Mayur\n')

# # Write multiple lines to the file
# file.writelines(["Line 1\n", "Line 2\n", "Line 3\n","Line 4\n"])


# Open a file in append mode
file = open("example.txt", "a")
file.write('Good night\n')


#close() method to free up system resources.
file.close()