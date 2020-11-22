#!/usr/bin/env python
"""
Create a square root function that takes two parameters. The first parameter, n, will be the number for which the square root is being computed. The second parameter, guess, will be the current guess for the square root. The guess parameter should have a default value of 1.0. Do not provide a default value for the first parameter. Your square root function will be recursive. The base case occurs when guess^2 is within 10^-12 of n. In this case, your function should return guess because it is close enough to the square root of n. Otherwise, your function should return the result of calling itself recursively with n as the first parameter and (guess + n/guess)/2 as the second parameter.

Write a main program that demonstrate your square root function by computing the square root of several different values. When you call your square root function from the main program you should only pass one parameter to it so that the default value for guess is used.

@author: vikki
"""

# Recursive funtion which checks if the absolute value of guess^2 is within 10^12 of n, if so then print the guess which is the square root
# the number n if not then return the square_root function with a new guess value calculated.  
def square_root(n, guess):
    if abs(n - guess ** 2) < 0.000000000001:
        return guess
    else:
        return square_root(n, (guess + n/guess) / 2)

# Main funtion to input the number and print the square root 
def main():
    number = float(input("Please enter the number for which square root has to be calculated: "))
    print "\nSquare root %s is" %number, square_root(number, 1.0)

# Call main function
if __name__ == "__main__":
    main()
