# Assignment 2
"""
Most years have 365 days. However, the time required for the Earth to orbit the Sun is actually slightly more than that. 
As a result, an extra day, February 29, is included in some years to correct for this difference. Such years are referred to as leap years. 
The rules for determining whether or not a year is a leap year follow:
Any year that is divisible by 400 is a leap year.
Of the remaining years, any year that is divisible by 100 is NOT a leap year.
Of the remaining years, any year that is divisible by 4 is a leap year.
All other years are NOT leap years.
This program reads a year from the user and displays a message indicating whether or not it is a leap year.

Created on Wed Oct 07 12:f(22:26 2015
@author: Vivek
"""

# user inputs the year to be found whether leap year or not
year = raw_input("Please enter the year to check if its leap year or not : ")

# Check if user has entered a integer value if so then print a message whether its leap or not
# if not then print a message to input a valid intered
if year.isdigit():
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print "\nThe year you entered is a leap year."
    else:
        print "\nThe year you entered is not a leap year."
else:
    print "\nPlease enter a year in integer."