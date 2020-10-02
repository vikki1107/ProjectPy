# Assignment2.1
"""
Created on Tue Oct 13 15:40:34 2015
@author: vikki
"""
# set the key limit to 26 and provide the user input
key_limit = 26

function = raw_input("Please enter the functionality you would wish to perform; encrypt or e; decrypt or d : ")

# If user had provided e or d then convert them to encrypt or decrypt
if function == 'e':
    function = 'encrypt'
elif function == 'd':
    function = 'decrypt'

# If the input entered is not e or encrypt or d or decrypt then keep looping until the user enters the right keyword
while function not in 'encrypt e decrypt d'.split():
    print "\nPlease enter either encrypt or e; decrypt or d."
    function = raw_input("Please enter the functionality you would wish to perform; encrypt or e; decrypt or d : ")
    
message = raw_input("Please enter your message now to %s: " %function)

key = int(input('Enter the key number from 1 to 26: '))

# Check the key user provided is between 1 to 26
if key < 1 and key > key_limit:
    print "Please enter the key within 1 to 26"

# Function to convert the message input by user to Ceaser's cipher
def convert_message(function, message, key):
# If the function is decrypt then make the key value as negative
    if function[0] == 'd':
        key = -key
        
    new_message = ''
        
    for l in message:
        if l.isalpha():
            n = ord(l)
            n += key
            
            if l.isupper():
                if n > ord('Z'):
                    n -= 26
                elif n < ord('A'):
                    n += 26
            elif l.islower():
                if n > ord('z'):
                    n -= 26
                elif n < ord('a'):
                    n += 26
    
            new_message += chr(n)
        else:
            new_message += l
    return new_message  

print '\nYour Caeser', str(function) + str('ed') +' text is:', convert_message(function, message, key)