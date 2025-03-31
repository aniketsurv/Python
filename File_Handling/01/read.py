import os

file_path = "../All_Files/first_file.txt"

with open (file_path,'r') as file:
    abc =file.read()
    print(abc)


with open (file_path,'r') as file:
    for i in file:
        print(i,end='')    # Print each line without adding extra newline

