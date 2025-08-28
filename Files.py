def file_operations_challenge():
    """
    This program reads a file, creates a modified version, and handles errors.
    """
    
    # Error Handling Lab: Ask for filename with error handling
    while True:
        try:
            filename = input("Enter the filename you want to read: ")
            
            # Try to open and read the file
            with open(filename, 'r') as file:
                content = file.read()
            
            # If successful, break out of the loop
            break
            
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied to read '{filename}'. Please try a different file.")
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file. Please enter a filename.")
        except UnicodeDecodeError:
            print(f"Error: Cannot decode '{filename}'. It might be a binary file. Please try a text file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
    
    # File Read & Write Challenge: Create modified version
    try:
        # Create output filename (add '_modified' before extension)
        if '.' in filename:
            name_parts = filename.rsplit('.', 1)
            output_filename = f"{name_parts[0]}_modified.{name_parts[1]}"
        else:
            output_filename = f"{filename}_modified"
        
        # Modify the content (example: convert to uppercase and add line numbers)
        modified_content = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            modified_line = f"{i:3d}. {line.upper()}"
            modified_content.append(modified_line)
        
        # Join back into a single string
        final_content = '\n'.join(modified_content)
        
        # Write to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(final_content)
        
        print(f"Success! Modified file saved as: {output_filename}")
        print(f"Original file had {len(lines)} lines.")
        
    except Exception as e:
        print(f"Error writing modified file: {e}")

# Run the program
if __name__ == "__main__":
    print("📝 File Modification Program")
    print("=" * 40)
    file_operations_challenge()