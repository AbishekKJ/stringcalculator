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

## To execute the string calculator

python stringcalculator

It asks for the string input 

![image](https://user-images.githubusercontent.com/40816819/224110365-841225ad-a813-4875-a223-6cac7fb2f2a8.png)


## Unittest and Coverage Report:

![image](https://user-images.githubusercontent.com/40816819/224109052-87df2eed-2138-4211-9278-0a5d4186105f.png)

## Improvements:

1. Docker can be used to make the program suitable for all the run time
2. Regex can be used to parse the strings more effectively. Not used to avoid it as a quick hack
3. If needed as installable then we can use pyinstaller to create executable files
