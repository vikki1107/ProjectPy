#!/usr/bin/env python

# import the modules for url open and format the data
import urllib
import json

# Assign a empty list for data
data = []

# Open the file and remove all the whitespaces from each line and store the words line by line
with open('stocklist.txt', 'r') as infile:
    word_list = infile.read().split()

# For each line from the word_list, open a new file with the name prefixed to the filename and load the minute price for 
# a day within it.
for stock in word_list:
    # Open a new file
    with open('%s_stockprice.txt' %stock, 'w') as outfile:
        # Get the data
	htmltext = urllib.urlopen("http://www.bloomberg.com/quote/%s:US" %stock)

        # sort the data for only data_values
        data = json.load(htmltext)['data_values']

        for point in data:
            # Write only the value from the list to a file
            outfile.write('%.2f\n' %float(point[1]))
