# Assignment 3.3
"""
Created on Wed Oct 21 23:21:58 2015
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