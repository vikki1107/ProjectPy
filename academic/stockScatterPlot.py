#!/usr/bin/env python
"""
@author: vikki
"""

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

stock_list = []
stock_values = []

# Create a list from the text file
with open("AAPL-NFLX.txt", "r") as f:
    for line in f:
        stock_list.append(line.strip('\n').strip().split(','))

# remove all the white spaces
for item in stock_list:
    stock_values.append(' '.join(item).split())

x = stock_values[0] #AAPL list 
y = stock_values[1] #NFLX list

# Plot scatter 
ax.scatter(x, y, color='blue', s=10, edgecolor='none')
plt.xlabel("AAPL")
plt.ylabel("NFLX") 
