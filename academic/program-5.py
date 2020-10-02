# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 12:53:29 2015

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