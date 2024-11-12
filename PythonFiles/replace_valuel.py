def replace_all_values_in_file(file_path, old_value, new_value):
    """
    Replaces all occurrences of old_value with new_value in a file.
    
    Parameters:
        file_path (str): The path to the file where the replacement will occur.
        old_value (str): The value to be replaced.
        new_value (str): The value to replace old_value with.
    """
    try:
        # Open the file for reading and writing (in text mode)
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()

        # Replace all occurrences of old_value with new_value
        updated_content = content.replace(old_value, new_value)

        # Open the file again to write the updated content
        with open(file_path, 'w') as file:
            file.write(updated_content)
        
        print(f"Replaced all occurrences of '{old_value}' with '{new_value}' in '{file_path}'.")

    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == '__main__':
    replace_all_values_in_file(r'C:\Users\Sachin_Singh\Desktop\New folder\ProjectStart.bat', 'ProjectStart', 'ProjectName')
