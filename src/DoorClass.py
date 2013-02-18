'''
Created on Jan 26, 2013

@author: Reza
'''
import sys, pygame, os, AnimationClass, Const
from pygame.locals import *
from AnimationClass import Animation

pygame.init()

class Door:
    
    def __init__(self, spriteSheet, location, lockStatus, doorNum, \
                 connectingDoorNum, connectingRoomNum):
        self.location = location
        self.lockedStatus = lockStatus
        self.doorNumber = doorNum
        self.connectingDoorNum = connectingDoorNum
        self.connectingRoomNum = connectingRoomNum
        self.doorAnimation = Animation(spriteSheet, Const.NUMDOORFRAMESCLOSED, \
                                       Const.DOORWIDTH, Const.DOORHEIGHT)
        
    def GetLocation(self):
        return self.location
    
    def GetDestination(self):
        return (self.connectingRoomNum, self.connectingDoorNum)
    
    def IsLocked(self):
        return self.lockedStatus
    
    def Unlock(self):
        self.lockedStatus = False
        
    def GetDoorNumber(self):
        return self.doorNumber
    
    def GetDoorRect(self):
        return pygame.Rect((self.location), (Const.DOORWIDTH, Const.DOORHEIGHT))
    
    def Update(self):
        self.doorAnimation.Update()
        
    def Draw(self, displaySurf):
        self.doorAnimation.Draw(displaySurf, self.location)