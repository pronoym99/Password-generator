# otp generator

# your CLI app essential
import click

from six import print_

# functions from random for password generation
from random import (choice,shuffle)
# decorative ascii text
from pyfiglet import figlet_format
# your CLI app essentials
from PyInquirer import (Token, ValidationError, Validator, prompt,
                        style_from_dict, Separator)

from pprint import pprint

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
    Token.Selected: '',  # default
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
            print_(colored(figlet_format(
                info, font=font), color))
    else:
        print_(info)


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
            'qmark': '\U0001F600',
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
    pprint(answers)



# questions = [
#         {
#             'type': 'input',
#             'name': 'password length',
#             'message': 'How many digit password do you want to generate?:',
#             'validate': PasswordLengthValidator
#         },
#         {
#             'type': 'checkbox',
#             'qmark': '\U0001F600',
#             'message': 'Select options ',
#             'name': 'password options',
#             'choices': [
#                 Separator('=== Menu ==='),
#                 {
#                     'name': 'Numbers'
#                 },
#                 {
#                     'name': 'Lowercase Alphabets'
#                 },
#                 {
#                     'name': 'Uppercase Alphabets'
#                 },
#                 {
#                     'name': 'Special characters'
#
#                 }
#             ]
#             # 'validate': PasswordOptionsValidator
#         }
#     ]
#
# answers = prompt(questions, style=style)
# pprint(answers)




@click.command()
def main():
    """
    Simple CLI for generating passwords
    """
    displayInfo("Password Generator", color="yellow", figlet=True)
    displayInfo("Welcome to Password generator CLI", "green")

    # a dictionary to store all ascii characters as strings
    password_map = {1: '0123456789', 2: 'abcdefghijklmnopqrstuvwxyz',
                    3: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4: '!@#$%^&*()-_=+<>?/|\{}[]~'}

    main_use_string = ''  # megastring

    askPasswordInformation()


if __name__ == '__main__':
    main()
