import os

def main():
    os.chdir('files/')
    all_files = os.listdir()
    print(all_files)

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
        elif file_extension == ".efe":
            old_name = f"{filename}.efe"
            new_name = f"{filename}.cr"
            os.rename(old_name, new_name)

    #  Print imports for main.cr
    with open("main.cr", "w") as main:
        for f in all_files:
            filename, file_extension = os.path.splitext(f)
            if file_extension == ".cr" and filename != "main":
                print(f'IMPORT "{f}"')
                main.write(f'IMPORT "{f}"\n')


if __name__ == "__main__":
    main()