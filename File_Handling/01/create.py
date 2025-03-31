import os

file_path = "../All_Files/first_file.txt"

if os.path.exists(file_path):
    print(f"The file {file_path} already exists.")
else:
    print(f"The file {file_path} not exists.")

    with open(file_path,"w") as file: 
        pass