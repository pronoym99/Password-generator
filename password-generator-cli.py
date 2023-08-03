# otp generator

# module for secure source of randomness
# functions from random for shuffling
from random import shuffle
from secrets import choice

# predefined ascii string constants
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

# your CLI app essential
import click

# decorative ascii text
from pyfiglet import figlet_format

# your CLI app essentials
from PyInquirer import (
    Separator,
    Token,
    ValidationError,
    Validator,
    prompt,
    style_from_dict,
)

# for copying to clipboard
from pyperclip import copy
from six import print_

# your colouring essentials
try:
    import colorama

    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None

# a custom style for this CLI
style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#5F819D bold',
    Token.Question: '',
})


# an utility function for displaying information in colour
def displayInfo(info, color, font="slant", figlet=False):
    if colored:
        if not figlet:
            print_(colored(info, color))
        else:
            print_(colored(figlet_format(info, font=font), color))
    else:
        print_(info)


class PasswordLengthValidator(Validator):
    @staticmethod
    def validate(answer):
        try:
            user_choice_password_length = int(answer.text)

            if user_choice_password_length <= 0:
                raise ValidationError(
                    message="Please enter a positive integer",
                    cursor_position=len(answer.text),
                )  # Move cursor to end

        except ValueError:
            raise ValidationError(
                message="Please enter a positive integer",
                cursor_position=len(answer.text),
            )  # Move cursor to end


def askPasswordInformation():
    questions = [
        {
            "type": "input",
            "name": "password length",
            "message": "How many digit password do you want to generate?:",
            "validate": PasswordLengthValidator,
        },
        {
            "type": "checkbox",
            "qmark": "\U0001F600",
            "message": "Select options ",
            "name": "password options",
            "choices": [
                Separator("=== Menu ==="),
                {"name": "Numbers"},
                {"name": "Lowercase Alphabets"},
                {"name": "Uppercase Alphabets"},
                {"name": "Special characters"},
            ]
            # checkbox doesn't have a Validator implementation yet
        },
    ]

    answers = prompt(questions, style=style)
    return answers


def askCopyInformation():
    questions = [
        {
            "type": "confirm",
            "name": "copy",
            "message": "Do you want to copy password to clipboard?:",
            "default": False,
        }
    ]

    answers = prompt(questions, style=style)
    return answers


@click.command()
def main():
    """
    Simple CLI for generating passwords
    """
    displayInfo("Password Generator", color="yellow", figlet=True)
    displayInfo("Welcome to Password generator CLI", "green")

    # a dictionary to store all ascii characters as strings
    password_map = {
        "Numbers": digits,
        "Lowercase Alphabets": ascii_lowercase,
        "Uppercase Alphabets": ascii_uppercase,
        "Special characters": punctuation,
    }

    main_use_string = ""  # megastring

    # retrieve data from PyInquirer prompt
    password_info = askPasswordInformation()
    # first element of 'password_info' is the password length
    user_choice_password_length = int(password_info["password length"])
    # while second element of 'password_info' is a list of user choices
    user_choices = password_info["password options"]

    # initialise empty otp string
    otp = ""

    for choice_string in user_choices:
        # enumerate over each of the strings in user_choice
        current_string = password_map[choice_string]
        # construct your megastring at the same time
        main_use_string += current_string
        # add atleast one character from each of the strings in user_choice
        otp += choice(current_string)

    # reduced target length
    target_length_of_otp = user_choice_password_length - len(user_choices)

    # shuffle your otp once
    # add remaining characters as per reduced target length
    # remember to convert to list type before shuffling
    # and back to str type after shuffling
    otp_list = list(
        otp + "".join(choice(main_use_string)
                      for _ in range(target_length_of_otp))
    )
    shuffle(otp_list)
    otp = "".join(otp_list)

    # display the final otp
    print("Your one time password is-")
    displayInfo(otp, "red")

    if askCopyInformation()["copy"]:
        copy(otp)
        print("Password copied to clipboard")


if __name__ == "__main__":
    main()
