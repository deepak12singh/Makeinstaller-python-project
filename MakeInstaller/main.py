import os
import sys

import logging


from setupfiles.help import show_detailed_help
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

    # Retrieve command-line arguments
    argv = sys.argv
    current_path = argv[-1]

    # Process based on command
    if current_path:
        setup_project(current_path=current_path,build_in_file_path=build_in_file_path)
    else:
        logging.info("Displaying detailed help.")
        show_detailed_help()
        print("\nDetailed help shown.")

if __name__ == '__main__':
    main()
    logging.info("Script ended")

        
    