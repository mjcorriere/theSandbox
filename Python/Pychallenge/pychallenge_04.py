# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 18:57:38 2013

@author: NotMark
"""


# Challenge 3 lies at:
#   http://www.pythonchallenge.com/pc/def/linkedlist.php

# Riddle stated: Nothing. Just a photo. Clicking on the photo takes you to
#       http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# with the message: and the next nothing is 44827

# Putting that 5 digit sequence into the URL 'nothing=44827' brings you to
# another page with another sequence of digits. Thus it begins ...


import urllib2


baseUrl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
arg = '?nothing='
firstNum = 12345

response = urllib2.urlopen(baseUrl + arg + str(firstNum))

html = response.read()
lastGoodDigit = 0

for i in range(400):
    
    try:    
        digit = [num for num in html.split() if num.isdigit()][0]
        print html
        
    except IndexError:
        print 'Looks like there is no number here ...'
        
        print 'Here is the HTML: '
        print html

        print 'Here is the last good digit: ' + str(lastGoodDigit)
        digit = input('What number should we use next?: ')
        
    
    try:
        digit = int(digit)

    except ValueError:
        print 'Ooops. No digits here. Last good digit: ' + str(lastGoodDigit)
        break
    
    lastGoodDigit = digit
    nextUrl = baseUrl + arg + str(digit)
    
    html = urllib2.urlopen(nextUrl).read()
    


# Woohoo! The number that yielded the answer was 66831
# This is awesome.



