#otp generator
import random
L1=[]
for a in range (10):                                                                  
    L1.append(a)                                                                                                    #list of integers
L2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]        #list of lowercase alphabets
L3=[]
for a in L2:
    L3.append(a.upper())                                                                                            #list of uppercase alphabets
L4=["!","@","#","$","%","^","&","*"]                                                                                #list of special characters
L=L1+L2+L3+L4                                                                                                       #megalist
while True:
    try:
        n=int(raw_input("How many digit password do you want to generate?:"))                                       #Asking the user for required length
        if n==0:
            print"No null value passwords allowed"
        elif n!=0:
            break
    except ValueError:
            print "please enter a proper integer indicating the number of digits"                                 #Handling the error where an user enters a string value for the length of the otp (purposefully or otherwise)
otp=""
while len(otp)<n:
        i=random.randint(0,len(L)-1)
        if type(L[i])!=str:                                                                                       #Handling the case of addition of integers to a string or vice versa
            otp+=str(L[i])
        else:
            otp+=L[i]
print "Your one time password is-",otp
