# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:01:25 2013

@author: NotMark
"""

# Challenge 3 lies at:
#    http://www.pythonchallenge.com/pc/def/equality.html

# Riddle stated: One small letter, surrounded by EXACTLY three big bodyguards 
#                   on each of its sides. 

# Viewing the page source showed a list of garbage. I copied and pasted it 
# into the filename below. Then I begun ...

filename = 'pychallenge_03.dat'

rawData = open(filename, 'r')

stringData = ''.join( [line.rstrip() for line in rawData] )

word = []

for index, c in enumerate(stringData):
    
    if c.islower():
        
        prevThree = ''.join([stringData[index - 3:index]])
        prevFourth = stringData[index - 4]
        
        if prevThree.isupper() and prevFourth.islower():
        
            nextThree = ''.join([stringData[index + 1:index + 4]])            
            nextFourth = stringData[index + 4]            
            
            if nextThree.isupper() and nextFourth.islower():
                
                word.append(c)
                
print ''.join(word)
            
        
        