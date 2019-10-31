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
        if user_choice_password_length <= 0:
            print "No negative integers or null value allowed for password length"
        elif user_choice_password_length > 0:
            break
    except ValueError:
        # Handling the error where an user enters a string value
        # for the length of the otp (purposefully or otherwise)
        print "Please enter a proper integer indicating the number of digits"


# handling desired choices
print '\n'.join(["MENU", "1.Numbers", "2.Lowercase Alphabets",
                 "3.Uppercase Alphabets", "4.Special characters"])
user_choices = raw_input(
    "Enter your choice(s);multiple choices can be added for eg.124:")

# Ensure that at least one character from every option exists in the final otp

# initialise empty otp string
otp=""

for choice in user_choices:
    # enumerate over each of the lists in user_choice
    current_list = password_map[int(choice)]
    # upperbound for random variable
    limit = len(current_list) - 1
    # construct your megalist at the same time
    main_use_list.extend(password_map[int(choice)])

    otp_char = randint(0, limit)
    otp += current_list[otp_char]

# shuffle your list
shuffle(main_use_list)

# upperbound for random variable
limit = len(main_use_list)-1

# reduced target length
target_length_of_otp = user_choice_password_length - len(user_choices)

while target_length_of_otp < user_choice_password_length:
    otp_char = randint(0, limit)
    otp += main_use_list[otp_char]
    target_length_of_otp += 1
print "Your one time password is-", otp
