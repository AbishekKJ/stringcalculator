from setuptools import setup
setup(
    name='stringcalculator',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'stringcalculator=stringcalculator:main'
        ]
    }
)