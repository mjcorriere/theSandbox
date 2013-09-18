# -*- coding: utf-8 -*-
"""
Created on Tue Jan 01 16:46:54 2013

@author: NotMark
"""

#OpenCV Test

import cv
from os import chdir

chdir(r"C:\Documents and Settings\NotMark\My Documents\PBot\boardimages")

window = cv.NamedWindow("myWindow", cv.CV_WINDOW_AUTOSIZE)

image = cv.LoadImage("01.png", cv.CV_LOAD_IMAGE_COLOR)
grey_image = cv.CreateImage(cv.GetSize(image), 8, 1)

cv.CvtColor(image, grey_image, cv.CV_RGB2GRAY)

image16 = cv.CreateImage(cv.GetSize(image), cv.IPL_DEPTH_16S, 1)

cv.Laplace(grey_image, image16, 1)
cv.Convert(image16, grey_image)

#font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8)
#
#x = 40
#y = 250
#
#cv.PutText(image, "Greetings.", (x, y), font, (255, 255, 255))
#
#cv.Line(image, (250, 30), (400, 290), (200, 200, 200), 1, 0)
#grey = cv.CreateImage((image.width, image.height), 8, 1)
#
#cv.CvtColor(image, grey, cv.CV_RGB2GRAY)
#
#spare = cv.CreateImage((image.width, image.height), 8, 3)
#
#cv.Smooth(image, spare, cv.CV_MEDIAN)

cv.ShowImage("myWindow", grey_image)

cv.WaitKey(20000)
