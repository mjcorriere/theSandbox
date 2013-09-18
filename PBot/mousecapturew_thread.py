# -*- coding: utf-8 -*-
"""
Created on Wed Jan 02 19:27:13 2013
 
@author: Mark
"""
 
import win32api
import sys
import time
 
from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QPoint
from PyQt4 import QtCore
 
class MouseRecord(QtCore.QObject):
   
    finished = QtCore.pyqtSignal()    
   
    def __init__(self):
       
        super(MouseRecord, self).__init__()        
       
        self.isRecording = False
        self.cursorPath = []
   
    @QtCore.pyqtSlot()  
    def record(self):
   
        self.isRecording = True
        self.cursorPath = []
       
        while(self.isRecording):
       
            self.cursorPath.append(win32api.GetCursorPos())
            time.sleep(.02)            
           
        self.finished.emit()
   
    def stop(self):
   
        self.isRecording = False
   
    @QtCore.pyqtSlot()    
    def play(self):
       
        for pos in self.cursorPath:
            win32api.SetCursorPos(pos)
            time.sleep(.02)        
           
        print "Playback complete!"
        self.finished.emit()            
       
 
class CursorCapture(QtGui.QWidget):
   
    def __init__(self):
       
        super(CursorCapture, self).__init__()
       
        self.isRecording = False
        self.mouseRecorder = MouseRecord()
       
        self.myThread = QtCore.QThread()
               
        self.mouseRecorder.moveToThread(self.myThread)
        self.mouseRecorder.finished.connect(self.myThread.quit)
                       
        self.initUI()
       
    def initUI(self):
       
        recordPix = QtGui.QPixmap(20, 20)
        stopPix   = QtGui.QPixmap(20, 20)
        playPix   = QtGui.QPixmap(20, 20)
       
        recordPix.fill(Qt.transparent)
        stopPix.fill(Qt.transparent)
        playPix.fill(Qt.transparent)
       
        painter = QtGui.QPainter()
       
        painter.begin(recordPix)
        painter.setBrush(Qt.red)
        painter.drawEllipse(5, 5, 10, 10)
        painter.end()
       
        painter.begin(stopPix)
        painter.setBrush(Qt.blue)
        painter.drawRect(5, 5, 10, 10)
        painter.end()
       
        painter.begin(playPix)
        painter.setBrush(Qt.green)
        painter.drawPolygon(QPoint(5, 5), QPoint(15, 10), QPoint(5, 15))
        painter.end()
       
        recordIcon = QtGui.QIcon(recordPix)
        stopIcon = QtGui.QIcon(stopPix)
        playIcon = QtGui.QIcon(playPix)
       
        self.recordBtn = QtGui.QPushButton(recordIcon, "&Record")
        self.stopBtn   = QtGui.QPushButton(stopIcon, "&Stop")
        self.playBtn   = QtGui.QPushButton(playIcon, "&Play")        
       
        self.recordBtn.clicked.connect(self.record())
        self.stopBtn.clicked.connect(self.stop)
        self.playBtn.clicked.connect(self.play)
       
        self.stateLabel = QtGui.QLabel("Status: Stopped.")
       
        self.vLayout = QtGui.QVBoxLayout()
        self.hLayout = QtGui.QHBoxLayout()
       
        self.hLayout.addWidget(self.recordBtn)
        self.hLayout.addWidget(self.stopBtn)        
        self.hLayout.addWidget(self.playBtn)
       
        self.vLayout.addLayout(self.hLayout)        
        self.vLayout.addWidget(self.stateLabel)
       
        self.setLayout(self.vLayout)
       
        self.setWindowTitle("Cursor Capture")
        self.show()
       
        def record(self):
           
            self.stateLabel.setText("Status: Recording ...")  
     
            self.myThread.started.connect(self.mouseRecorder.record)
            self.myThread.start()
            time.sleep(.005)        
     
            self.myThread.started.disconnect()
           
        def stop(self):
           
            self.mouseRecorder.stop()
            self.stateLabel.setText("Status: Stopped.")
     
        def play(self):
           
            self.stateLabel.setText("Status: Playback initated ...")
           
            self.myThread.started.connect(self.mouseRecorder.play)
            self.myThread.start()
            time.sleep(.005)
     
            self.myThread.started.disconnect()
       
 
def main():
 
    qApp = QtGui.QApplication(sys.argv)
   
    cursorCapture = CursorCapture()
   
    sys.exit(qApp.exec_())
           
if __name__ == "__main__":
    main()
