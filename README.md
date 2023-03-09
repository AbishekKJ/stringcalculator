# stringcalculator
String calculator- Return the sum of numbers in the string. You can use two below options to run the string calculator,

## Installation 1

Use the Below Steps to install the requirements

```bash
1. Create a Virtual environment
		
		python -m venv venv

2. Activate the virtual environment
		
		cd venv
		cd Scripts
		activate


3. To run the string calculator tool
		python stringcalculator.py

```
## Installation 2 - Cross platform approach

The best way, which is cross-platform, is to create setup.py, define an entry point in it and install with pip.

```bash
Say you have the following contents of hello.py:

def run():
    print('Hello world')
Then you add setup.py with the following:

from setuptools import setup
setup(
    name='hello',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'hello=hello:run'
        ]
    }
)
Entry point format is terminal_command_name=python_script_name:main_method_name

Finally install with the following command.

pip install -e /path/to/script/folder

-e stands for editable, meaning you'll be able to work on the script and invoke the latest version without need to reinstall

After that you can run myscript from any directory.
```
