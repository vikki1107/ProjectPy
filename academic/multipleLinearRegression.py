#!/usr/bin/env python
"""
Multiple Linear Regression Model

@author: vikki
"""

# Import modules required for this code
from numpy import *
import numpy as np

# Normalizing the values by storing mean and standard deviation values in a list along with values of x
# If we fail to do so then for more number of iterations the t value will be reaching inf and we fail to predict the prices
# Example of t if not normalized [[inf] [inf] [inf] [1.20784356e+305]]
def normalization(x):
    global mean_list, std_list
    mean_list = []
    std_list = []
    
    x_norm = x

    for i in range(k - 1):
        m = mean(x[:, i])
        s = std(x[:, i])
        mean_list.append(m)
        std_list.append(s)
        x_norm[:, i] = (x_norm[:, i] - m) / s
    return x_norm, mean_list, std_list

# Cost function to predict the cost 
# T - Transpose method is used to interchange the rows to columns and viceversa for multiplication
# Here the error will be a m(13 in this example) X 1 matrix, hence transpose of error will result into 1 X m matrix
# so error transpose (1Xm) multiplies by error (mX1) results into a 1X1 matix
# Add all the values and store them under SSE - sum of squared errors
def cost(x, y, t):
    SSE = 0

    error = x * t - y
    SSE += error.T.dot(error)
    return SSE / (2 * m)

# Gradient descent function calculates the value of theta(t) for Iter number of iterations
# Same matrix operation technique are applied under this function 
# Here x is m(13)Xk(4) matrix, t will be k(4)X1 matrix so the resulting multiplcation yeilds mX1 matrix. 
# y is a mX1 matrix as well. So e will result in a mX1 matrix after subtracting y from x*t
# for each value of theta we multiply each column transposed(1Xm) with e(mX1), resulting in a single value or a 1X1 matrix
# At the end we will calculate theta value and end up with a kX1 matrix
def gradient(x, y, a, t):
    SUM_ex = 0

    e = x * t - y
    
    for i in range(len(t)):
        temp = x[:, i]
        SUM_ex = temp.T * e
        t[i] = t[i] - (a / m) * SUM_ex

    return t

# main function to read the file, calculate the number of columns in X and number of rows in Y
# Normalize the X values and append one at the first column to make it a mXk matrix
# Initialiase alpha, number of iterations and theta matrix
# for each iteration print the iteration, theta transpose 1Xk (1X4), predicted cost(normalized) and difference of the cost(normalized) 
# If we want to perform a test then uncomment the commented and follow the instructions
def main():
    global m, k
    x1 = []
#    filename = raw_input("Please enter the full path of a file on which you wish to perform gradient decent:\n")
#    data = genfromtxt(filename, delimiter = ',')
    data = genfromtxt("regression.csv", delimiter = ',')
    
    k = len(data[0])
    m = len(data)
    
    x0 = data[:, 0:k-1]
    y = data[:, k-1]

    y.shape = (m, 1)    

    x1, mean_list, std_list = normalization(x0)
    x = np.matrix(x1)
    x = c_[ones((m, 1)), x]
    
    a = 0.1
    Iter = 500
    
    t = zeros(shape = (k, 1))
    print x, y
    PreviousCost = cost(x,y,t)    
#    print PreviousCost
    
    for i in range(Iter):
        print i, t.T[0], cost(x,y,t), cost(x,y,t) - PreviousCost
        t = gradient(x, y, a, t)

#    Following code is to Check the predicted price of the mini-cooper
    print
    print "Please enter milage, year of model and T-top(as binary) below when prompted to predict the price of mini-cooper\n"
    milage = float(input('Please enter milage in 1000s: '))
    model_year = float(input('Please enter the year of make: '))
    T_top = float(input('Please enter whether you need a T-top or not. 0 - no T-top, 1 - T-top: '))
    
    price = array([1.0,   ((milage - mean_list[0]) / std_list[0]), \
                          ((model_year - mean_list[1]) / std_list[1]), \
                          ((T_top - mean_list[2]) / std_list[2])]).dot(t)
    print "\nPredicted price of the mini-cooper for above furnished data is $%.2f" %price[0]

# Call main function
if __name__ == "__main__":
    main()
