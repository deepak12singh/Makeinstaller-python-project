import os
import sys

import logging


# from setupfiles.help import show_detailed_help
# from config import GENERATIVE_AI_KEY
from PythonFiles.control_file import setup_project
build_in_file_path = os.path.join(os.getcwd(),'Maker_file')

    


# Setting up logging configuration
logging.basicConfig(
    filename='application.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log starting point
logging.info("Script started")
# logging.info("Config file data: GENERATIVE_AI_KEY=%s", GENERATIVE_AI_KEY)

def main():
    # Check if there are enough command-line arguments
    if len(sys.argv) < 3:
        logging.error("Insufficient arguments provided.")
        print("Error: Insufficient arguments provided. Use 'autodata help' for usage information.")
        return

    # Retrieve command-line arguments
    argv = sys.argv
    command = argv[2].lower()

    logging.info("Command received: %s", command)

    # Process based on command
    if command == 'here':
        current_path = argv[-1]
        setup_project(current_path=current_path,build_in_file_path=build_in_file_path)
        logging.info("Current path set to: %s", current_path)
        
    elif command in ('path', 'p','-p'):
        # Validate path argument exists
        if len(argv) > 3:
            specified_path = argv[3]
            setup_project(current_path=specified_path,build_in_file_path=build_in_file_path)
            logging.info("Path set to: %s", specified_path)
        else:
            logging.error("Path argument missing for command 'path' or 'p'")
            print("Error: Path argument is missing. Please specify a path after 'path' or 'p' command.")

    else:
        logging.info("Displaying detailed help.")
        # show_detailed_help()
        print("\nDetailed help shown.")

if __name__ == '__main__':
    main()
    logging.info("Script ended")

        
    