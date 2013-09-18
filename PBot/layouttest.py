# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:12:09 2012

@author: ngt5ids
"""

import os, sys
from PyQt4 import QtGui

class MyWidget(QtGui.QWidget):

    def __init__(self):
        
        super(MyWidget, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        txtBox = QtGui.QLineEdit()
        
        picLabel = QtGui.QLabel()
        cancelBtn = QtGui.QPushButton("Save/Next")
        
        qlabelStyleSheet = "QLabel { background-color : rgb(230, 230, 240); }"        
        
        picLabel.setStyleSheet(qlabelStyleSheet)
        picLabel.setFixedSize(120, 135)
        
        txtBox.setFixedWidth(30)
        txtBox.setMaxLength(3)
        
        #Horizontal Layout
        hBox = QtGui.QHBoxLayout()
      
        hBox.addStretch(1)        
        hBox.addWidget(txtBox)
        hBox.addWidget(cancelBtn)
       
        #Vertical Layout        
        vBox = QtGui.QVBoxLayout()
        
        #vBox.addStretch(1)
        vBox.addWidget(picLabel)
        vBox.addLayout(hBox)
        
        self.setLayout(vBox)
        
        self.setGeometry(350, 350, 300, 200)
        self.setFixedSize(self.sizeHint())

        self.setWindowTitle("Layout Experiment")
        
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    
    myWidget = MyWidget()
    
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
    
        
        