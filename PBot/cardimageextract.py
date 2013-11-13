# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 16:15:53 2012

@author: Mark
"""

import os

from PIL import Image
from PIL import ImageQt

import sys
from PyQt4 import QtGui

qtimgs = []

#List of top left card values and widths
topLeft = [277, 328, 380, 431, 482]
top = 209
squareSize = 42

#Coordinates to test for a white pixel, determining if a
#card is in that location
cardTestStartX = 310
cardtestY      = 220
cardTestIncX   = 50

cardsPresent = 0

path = "C:\\Documents and Settings\\NotMark\\My Documents\\Programming\\theSandbox\PBot\\boardimages"

os.chdir(path)
imglist = os.listdir(path)

print type(topLeft)

for filename in imglist:
    
    print "Opening " + filename
    img = Image.open(filename)
    
    print type(img)
    
    #Create an array of RGB values
    pix = img.load()
  
    #Pix is now a list of tuples
    #I would like to remove the alpha values, so I need to make
    #the tuples into lists in order to delete the 4th element
    if len(pix[0, 0]) == 4:
        print "Image " + filename + " is RGBA. Converting to RGB ... "
        img = img.convert("RGB")
        print "Converted."
        pix = img.load()
        print "Test pixel[0, 0]: " + str(pix[0, 0])
   
    #Test to see how many cards are present
    if sum(pix[310+4*50, 220]) == 255*3:
        print "River state"
        cardsPresent = 5
    elif sum(pix[310+3*50, 220]) == 255*3:
        print "Turn state"
        cardsPresent = 4
    else: 
        print "Flop state"
        cardsPresent = 3
        
    for i in range(cardsPresent):
        cardregion = (topLeft[i], top, topLeft[i] + squareSize, \
            top + squareSize)
            
        newcard = img.crop(cardregion)
        newcardQT = ImageQt.ImageQt(newcard)
        
        qtimgs.append(newcardQT)
        
        print len(qtimgs)
        
# MAIINNNNNNNNNNNNNN

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
window.setGeometry(150, 150, 400, 200)

pic = QtGui.QLabel(window)
pic.setGeometry(10, 10, 400, 100)
#use full ABSOLUTE path to the image, not relative
pic.setPixmap(QtGui.QPixmap.fromImage(qtimgs[0]))

#print os.getcwd()

window.show()
sys.exit(app.exec_())
        