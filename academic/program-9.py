# Assignment 4.1

# import the modules for url open and format the data
import urllib
import json

# Assign a empty list for data
data = []

# Open the file and remove all the whitespaces from each line and store the words line by line
with open('program-9-data.txt', 'r') as infile:
    word_list = infile.read().split()

# For each line from the word_list, open a new file with the name prefixed to the filename and load the minute price for 
# a day within it.
for stock in word_list:
    outfile = open('%s_stockprice.txt' %stock, 'w') # open a new file
    
    htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/%s:US" %stock) # get the data

    data = json.load(htmltext)['data_values'] # sort the data for only data_values

    for point in data:
        outfile.write('%.2f\n' %float(point[1])) # Write only the value from the list to a file
        
    outfile.close() # Close the file