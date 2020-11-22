#!/usr/bin/env python
"""
In this exercise, your will first write a function that determines whether or not a password is good. We will define a good password to be a one that is at least 8 characters long and contains at least one uppercase letter, at least one lowercase letter, and at least one number. Your function should return True if the password passed to it as its only parameter is good. Otherwise it should return False.
Then use the random password generator from Example 4-4 (copy that function and paste it here) and the function you defined above, write a program that generates a random good password and displays it. Count and display the number of attempts that were needed before a good password was generated. Call the two functions mentioned above from a function named main in the file that you create for this exercise. Ensure that your main program only runs when your solution has not been imported into another file.

@author: vikki
"""

# Import random function to randomly choose a number
import random

# Assign default values to the variables
min_letter = 8
max_letter = 9
min_ascii = 48
max_ascii = 122
password = ''
lower = 0
upper = 0
digit = 0
num = 0

def rand_password():
    global password
    n = random.randrange(min_letter, max_letter)
    
    for i in range(n):
        char = chr(random.randrange(min_ascii, max_ascii))
        password += char       
    return password

def good_password(a):
    global lower,upper,digit, num

    # loop each letter in the randomly generated password and check if it has lower, upper or digit.  
    for l in a:
        if l.isalnum():
            num = ord(l)
            
        if num >= 65 and num <= 90:
            lower += 1
        elif 97 <= num <= 122:
            upper += 1
        elif 48 <= num <= 57:
            digit += 1

    # If the password has atleast a lower, a upper and a digit, return True         
    if lower >= 1 and upper >= 1 and digit >= 1:
        return True

def main():
    i = 0
    a = rand_password()
    
    while not good_password(a):
        a = rand_password()
        i += 1
    
    print "\nThe password generated is %s in %d iterations" % (str(password), i)    
#    print "\nThe password, %s, generated is bad. Hence re-generate it again." %password
              
if __name__ == "__main__": 
    main()  
