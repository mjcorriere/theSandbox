# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 16:37:02 2012

@author: Mark
"""

import os, sys

from PIL import Image, ImageQt

from PyQt4 import QtGui
from PyQt4.QtCore import Qt

import glob

def extractCards(path):
    

    """
    extractCards takes a path pointing to a directory full of screenshots
    from the CarbonPoker client and returns an array of Qt QImages of each
    individual card.
    
    extractCards expects that each screenshot is of the carbonPoker client
    set to "default" window size.

    """
    
    os.chdir(path)    
    imgFileList = glob.glob('*.png')
    
    cardQtImages = []

    topLeftX = [277, 328, 380, 431, 482]
    topLeftY = 209
    
    squareSize = 42
    
    
    for imgFile in imgFileList:
        
        print "Opening " + str(imgFile)        
        img = Image.open(imgFile)
        
        #For some reason, some of my screenshots were RGBA
        #This tests and converts, if necessary        
        if img.mode != "RGB":
            print "Converting " + str(imgFile) + " to RGB ... "
            img = img.convert("RGB")
            print "Converted!"
            
        #pix = img.load()
        
        #Test to see how many cards are present for extraction
        #These three pixel locations should be pure white if there is
        #a card present there. First we test river, then turn, then flop
        
        if sum(img.getpixel((510, 220))) == 255*3:
            print "5 cards detected"
            cardsPresent = 5
            
        elif sum(img.getpixel((460, 220))) == 255*3:
            print "4 cards detected"
            cardsPresent = 4
            
        elif sum(img.getpixel((410, 220))) == 255*3:
            print "3 cards detected"
            cardsPresent = 3
            
        else:
            print "No cards detected in image " + str(imgFile)
            print "Aborting card extract for this image"
            break
        
        for i in range(cardsPresent):
            
            cardRegion = (topLeftX[i], topLeftY, topLeftX[i] + squareSize, \
                topLeftY + squareSize)
            
            cardImg = img.crop(cardRegion)
                
            cardQtImages.append(ImageQt.ImageQt(cardImg))
            

    print str(len(cardQtImages)) + " cards extracted!"
    
    return cardQtImages
    
class MyWidget(QtGui.QWidget):

    def __init__(self):
        
        super(MyWidget, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.txtBoxCardName = QtGui.QLineEdit()
        self.txtBoxCardName.returnPressed.connect(self.saveandNext)
        
        self.picLabel = QtGui.QLabel()
        self.picLabel.setObjectName("imgDisplay")
        self.picLabel.setAlignment(Qt.AlignCenter)
        self.picLabel.setScaledContents(True)
        
        self.saveBtn = QtGui.QPushButton("Save/Next")
        self.saveBtn.setObjectName("saveBtn")  
        self.saveBtn.clicked.connect(self.saveandNext)
        
        self.generateBtn = QtGui.QPushButton("Generate Cards")
        self.generateBtn.clicked.connect(self.extractCardsandDisplay)

        qlabelStyleSheet = "QLabel { background-color : rgb(230, 230, 240); }"        
        
        self.picLabel.setStyleSheet(qlabelStyleSheet)
        self.picLabel.setFixedSize(150, 150)        
        self.picLabel.baseSize()
        
        self.txtBoxCardName.setFixedWidth(30)
        self.txtBoxCardName.setMaxLength(3)
        
        self.txtBoxPath = QtGui.QLineEdit()
        self.txtBoxPath.setObjectName("pathText")
        
        self.btnBrowse = QtGui.QPushButton("...")
        self.btnBrowse.setObjectName("browseBtn")
        self.btnBrowse.clicked.connect(self.setExistingDirectory)
        
        self.btnBrowse.setFixedWidth(25)
        
        #Horizontal Layout
        #Input and Save Button
        self.hBoxInputSave = QtGui.QHBoxLayout()
      
        self.hBoxInputSave.addStretch(1)        
        self.hBoxInputSave.addWidget(self.txtBoxCardName)
        self.hBoxInputSave.addWidget(self.saveBtn)
        
        #Horizontal Layout
        #Path stuff
        
        self.hBoxPath = QtGui.QHBoxLayout()
        
        self.hBoxPath.addWidget(self.txtBoxPath)
        self.hBoxPath.addWidget(self.btnBrowse)        
       
        #Vertical Layout        
        self.vBox = QtGui.QVBoxLayout()
        
        #vBox.addStretch(1)
        self.vBox.addWidget(self.picLabel)
        self.vBox.addLayout(self.hBoxInputSave)
        self.vBox.addWidget(self.generateBtn)
        
        self.vBox.addLayout(self.hBoxPath)
        
        self.setLayout(self.vBox)
        
        self.setGeometry(350, 350, 300, 200)
        self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)      
        #self.setFixedSize(self.sizeHint())

        self.setWindowTitle("CardEx")
        
        self.show()
        
    def setExistingDirectory(self):    
        
        options = QtGui.QFileDialog.DontResolveSymlinks |\
            QtGui.QFileDialog.ShowDirsOnly
        
        directory = QtGui.QFileDialog.getExistingDirectory(self,
                "Board Image Directory",
                "", options)
                
        self.txtBoxPath.setText(directory)
        
    def extractCardsandDisplay(self):
        
        self.cardImages = extractCards(str(self.txtBoxPath.text()))
        self.currentCardIndex = 0
        
        self.picLabel.setPixmap(QtGui.QPixmap.fromImage(self.cardImages[0]))
        

        directories = os.walk('.').next()[1]
        for adir in directories:
            if adir == 'outcards':
                print "outcards exists"
            else:
                os.mkdir("outcards")

        os.chdir("outcards")
        
    def saveandNext(self):

        print self.cardImages[self.currentCardIndex].save(
            self.txtBoxCardName.text() + ".png", "PNG")

        if self.currentCardIndex == len(self.cardImages) - 1:
            print "End of list!"
            return False
        else:
            self.currentCardIndex += 1
            
        self.picLabel.setPixmap(QtGui.QPixmap.fromImage(
            self.cardImages[self.currentCardIndex]))
        
        self.txtBoxCardName.clear()

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    
    myWidget = MyWidget()    
    
    #extractCards(r"C:\Documents and Settings\NotMark\My Documents\PBot\boardimages")

    sys.exit(app.exec_())   
    
if __name__ == '__main__':
    main()
    

        