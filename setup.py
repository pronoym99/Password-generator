from setuptools import setup, find_packages

with open('requirements.txt') as f:
  requirements = f.readlines()

long_description = 'A sleek CLI Password generator built \
                      using the PyInquirer module'

setup(
    name='Password-generator',
    version='1.0.0',
    author='Pronoy Mandal',
    author_email='lukex9442@gmail.com',
    url='https://github.com/pronoym99/Password-generator',
    description=' A CLI tool for password generation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='The Unilicense',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gfg = vibhu4gfg.gfg:main'
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: The Unlicense",
        "Operating System :: OS Independent",
    ),
    keywords='password-generation cli python PyInquirer package lukex9442',
    install_requires=requirements,
    zip_safe=False
)
