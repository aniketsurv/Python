import os

file_path = "../All_Files/first_file.txt"

if os.path.exists(file_path):
    with open(file_path,'a') as file:
        file.write("Hello Aniket !\n")

