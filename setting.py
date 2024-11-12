
import sys
import subprocess
# In setting.py
print('Running the Setting.py')
import sys
from setupfiles.setup import run_other_file

for i in range(len(sys.argv)):
    print('Your Given Argv:', i, '----->', sys.argv[i])

# Pass the entire argument list except the script name to `main.py`
run_other_file('main.py', sys.argv[2:])

# Update in setup.py
def run_other_file(file_path, args):
    try:
        command = [sys.executable, file_path] + args
        print("Executing command:", command)  # Debugging print statement
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Output from the file:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error running the file: {e}")
        print(f"Standard error output:
{e.stderr}")

