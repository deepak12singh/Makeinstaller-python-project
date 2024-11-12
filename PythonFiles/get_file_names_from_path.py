import os

def get_file_names(path):
    """
    Returns a list of all file names in the given path.
    
    Parameters:
        path (str): The directory path where to list file names.
    
    Returns:
        List[str]: A list of file names.
    """
    # Ensure the provided path exists and is a directory
    if not os.path.exists(path) or not os.path.isdir(path):
        raise ValueError(f"The path '{path}' is not a valid directory.")
    
    # List all files in the given path (excluding directories)
    file_names = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
    return file_names

# Example usage
if __name__ == '__main__':
    path = r'C:\Users\Sachin_Singh\Desktop\New folder'  # Replace with the desired path
    file_list = get_file_names(path)
    print("Files:", file_list)
