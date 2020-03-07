from setuptools import setup
setup(
    name = 'Password-generator',
    version = '0.1.0',
    packages = ['Password-generator-cli'],
    entry_points = {
        'console_scripts': [
            'Password-generator-cli = Password-generator-cli.__main__:main'
        ]
    })
