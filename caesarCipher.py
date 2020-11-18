#!/usr/bin/env python2
import string, sys

def alphaMap(text, num):
    newText = ''

    # Create a dictionary with both lower and upper case alphabets
    alphaDict = dict(zip(string.ascii_lowercase, range(1, 27)))
    alphaDict.update(dict(zip(string.ascii_uppercase, range(27, 53))))

    for i in text:
        if i not in alphaDict:
            # Continue if there are no alphabets
            newText += i
            continue

        # Store old index and create new one adding the shift
        oldIndex = alphaDict[i]
        newIndex = oldIndex + num

        # Reset the index if it goes beyond the alphabets assigned
        if (oldIndex < 27 and newIndex > 26) or (oldIndex > 26 and newIndex > 52):
            newIndex -= 26

        # Convert dictionary to list and get the key as per the index
        newText += alphaDict.keys()[alphaDict.values().index(newIndex)]

        # Standard key, value search
        # for k, v in alphaDict.items():
        #     if newIndex == v:
        #         newText += k
    return newText

# Pass arguments from command line
# if len(sys.argv) != 3:
#     print 'Provide 2 arguments: First the word and second the number \
#     and make sure to wrap quotes if using special characters are present'
#     sys.exit(1)
# #elif not sys.argv[1].isalpha():
# #    print 'Enter the word with only alphabets'
# elif not str(sys.argv[2]).isdigit():
#     print 'Enter a number/digit'
# else:
#     alphaMap(sys.argv[1], int(sys.argv[2]))

# Ask for input from user
try:
    text = str(input('Enter the text to translate:'))
except NameError:
    print 'Did you forget to wrap quotes around the text?'
    sys.exit(1)

num = int(input('Enter the number add to the text:'))
newText=alphaMap(text, num)
print 'Your original text entered is %s and after adding the index value %s, \n the final text is %s' % (text, num, newText)

# Test cases
#alphaMap('azcd',5)
