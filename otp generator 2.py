# otp generator

# clean Python 3.x-compatible codebase to support both Python 2 and Python 3 with minimal overhead.
from __future__ import print_function, unicode_literals

# your CLI app essential
import click

# functions from random for password generation
from random import choice
from random import shuffle
# decorative ascii text
from pyfiglet import figlet_format
# your CLI app essentials
from PyInquirer import (Token, ValidationError, Validator, print_json, prompt,
                        style_from_dict)

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
    #Token.Selected: '',  # default
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
            six.print_(colored(info, color))
        else:
            six.print_(colored(figlet_format(
                info, font=font), color))
    else:
        six.print_(info)

class PasswordLengthValidator(Validator):
    def validate(self, answer):
        try:
            user_choice_password_length = int(answer.text)

            if user_choice_password_length <= 0:
                raise ValidationError(
                    message='Please enter a positive integer',
                    cursor_position=len(answer.text))  # Move cursor to end

        except ValueError:
            raise ValidationError(
                message='Please enter a positive integer',
                cursor_position=len(answer.text))  # Move cursor to end

# class PasswordOptionsValidator(Validator):
#     def validate(self, answer):
#         try:
#             if len(answer) == 0:
#                 raise ValidationError(
#                     message='You must choose at least one option',
#                     cursor_position=len(answer.text))  # Move cursor to end


def askPasswordInformation():

    questions = [
        {
            'type': 'input',
            'name': 'password length',
            'message': 'How many digit password do you want to generate?:',
            'validate': PasswordLengthValidator
        },
        {
            'type': 'checkbox',
            'qmark': '😃',
            'message': 'Select options ',
            'name': 'password options',
            'choices': [
                Separator('=== Menu ==='),
                {
                    'name': 'Numbers'
                },
                {
                    'name': 'Lowercase Alphabets'
                },
                {
                    'name': 'Uppercase Alphabets'
                },
                {
                    'name': 'Special characters'

                }
            ]
            # 'validate': PasswordOptionsValidator
        }
    ]

    answers = prompt(questions, style=style)
    return answers

@click.command()
def main():
    """
    Simple CLI for generating passwords
    """
    displayInfo("Password Generator", color="blue", figlet=True)
    displayInfo("Welcome to Password generator CLI", "green")

if __name__ == '__main__':
    main()
