import sys
import os

def validate_arguments(command, args):
    if command == "reverse":
        if len(args) != 2:
            raise ValueError("reverse command takes exactly 2 arguments: inputpath outputpath")
        if not os.path.exists(args[0]):
            raise ValueError("Input file does not exist")
        
    elif command == "copy":
        if len(args) != 2:
            raise ValueError("copy command takes exactly 2 arguments: inputpath outputpath")
        if not os.path.exists(args[0]):
            raise ValueError("Input file does not exist")

    elif command == "duplicate-contents":
        if len(args) != 2:
            raise ValueError("duplicate-contents command takes exactly 2 arguments: inputpath outputpath")
        if not os.path.exists(args[0]):
            raise ValueError("Input file does not exist")
        try:
            int(args[1])
        except ValueError:
            raise TypeError("n must be an integer")
        
    elif command == "replace-string":
        if len(args) != 3:
            raise ValueError("replace-string command takes exactly 3 arguments: inputpath needle newstring")
        if not os.path.exists(args[0]):
            raise ValueError("Input file does not exist")
    
    else:
        raise ValueError("Invalid command")

def reverse_file(inputpath, outputpath):
    try:
        with open(inputpath, "r") as infile, open(outputpath, "x") as outfile:
            contents = infile.read()
            outfile.writelines(contents[::-1])
    except FileExistsError:
        print("Input file does not exist")

def copy_file(inputpath, outputpath):
    try:
        with open(inputpath, "r") as infile, open(outputpath, "w") as outfile:
            outfile.write(infile.read())
    except FileNotFoundError:
        print("Input file does not exist")
        print(f"Error: File'{inputpath}' does not exist")

def duplicate_contents(inputpath, n):
    try:
        with open(inputpath, "r+") as file:
            original_content = file.read()
            duplicate_content = original_content * int(n)
            file.write(duplicate_content)
    except FileNotFoundError:
        print("Input file does not exist")
        print(f"Error: File'{inputpath}' does not exist")

def replace_string(inputpath, needle, newstring):
    try:
        with open(inputpath, "r") as infile:
            content = infile.read()
            modified_content = content.replace(needle, newstring)
        with open(inputpath, "w") as outfile:
            outfile.write(modified_content)
    except FileNotFoundError:
        print("Input file does not exist")    
        print(f"Error: File'{inputpath}' does not exist")

def main():
    if len(sys.argv) < 2:
        print("Usage: python file_manipulator.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    try:
        validate_arguments(command, args)

        if command == "reverse":
            reverse_file(args[0], args[1])
        elif command == "copy":
            copy_file(args[0], args[1])
        elif command == "duplicate-contents":
            duplicate_contents(args[0], args[1])
        elif command == "replace-string":
            replace_string(args[0], args[1], args[2])

    except (ValueError, TypeError, FileNotFoundError) as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
