def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.
    
    Parameters:
        file_path (str): The path to the file.
    
    Returns:
        str: The content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at '{file_path}' was not found.")
        return None
    except IOError:
        print(f"An error occurred while reading the file '{file_path}'.")
        return None
