#!/usr/bin/env python
"""
Create a program that identifies all of the words in a string entered by the user. Begin by writing a function that takes a string of text as its only parameter. Your function should return a list of the words in the string with the punctuation marks at the edge of the words removed. Do not remove punctuation marks that appear in the middle of a words, such as the apostrophes used to form a contraction. For example, if your function is provided with the string "Examples of contractions include: don't, isn't, and wouldn't." Your function should return the list ["Examples", "of", "contractions", "include", "don't", "isn't", "and", "wouldn't"].

Write a main program that demonstrates your function. It should read a string from the user and display all of the words in the string with the punctuation marks removed. As a result, you should ensure that your main program only runs when your file has not been imported into another program.

@author: vikki
"""

import json

words = ''

def break_words(input):
    global words
    
    # This will break up words based on space
    words = input.split(' ')
    return words
   
def main():
    input = raw_input('Enter a sentence: ')
    a = break_words(input)

    for i in range(len(a)):
        a[i] = a[i].strip('?:!.,;"')
        
    print "\nWords in the string are:",json.dumps(a)

if __name__ == "__main__": 
    main()      
