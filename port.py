import os

all_files = os.listdir()

#  Rename .efo to .cr and .txt to .cl
for f in all_files:
    filename, file_extension = os.path.splitext(f)
    if file_extension == ".txt":
        old_name = f"{filename}.txt"
        new_name = f"{filename}.cl"
        os.rename(old_name, new_name)
    elif file_extension == ".efo":
        old_name = f"{filename}.efo"
        new_name = f"{filename}.cr"
        os.rename(old_name, new_name)

#  Print imports for main.cr
for f in all_files:
    filename, file_extension = os.path.splitext(f)
    if file_extension == ".cr":
        print(f'IMPORT "{f}"')