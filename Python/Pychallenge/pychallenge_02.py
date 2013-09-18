# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:41:20 2013

@author: NotMark
"""



# Challenge 2 lies at:
#   http://www.pythonchallenge.com/pc/def/ocr.html

# Riddle stated: recognize the characters. maybe they are in the book,
#                   but MAYBE they are in the page source.

# Copied data from the webpage source:
filename = 'pychallenge_02.dat'

f = open(filename, 'r')

# Puts every line into its own list element. 
# Creates a list of strings
rawData = f.readlines()

# Combines all the individual lines into one long string
# This allows me to complile a set of the data easily
stringData = ''.join(rawData)

# Calling set() on a list will return a set object with
# the unique elements in the list.
charSet = set(stringData)
listData = list(charSet)

# Printing out the charSet, I realized the 'unique characters' the puzzle was
# talking about were letters. The letters in charSet were sorted in ascending
# order and appeared to be jumbled. Many solutions I read after this assumed
# that the unique characters must be letters. A key assumption that would have
# made this script shorted.

# ['\n', '!', '#', '%', '$', '&', ')', '(', '+', '*', '@', '[', ']', '_', '^',
#   'a', 'e', 'i', 'l', 'q', 'u', 't', 'y', '{', '}']

# I then called charSet.count(letter of interest) to see how many times the
# character appeared. Each character appeared only once. I guessed that the
# order that the letters appeared in the data was the original spelling of the
# word. Therefore I wanted to find the index of each letter and sorth them
# accordingly.

# Take only the character data from the list
letters = [c for c in listData if ord(c) >= ord('a') and ord(c) <= ord('z')]

# Find the index of each letter in the original string
indicies = [stringData.index(c) for c in letters]

from operator import itemgetter

# Turn the letters and their corresponding indicies into pairs of data (tuple)
pairs = zip(letters, indicies)

# Sort this list of tuples by the second item in each tuple i.e. the index
sortedPairs = sorted(pairs, key = itemgetter(1))

# Extract the first item in each tuple (the letter) and join it into a string
theWord = ''.join( [tup[0] for tup in sortedPairs])

# Guess what this does!
print theWord