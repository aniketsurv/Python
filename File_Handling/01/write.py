import os

file_path = "../All_Files/first_file.txt"

with open(file_path, "w") as file:
    file.write("Hello world!\n")
