#!/usr/bin/env python
"""
One of the first known examples of encryption was used by Julius Caesar. Caesar needed to provide written instructions to his generals, but he didn't want his enemies to learn his plans if the message slipped into their hands. As a result, he developed what later became known as the Caesar Cipher.
The idea behind this cipher is simple (and as a result, it provides no protection against modern code breaking techniques). Each letter in the original message is shifted by 3 (or n) places. As a result, A becomes D, B becomes E, etc.  The last three letters in the alphabet are wrapped around to the beginning: X becomes A, Y becomes B, and Z becomes C. Non-letter characters are not modified by the cipher.

@author: vikki
"""

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

# set the key limit to 26 and provide the user input
key_limit = 26

function_input = raw_input("Please enter the functionality you would wish to perform; encrypt or e; decrypt or d : ")

# If the input entered is not e or encrypt or d or decrypt then keep looping until the user enters the right keyword
while function_input.lower() not in 'encrypt e decrypt d'.split():
    print "\nPlease enter either encrypt or e; decrypt or d."
    function = raw_input("Please enter the functionality you would wish to perform; encrypt or e; decrypt or d : ")
    
# If user had provided e or d then convert them to encrypt or decrypt
if function_input.lower() == 'e' or function_input.lower() == 'encrypt':
    function = 'encrypt'
elif function_input.lower() == 'd' or function_input.lower() == 'decrypt':
    function = 'decrypt'

message = raw_input("Please enter your message now to %s: " %function)

key = int(input('Enter the key number from 1 to 26: '))

# Check the key user provided is between 1 to 26
while key < 1 and key > key_limit:
    print "Please enter the key within 1 to 26"

print '\nYour Caeser', str(function) + str('ed') +' text is:', convert_message(function, message, key)
