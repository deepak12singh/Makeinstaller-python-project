import os

# Absolute imports
from .copy_dir import copy_all
from .create_missing_file import create_files
from .rename import rename_file
from .get_name_folder import get_folder_names
from .get_file_names_from_path import get_file_names
from .replace_valuel import replace_all_values_in_file

def setup_project(current_path,build_in_file_path):
    """
    This function automates the setup of a project by performing tasks such as:
    - Copying necessary files
    - Creating required files if missing
    - Renaming and modifying template files based on project name
    """

    # Define paths
    # build_in_file_path = r'C:\Users\Sachin_Singh\Desktop\New folder\maker_file'
    # current_path = r"C:\Users\Sachin_Singh\Desktop\AdityaSir\make\New folder"
    result_path = os.path.join(current_path, 'OUTPUT')

    # Retrieve project name from the first folder in current_path
    project_name = get_folder_names(current_path)[0]
    copy_source_path = os.path.join(current_path, project_name)
    copy_destination_path = os.path.join(result_path, project_name)

    # Copy project folder contents to the output directory
    copy_all(copy_source_path, copy_destination_path)

    # Retrieve names of files in the destination directory
    present_files = get_file_names(copy_destination_path)

    # Initialize flags for key files
    main = config = requirements =setting = 0

    # Check if 'main.py' exists, if not, create it
    if 'run.py' not in present_files:
        main_path = os.path.join(copy_destination_path, 'run.py')
        create_files(main_path,project_name, main=True)

    # Check if 'main.py' exists, if not, create it
    if 'setting.py' not in present_files:
        setting = os.path.join(copy_destination_path, 'setting.py')
        create_files(setting,project_name, setting=True)

    # Check if 'config.py' exists, if not, create it
    if 'config.py' not in present_files:
        config_path = os.path.join(copy_destination_path, 'config.py')
        create_files(config_path, project_name,config=True)

    # Check if 'requirements.txt' exists, if not, create it
    if 'requirements.txt' not in present_files:
        requirements_path = os.path.join(copy_destination_path, 'requirements.txt')
        create_files(requirements_path,requirements=True)

    # Copy additional build files from '1' directory into the project folder
    copy_all(os.path.join(build_in_file_path, '1'), copy_destination_path)

    # Prepare the batch file for project start-up
    run_bat_file_path = os.path.join(copy_destination_path, 'ProjectStart.bat')
    Gaven_path_project,new_file_name =rename_file(run_bat_file_path, os.path.join(copy_destination_path, f'{project_name}.bat'))
    replace_all_values_in_file(new_file_name, Gaven_path_project, project_name)

    # Update the 'help.py' file with the project name
    replace_all_values_in_file(os.path.join(copy_destination_path, 'setupfiles', 'help.py'), 'ProjectName', project_name)

    # Copy remaining build files from '0' directory into the output directory
    copy_all(os.path.join(build_in_file_path, '0'), result_path)

    # Update the installer batch file with the project name
    replace_all_values_in_file(os.path.join(result_path, 'installer.bat'), 'ProjectStart' , project_name)
    file_setup_path = os.path.join(copy_destination_path,'setupfiles','helptxtfile')
    replace_all_values_in_file(os.path.join(file_setup_path,'help.txt'),'ProjectStart',project_name)
    replace_all_values_in_file(os.path.join(file_setup_path,'run.txt'),'ProjectStart',project_name)
    replace_all_values_in_file(os.path.join(file_setup_path,'key.txt'),'ProjectStart',project_name)
    path_uninstall = os.path.join(copy_destination_path,'setupfiles','uninstaller.bat')
    replace_all_values_in_file(path_uninstall,'ProjectStart',project_name)


