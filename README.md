![Password generator welcome text](https://github.com/pronoym99/Password-generator/blob/master/header%20symbol.PNG)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Password Generator

Your sleek CLI Password generator built using [PyInquirer](https://github.com/CITGuru/PyInquirer)

## Table of contents

1.  [Installation](https://github.com/pronoym99/Password-generator#installation)
2.  [Usage](https://github.com/pronoym99/Password-generator#usage)
3.  [To do](https://github.com/pronoym99/Password-generator#to-do)
4.  [License](https://github.com/pronoym99/Password-generator#license)

### Installation

Like any other repo you can clone this repo onto your local machine using the following command

    git clone https://github.com/pronoym99/Password-generator.git

till a proper pip distribution is available (For more information see [To do](https://github.com/pronoym99/Password-generator#to-do))

### Usage

The usage is pretty self-explanatory. It is divided into the following sections

-   **Option selection** - All the major type of characters can be included in your password such as **Numbers**, **Uppercase letters**, **Lowercase letters** and **Special characters**.

    ![Option selection demo](https://github.com/pronoym99/Password-generator/blob/master/Option%20selection.gif)

    The number of characters in the password is to be entered at the top. Choose anyone or more than one of the options that follow. Use \\&lt;up> and \\&lt;down> to move. <space> to select and deselect. \\&lt;a>  to toggle and \\&lt;i> to invert all selections respectively.    

* * *

-   **Password generation** - After going through the above steps press the famous _**Enter**_ button to generate your password as shown below.

![Password generation demo](https://github.com/pronoym99/Password-generator/blob/master/Password%20generation.gif)

* * *

-   **Copying password** - After generating the password, the CLI tool gives you the option to **Copy** the generated password to your clipboard. Press y/n on your keyboard to confirm your selection.

![Copy demo](https://github.com/pronoym99/Password-generator/blob/master/Copying%20password.gif)

### To do
    
-   [ ] Migrate from ```random``` to the more secure ```secrets``` module
-   [ ] Avoid display of passwords in text or encrypted format
-   [ ] Create a proper pip distribution
-   [x] Rectify invalid escape sequence warning :warning:
-   [ ] Add more desirable features

### License

Licensed under [The Unilicense](https://github.com/pronoym99/Password-generator/blob/master/LICENSE)
