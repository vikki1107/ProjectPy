# Assignment 7.2
"""
Created on Thu Nov 19 16:18:08 2015
@author: vikki
"""
# Import the modules
import numpy as np
import math

# Helper function to resample the list
def resampling(l): 
    temp_list = []
    n = len(l) 
    for i in range(n):
        temp_list.append(l[np.random.randint(0, n)])
    return temp_list

# Main function to create a list of means from a given list for 10000 iterations and calculate the mean and standard deviation 
def main():
    sample_mean = []
    mylist = [48, 24, 51, 12, 21, 41, 25, 23, 32, 61, 19, 24, 29, 21, 23, 13, 32, 18, 42, 18]
    iterations = 10000
    for i in range(iterations):
        new_list = resampling(mylist)
#        print new_list
        sample_mean.append(np.mean(new_list))
#    print sample_mean
    mean_sample_mean = np.mean(sample_mean)
    std_sample_mean = np.std(sample_mean)        

    print "\nMean and Std deviation of %d iterations is %f and %f respectively" \
    %(iterations, mean_sample_mean, std_sample_mean)

# Section below is to find out the probability for a random variable in a distribution
# z here is nothing but the CDF(Cumulative distribution fuction) which is 1/2 * [1 + erf(x-μ / σ√2)]
# And probability would be 1 - z

    user_input = float(input("Now please enter a positive integer to find the probability: "))
    
    while user_input < 0:
        user_input = float(input("The integer you entered negative, Hence please enter a positive integer to find the probability: "))
    
    z = 0.5 * (1 + math.erf((user_input - mean_sample_mean)/(std_sample_mean * math.sqrt(2))))
    print "\nProbability that the number of reservations will be more than %d is %.2f" %(user_input, 1-z)
        
if __name__ == '__main__':
    main()