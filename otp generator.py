# otp generator
from random import randint
from random import shuffle

# list of integers
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# list of lowercase alphabets
lower_alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# list of uppercase alphabets
upper_alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# list of special characters
special_char_list = ["!", "@", "#", "$", "%", "^", "&", "*"]

password_map = {1: num_list, 2: lower_alpha_list, 3: upper_alpha_list, 4: special_char_list}

main_use_list = []  # megalist

while True:
    try:
        # Asking the user for required length
        user_choice_password_length = int(raw_input("How many digit password do you want to generate?:"))
        if user_choice_password_length == 0:
            print "No null value passwords allowed"
        elif user_choice_password_length != 0:
            break
    except ValueError:
        # Handling the error where an user enters a string value
        # for the length of the otp (purposefully or otherwise)
        print "please enter a proper integer indicating the number of digits"


# handling desired choices
print '\n'.join(["MENU", "1.Numbers", "2.Lowercase Alphabets",
                 "3.Uppercase Alphabets", "4.Special characters"])
user_choices = raw_input(
    "Enter your choice(s);multiple choices can be added for eg.124:")

# construct your megalist
for i in user_choices:
    main_use_list.extend(password_map[int(i)])

# shuffle your list
shuffle(main_use_list)

# upperbound for random variable
limit = len(main_use_list)-1

otp = ""
while len(otp) < user_choice_password_length:
    i = randint(0, limit)
    otp += L[i]
print "Your one time password is-", otp
