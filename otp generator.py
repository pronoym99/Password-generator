# otp generator
from random import choice
from random import shuffle


password_map = {1: '0123456789', 2: 'abcdefghijklmnopqrstuvwxyz', 3: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4: '!@#$%^&*()-_=+<>?/|\{}[]~'}

main_use_string = ""  # megastring

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
    # enumerate over each of the strings in user_choice
    current_string = password_map[int(choice)]
    # construct your megastring at the same time
    main_use_string += password_map[int(choice)])
    # add atleast one character from each of the strings in user_choice
    otp += choice(current_string)


# reduced target length
target_length_of_otp = user_choice_password_length - len(user_choices)

while target_length_of_otp < user_choice_password_length:
    otp += choice(main_use_string)
    target_length_of_otp += 1

# shuffle your otp once
# remember to convert to list type and back to string type
otp = ''.join(shuffle(list(otp)))

# display the final otp
print "Your one time password is-", otp
