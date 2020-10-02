# Assignment3.1
"""
Created on Thu Oct 22 00:26:23 2015
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