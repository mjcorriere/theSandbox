# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 23:54:45 2012

@author: Mark
"""

import os,sys
from PyQt4 import QtGui
from PIL import Image, ImageQt
os.chdir(r"C:\Documents and Settings\NotMark\My Documents\PBot\images")

myimg = Image.open("2h.png")
myimgqt = ImageQt.ImageQt(myimg)

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
window.setGeometry(100, 100, 400, 200)

pic = QtGui.QLabel(window)
pic.setGeometry(10, 10, 400, 100)
#use full ABSOLUTE path to the image, not relative
print type(myimgqt)
pic.setPixmap(QtGui.QPixmap.fromImage(myimgqt))

print os.getcwd()

window.show()
sys.exit(app.exec_())