# otp generator

# your CLI app essential
import click

from six import print_

# functions from random for password generation
from random import (choice, shuffle)
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
    return answers


@click.command()
def main():
    """
    Simple CLI for generating passwords
    """
    displayInfo("Password Generator", color="yellow", figlet=True)
    displayInfo("Welcome to Password generator CLI", "green")

    # a dictionary to store all ascii characters as strings
    password_map = {'Numbers': '0123456789', 'Lowercase Alphabets': 'abcdefghijklmnopqrstuvwxyz',
                    'Uppercase Alphabets': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'Special characters': '!@#$%^&*()-_=+<>?/|\{}[]~'}

    main_use_string = ''  # megastring

    # retrieve data from PyInquirer prompt
    answers = askPasswordInformation()
    # first element of 'answers' is the password length
    user_choice_password_length = int(answers['password length'])
    # while second element of 'answers' is a list of user choices
    user_choices = answers['password options']

    # initialise empty otp string
    otp = ''

    for choice_string in user_choices:
        # enumerate over each of the strings in user_choice
        current_string = password_map[choice_string]
        # construct your megastring at the same time
        main_use_string += current_string
        # add atleast one character from each of the strings in user_choice
        otp += choice(current_string)

    # reduced target length
    target_length_of_otp = user_choice_password_length - len(user_choices)

    for _ in range(target_length_of_otp):
        otp += choice(main_use_string)

    # shuffle your otp once
    # remember to convert to list type before shuffling and back to str type after shuffling
    otp_list = list(otp)
    shuffle(otp_list)
    otp = ''.join(otp_list)

    # display the final otp
    print('Your one time password is-')
    displayInfo(otp, "red")


if __name__ == '__main__':
    main()