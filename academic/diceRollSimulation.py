#!/usr/bin/env python
"""
Simulate 10,000 rolls of two dice. Begin by writing a function that simulates rolling a pair of six-sided dice. Your function will not take any parameters. It will return the total that was rolled on two dices as its only result.
Write a main program that uses your function to simulate rolling two six-sided dice 10,000 times. As your program runs, it should count the number of times that each total occurs. Then it should display a table that summarizes this data. Express the frequency for each total as a percentage of the total number of rolls. Your program should also display the percentage expected by probability theory for each total.

@author: vikki
"""

import random
# Empty dictionary to store the values for key 2 to 12
total = {}

def roll_pair_dice():
    return random.randint(1, 6) + random.randint(1, 6)
   
def main():
    # dictionary for the probability values for the total that occurs when 2 dice are rolled
    probability = { 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1 }

    for i in range(2, 13):
        total[i] = 0 # Initialize the dictionary values as 0

    n = 0 
    while n < 10000:  # performs 10000 rolls and stores the total of two dice under a total dictionary
        total[roll_pair_dice()] += 1
        n += 1

    print "\nTotal \t Simulated \t Expected"
    print "----- \t ---------\t ---------"
        
    # print the output in a structured format 
    for k in total.keys():
        print " ", k, "\t ", " %.2f" %float(total[k]/100.00) + "%", "\t ", "%.2f" %float(probability[k]/36.0 * 100) + "%"
 
# Call main function
if __name__ == "__main__":
    main()
