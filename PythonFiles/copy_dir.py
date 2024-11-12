import shutil
import os

def copy_all(src, dest):
    """
    Copies all files and folders from the source directory to the destination directory.
    
    Parameters:
        src (str): The path of the source directory.
        dest (str): The path of the destination directory.
    """
    # Ensure the source directory exists
    if not os.path.exists(src):
        raise FileNotFoundError(f"The source directory '{src}' does not exist.")
    
    # Ensure the destination directory exists
    os.makedirs(dest, exist_ok=True)
    
    # Walk through the source directory
    for root, dirs, files in os.walk(src):
        # Calculate the destination path for the current directory
        dest_dir = os.path.join(dest, os.path.relpath(root, src))
        
        # Create the destination directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)
        
        # Copy each file in the current directory
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dest_file)
            print(f"Copied '{src_file}' to '{dest_file}'")

# Example usage
if __name__ == '__main__':
    copy_all(r'C:\Users\Sachin_Singh\Desktop\AdityaSir\MakeInstaller\ProjectStart', r'C:\Users\Sachin_Singh\Desktop\New folder')
