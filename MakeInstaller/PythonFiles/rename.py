import os
from .readfilesdata import read_file
def rename_file(old_name, new_name):
    """
    Renames a file from old_name to new_name, removing the target file if it already exists.
    
    Parameters:
        old_name (str): The current file path and name.
        new_name (str): The new file path and name.
    """
    your_proect_path='ProjectStart'

    # Check if the old file name exists
    if not os.path.exists(old_name):
        raise FileNotFoundError(f"The file '{old_name}' does not exist.")
    
    try:
        # Attempt to rename the file
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'")
    except FileExistsError:
        # If the new file name already exists, remove it and retry the rename
        print(f'\n      Use Build in File Remove your {os.path.basename(new_name)} only (y,n) ',end='')
        choice = input(':-')
        if choice == 'y':
            os.remove(new_name)
            os.rename(old_name, new_name)
        else:
            print(f'\n\n                 Your file **{os.path.basename(new_name)}**\n\n')
            print("    ",read_file(new_name))
            print('\n\n')
            your_proect_path = input("Gave your runable path gave :-")
            os.remove(old_name)
        print(f"Existing file '{os.path.basename(new_name)}' removed and '{os.path.basename(old_name)}' renamed to '{os.path.basename(new_name)}'")
    
    return your_proect_path , new_name


# Example usage
if __name__ == '__main__':
    rename_file(r'C:\Users\Sachin_Singh\Desktop\New folder\nemProjec.bat', r'C:\Users\Sachin_Singh\Desktop\New folder\ProjectStart.bat')
