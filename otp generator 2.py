# otp generator

# functions from random for password generation
from random import choice
from random import shuffle
# decorative ascii text
from pyfiglet import figlet_format

from __future__ import print_function, unicode_literals
# your CLI app essentials
from PyInquirer import style_from_dict, Token, prompt, Separator
#
from pprint import pprint

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
