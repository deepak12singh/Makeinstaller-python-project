def create_file(file_name, content=''):
    """
    Creates a Python file with predefined or passed content.

    Parameters:
        file_name (str): The name of the file to create.
        content (str): The content to write into the file.
    """
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"File '{file_name}' created successfully.")
    
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")





def create_files(path,project_name='',config=False,main=False,requirements=False,setting=False):
        
    main_content = f'''import sys
import logging
from setupfiles.help import show_detailed_help, show_command_help
from config import GENERATIVE_AI_KEY
from setupfiles.setup import Set_GENERATIVE_AI_KEY_, Set_All_Config
import subprocess

# Setting up logging configuration
logging.basicConfig(
    filename='application.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log starting point
logging.info("Script started")
logging.info("Config file data: GENERATIVE_AI_KEY=%s", GENERATIVE_AI_KEY)

def main():
    # Check if there are enough command-line arguments
    if len(sys.argv) < 3:
        logging.error("Insufficient arguments provided.")
        print("Error: Insufficient arguments provided. Use 'autodata help' for usage information.")
        return

    # Retrieve command-line arguments
    argv = sys.argv
    command = argv[1].lower()

    logging.info("Command received: %s", command)

    # Process based on command
    if command == 'run':
        if argv[2] == 'here':
            current_path = argv[-1]
            print(f"     Current path: {{current_path}}     ")
            logging.info("Current path set to: %s", current_path)
            # Run the setting.py first
            subprocess.run(['C:\\{project_name}\\.venv\\Scripts\\python.exe', 'setting.py','run','here',  current_path])
            # Now run main.py after setting.py completes

        elif argv[2] in ('path', 'p'):
            if len(argv) > 3:
                specified_path = argv[3]
                print(f"     Path: {{specified_path}}     ")
                logging.info("Path set to: %s", specified_path)
                # Now run main.py with the specified path
                subprocess.run(['C:\\{project_name}\\.venv\\Scripts\\python.exe', 'setting.py','run','path',  specified_path])
            else:
                logging.error("Path argument missing for command 'path' or 'p'")
                print("Error: Path argument is missing. Please specify a path after 'path' or 'p' command.")
    elif command in ('help', 'h', '-h'):
        if len(argv) > 3:
            value = argv[3]
            show_command_help(value)
        else:
            show_detailed_help()
    elif command in ('set', '-s'):
        if len(argv) > 3:
            key = argv[2]
            value = argv[3]
            if key == 'key':
                print(f"     Path: {{key}}  = {{value}}   ")
                Set_GENERATIVE_AI_KEY_(value)
            else:
                Set_All_Config(key, value)
        else:
            logging.error("Path argument missing for command 'path' or 'p'")
            print("Error: Path argument is missing. Please specify a path after 'path' or 'p' command.")
    else:
        logging.info("Displaying detailed help.")
        command_setting = ['C:\\{project_name}\\.venv\\Scripts\\python.exe', 'setting.py']
        for i in argv:
            command_setting.append(i)
        subprocess.run(command_setting)

if __name__ == '__main__':
    main()
    logging.info("Script ended")

    '''
    config_content = f'''
GENERATIVE_AI_KEY = 'None'

time_dale = 1.52
    '''



    setting_content = f'''
import sys
import subprocess
from setupfiles.help import show_detailed_help
print("running the setting file ")
def main():
    # Check if there are enough command-line arguments
    argv = sys.argv
    # Get the command-line argument (the path in this case)
    command = sys.argv[1].lower()
    if command == 'run':
        if argv[2] in ('path', 'here'):
            # Get the current path
            current_path = sys.argv[3]
            print(f"Setting current path to: {{current_path}}")
            # After setting up, now call main.py with the correct argument
            try:
                subprocess.run(['C:\\{project_name}\\.venv\\Scripts\\python.exe', 'main.py', current_path])
            except Exception as e:
                print(f"Error executing main.py: {{str(e)}}")
    else:
        show_detailed_help()
        print("Error: Invalid command passed to setting.py")


if __name__ == '__main__':
    main()

    '''


    if setting:
        create_file(path,setting_content)
    if config:
        create_file(path, config_content)
    if main:
        create_file(path, main_content)
    # Content for the config file
    if requirements:
        create_file(path)

# Example usage
if __name__ == '__main__':
    # Content for the main file
    create_files(1,1,1)
    
