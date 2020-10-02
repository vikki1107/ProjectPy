# Assignment 2.2
"""
Created on Wed Oct 14 10:37:17 2015
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
    
    while good_password(a) not in True:
        a = rand_password()
        i += 1
    
    print "\nThe password generated is %s in %d iterations" % (str(password), i)    
        
#        print "\nThe password, %s, generated is bad. Hence re-generate it again." %password
              
if __name__ == "__main__": 
    main()  