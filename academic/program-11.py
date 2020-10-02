# Assignment 5.1
"""
Created on Wed Nov 11 18:01:30 2015
@author: vikki
"""
# Import modules responsible for plotting
import matplotlib.pyplot as plt
import numpy as np

# Assign global variables 
stock_list = []
stock_values = []
y = []
z = []

# Open the file and store the values into stock_list list
with open("program-11-AAPL-NFLX.txt", "r") as f:
    for line in f:
        stock_list.append(line.strip('\n').strip().split(','))

# Remove all the white spaces if there are from stock_list and store it under stock_values list
for item in stock_list:
    stock_values.append(' '.join(item).split())

# Assign the length of 1st list of stock_values. 
# This variable can be assigned to any number between 2 to length of 1st list of stock_values
#n = 26
n = len(stock_values[0])

# The reason behind assigning n to the length of 1st list of stock_values is to get all the values from 0 and plot it as x axis
# If n is assigned value 2 then x will have only 2 values as 0 and 1 and the graph will be a straight line
x = np.linspace(0, n-1, n)

# Get all the values for the nth value from stock_values[0] & stock_values[1] and store them in a list
for i in range(n):
    y.append(stock_values[0][i])
    z.append(stock_values[1][i])
    
#print x, y, z

# Plot line graph
plt.plot(x, y, label='AAPL')
plt.plot(x, z, 'r', label='NFLX')
plt.legend(loc = 5)
plt.xlabel("Time in Minutes")
plt.ylabel("Stock Price") 