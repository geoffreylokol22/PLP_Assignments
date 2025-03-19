def file_modify_and_write(input_filename, output_filename):
    """
    Reads a file, modifies its content, and writes it to a new file.

    Args:
        input_filename: The name of the input file.
        output_filename: The name of the output file.
    """
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        modified_lines = [line.upper() for line in lines]  # Example modification: uppercase

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"File '{input_filename}' modified and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_filename_and_handle_errors():
    """
    Prompts the user for a filename and handles potential errors.
    """
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            content = file.read() #or file.readlines()
            print(f"File '{filename}' content:\n{content}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
input_file = "input.txt"  # Create a dummy input.txt file for testing.
output_file = "output.txt"

#Create dummy input file if it does not exist.
try:
  with open(input_file, 'x') as f:
    f.write("this is a test\nthis is another test")
except FileExistsError:
  print("input file already exists, continuing")

file_modify_and_write(input_file, output_file)
get_filename_and_handle_errors()