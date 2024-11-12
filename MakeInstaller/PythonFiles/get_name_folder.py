import os 


def get_folder_names(path):
    """
    Returns a list of all folder names in the given path.

    Parameters:
        path (str): The directory path where to list folder names.
    
    Returns:
        List[str]: A list of folder names.
    """
    # Ensure the provided path exists and is a directory
    if not os.path.exists(path) or not os.path.isdir(path):
        raise ValueError(f"The path '{path}' is not a valid directory.")

    # List all directories in the given path
    folder_names = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    return folder_names

# Run the function if this script is executed directly
if __name__ == '__main__':
    path = r'C:\Users\Sachin_Singh\Desktop\New folder'   # Replace with the desired path
    folder_list = get_folder_names(path)
    print("Folders:", folder_list)

