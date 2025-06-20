# 2.Write a function that reads a text file and returns its
# lines.
# Use with open(...) as f:
# Catch and handle FileNotFoundError with a user-friendly message.
# From main(), prompt user for file name, call read_lines, then print line
# count

def read_lines(filename: str) -> list[str]:
    """
    Reads lines from a given text file.

    Args:
        filename (str): Name of the file to read.

    Returns:
        list[str]: List of lines from the file.
    """
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def main():
    file_name = input("Enter the file name: ")
    lines = read_lines(file_name)
    print(f"Total lines in file: {len(lines)}")

if __name__ == "__main__":
    main()