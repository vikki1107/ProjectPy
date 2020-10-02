# Assignment 7.1
"""
Created on Thu Nov 19 13:38:38 2015
@author: vikki
"""
# Import modules
import numpy as np
import random
import matplotlib.pyplot as plt

# Helper function to shuffle the two lists and returns two lists with the same index
def reshuffle(p, d):
    index = len(p)
    combined = p + d
    random.shuffle(combined)
    p = combined[:index]
    d = combined[index:]
    return p, d

# Main function which has a original mean difference
# Also the new mean difference after the reshuffle for 10000 iterations
def main():
    global placebo, drug
    new_mean_hist = []
    placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
    drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
    
    mean_difference = abs(np.mean(placebo) - np.mean(drug))
    
    iterations = 10000
    count = 0
    for i in range(iterations):
        placebo, drug = reshuffle(placebo, drug)
    
        new_mean = np.mean(placebo) - np.mean(drug)
        new_mean_hist.append(new_mean)
        
        if abs(new_mean) >= mean_difference:
            count += 1
    
    p = float(count)/iterations
    
    plt.hist(new_mean_hist, 100, normed=1, facecolor='green')
    plt.xlabel('mean difference')
    plt.ylabel('Probability')
    plt.title(r'Histogram of $\mu$ difference')
    plt.show()
    if p > 0.01:
        output = 'ineffective'
    else:
        output = 'effective'
    
    print "\nIf the drug is as effective as the placebo, then the probability that the difference between \
the average placebo value and the average drug value is greater than or equal to 12.97 is %s. \
Thus, we conclude that the drug is '%s' given a significance level of 1%%." %(float(count)/iterations, output)
           
    
if __name__ == '__main__':
    main()
