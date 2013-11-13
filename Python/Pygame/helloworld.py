# -*- coding: utf-8 -*-
"""
Created on Sat Nov 09 18:07:03 2013

@author: NotMark
"""

import pygame

pygame.init()

screenWidth = 600
screenHeight = 600

screenSize = (screenWidth, screenHeight)

screen = pygame.display.set_mode(screenSize)

gameOn = True

gameClock = pygame.time.Clock()

def handleEvents():
    
    global gameOn
    
    for event in pygame.event.get():
        
        eType = event.type        
        
        if eType == pygame.QUIT:
            gameOn = False
        elif eType == pygame.KEYDOWN:
            print 'User pressed a goddamn key'
        elif eType == pygame.KEYUP:
            print 'Key released'
        elif eType == pygame.MOUSEBUTTONDOWN:
            print 'User pressed mouse'
            
def drawBoardSquare(x, y, width = 80, slotWidth = 10):
    
    pygame.draw.rect(screen, (120, 120, 120), [x, y, width, width])
    pygame.draw.rect(screen, (200, 200, 200), [x, y, width - slotWidth, 
                                                 width - slotWidth])
    
class Pawn(object):
    
    pawnColor = (0, 0 ,0)
    
    def __init__(self, _x, _y, _radius, _playerNumber):
        
        self.x = _x
        self.y = _y
        self.r = _radius
        self.playerNumber = _playerNumber
        
    def setPosition(self, _x, _y):
        
        self.x = _x
        self.y = _y

    def draw(self):
        
        pygame.draw.circle(screen, self.pawnColor, 
                               [self.x, self.y], self.r)

class BoardSquare(object):
    
    def __init__(self, _x, _y, _width, _slotWidth, _spaceColor, _slotColor):
        
        self.x = _x
        self.y = _y
        self.width = _width
        self.slotWidth = _slotWidth
        self.spaceColor = self.defaultSpaceColor = _spaceColor
        self.slotColor = _slotColor
        
        self.isMouseInside = False
        
    def draw(self):
        
        squareSpace = self.width - self.slotWidth       
        
        if self.isMouseInside == True:
            self.spaceColor = (255, 120, 120)
        else:
            self.spaceColor = self.defaultSpaceColor
        
        pygame.draw.rect(screen, self.slotColor, 
                             [self.x, self.y, self.width, self.width])
                                                   
        pygame.draw.rect(screen, self.spaceColor, 
                             [self.x, self.y, squareSpace, squareSpace])
                             
    
    def setSpaceColor(self, color):
        self.spaceColor = color
        
    def testMouseInside(self, mouseX, mouseY):
        
        print mouseX, mouseY
        
        if mouseX > self.x:
            #print '1'
            if mouseY > self.y:
                #print '2'
                if mouseX < (self.x + self.width):
                    #print '3'
                    if mouseY < (self.y + self.width):

                        self.isMouseInside = True
        else:               
            
            self.isMouseInside = False
            
    def getCenterPos(self):

        halfSquareSpace = int((self.width - self.slotWidth) / 2.0)
        
        return (self.x + halfSquareSpace, self.y + halfSquareSpace)

def createBoard(x, y, numSquares = 9, squareWidth = 60, slotWidth = 6,
                    spaceColor = (200, 200, 255), slotColor = (120, 120, 160)):

    squareList = []
    for i in range(numSquares):
        for j in range(numSquares):      
        
            squareList.append(BoardSquare(x + j * squareWidth, 
                                          y + i * squareWidth, 
                                          squareWidth, 
                                          slotWidth, 
                                          spaceColor,
                                          slotColor))

    return squareList
    
player1 = Pawn(297, 537, 20, 1)
player2 = Pawn(0, 0, 20, 2)
                             
while gameOn == True:
    
    handleEvents() 
        
    screen.fill((120, 120, 120))
    gameBoard = createBoard(30, 30)
    
    for square in gameBoard:
        square.testMouseInside(*pygame.mouse.get_pos())
        square.draw()
        
    col1 = 5
    row1 = 9
    
    col2 = 5
    row2 = 1
    
    
    pos1 = gameBoard[col1-1 + (row1-1)*9].getCenterPos()
    pos2 = gameBoard[col2-1 + (row2-1)*9].getCenterPos()
        
    player1.setPosition(*pos1)
    player2.setPosition(*pos2)
    
    player1.draw()
    player2.draw()

    pygame.display.flip()    
    
    gameClock.tick(30)

pygame.quit()