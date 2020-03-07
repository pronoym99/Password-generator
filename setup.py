from setuptools import setup
setup(
    name = 'Password-generator-cli',
    version = '0.1.0',
    packages = ['Password-generator'],
    entry_points = {
        'console_scripts': [
            'Password-generator = Password-generator.__main__:main'
        ]
    })
