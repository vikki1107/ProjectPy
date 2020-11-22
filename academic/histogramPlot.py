#!/usr/bin/env python
"""
Histogram Plot

@author: vikki
"""
# Import the plot modules 
import numpy as np
import matplotlib.pyplot as plt

# Assign empty list to a variable
data = []

# Open file and store all the values in list data
with open("histogram.txt", "r") as f:
    for line in f:
        data.append(line.strip())

# store the an array with all the values from data into x
x = np.array(data).astype(np.int)

# Assign 2 different bins
num_bins1 = 50
num_bins2 = 100

# Plot first graph using subplot - 2 rows, 1 column, 1st subplot. With first number of bin
plt.subplot(2, 1, 1) 
plt.hist(x, num_bins1, normed=1, facecolor='red', label='no of bins - 50')
plt.title('Test Score Distribution')
plt.ylabel('Probability')
plt.legend(loc = 2)

# Plot first graph using subplot - 2 rows, 1 column, 2nd subplot with second number of bin
plt.subplot(2, 1, 2) 
plt.hist(x, num_bins2, normed=1, facecolor='blue', label='no of bins - 100')
plt.xlabel('Score')
plt.ylabel('Probability')
plt.legend(loc = 2)

plt.show()
