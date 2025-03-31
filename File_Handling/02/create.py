from pathlib import Path

file_path = "../All_Files/second_file.txt"

if Path(file_path).exists():
    print(f"The file {file_path} already exists.")
else:
    print(f"The file {file_path} not exists.")

    with open(file_path,"w") as file: 
        pass