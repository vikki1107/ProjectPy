#!/usr/bin/env python
"""
There is at least one word in the English language that contains each of the vowels (case insensitive) a, e, i, o, u and y exactly once and in order. 
Write a program that searches words.txt and displays all of the words that meet this constraint.

@author: vikki
"""

# Global variables declaration
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
output = []

# helper function to check if there are vowels in words.
def check(word, vowels):
    # local variable to count the vowels in words
    vowel_count = 0 
    n = 0    
    
    # check if there are more than 6 vowels in a word if so then it doesnt satisfy our condition
    for i in range(len(word)):
        if word[i].lower() in vowels:
            n += 1

    # if vowels count is only 6 then check if they are in order as below        
    if n == 6: 
        # check first letter from word matches the first letter of vowel, if not then check the next letter and so on 
        # if any letter from a word matches the first vowel then increment the vowel count and check for the second vowel sequentially.
        # When the vowel_count matches the length of dict vowel i,e 6 then return True i,e the word has vowels present in order
        for letter in word:
            if letter.lower() == vowels[vowel_count]:
                vowel_count += 1
                if vowel_count == len(vowels):
                    return True

# Main function which takes each word from a file 
def main():                                
    with open(path, 'r') as infile:
        for line in infile:
                words = line.split()
                for word in words:
                    if check(word, vowels): # call function check to check if there are vowels in word.
                        output.append(word) # Appened the words when the functions returns True
    
    print "\nFollowing are the list of words that contains vowels in order:\n", output


path = raw_input("Please enter the full path including the filename. \
If the file is present in your current working directory then just enter the filename: ")

# Call main function
if __name__ == "__main__":
    main()
