# -*- coding: utf-8 -*-
"""
Created on Tue Jan 01 18:25:04 2013

@author: NotMark
"""

import cv

from os import chdir

chdir(r"C:\Documents and Settings\NotMark\My Documents\PBot\boardimages")

cv.NamedWindow("Erosion Demo", cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow("Dilation Demo", cv.CV_WINDOW_AUTOSIZE)

cv.CreateTrackbar("Name or whatever", "Erosion Demo", 0, 2, erosion)

cv.CreateTrackbar("Other thing", 0, 5, dilation())


cv.WaitKey(5000)

def erosion():
    print "hi"
    
def dilation():
    print "placeholder"