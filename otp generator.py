# otp generator
from random import randint as r

# list of integers
L1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# list of lowercase alphabets
L2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# list of uppercase alphabets
L3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# list of special characters
L4 = ["!", "@", "#", "$", "%", "^", "&", "*"]

pwd = {1: L1, 2: L2, 3: L3, 4: L4}
L = []  # megalist
while True:
    try:
        # Asking the user for required length
        n = int(raw_input("How many digit password do you want to generate?:"))
        if n == 0:
            print "No null value passwords allowed"
        elif n != 0:
            break
    except ValueError:
        # Handling the error where an user enters a string value
        # for the length of the otp (purposefully or otherwise)
        print "please enter a proper integer indicating the number of digits"


# handling desired choices
print '\n'.join(["MENU", "1.Numbers", "2.Lowercase Alphabets",
                 "3.Uppercase Alphabets", "4.Special characters"])
ch = raw_input(
    "Enter your choice(s);multiple choices can be added for eg.124:")

# construct your megalist
for i in ch:
    L.extend(pwd[int(i)])

# upperbound for random variable
limit = len(L)-1

otp = ""
while len(otp) < n:
    i = r(0, limit)
    otp += L[i]
print "Your one time password is-", otp
