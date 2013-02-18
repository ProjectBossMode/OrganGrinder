'''
Created on Jan 26, 2013

@author: Reza
'''
import pygame, AnimationClass, Const
from AnimationClass import Animation

pygame.init()

class Lock:

    def __init__(self, location, unlockSprite, lockSprite, key, doorNum):
        self.location = location
        self.keyType = key
        self.unlockDoorNum = doorNum
        self.lockedStatus = True
        self.unlockAnimation = Animation(unlockSprite, \
                                         Const.NUMLOCKFRAMESLOCKED, \
                                         Const.LOCKWIDTH, Const.LOCKHEIGHT)
        self.lockAnimation = Animation(lockSprite, \
                                         Const.NUMLOCKFRAMESLOCKED, \
                                         Const.LOCKWIDTH, Const.LOCKHEIGHT)
        
    def Unlock(self, invList):
        for key in invList:
            if key == self.keyType and self.lockedStatus == True:
                self.lockedStatus = False
                return self.unlockDoorNum
        return None
    
    def Update(self):
        if self.lockStatus == True:
            self.lockAnimation.Update()
        else:
            self.unlockAnimation.Update()
    
    def Draw(self, displaySurf):
        if self.lockStatus == True:
            self.lockAnimation.Draw(displaySurf, self.location)
        else:
            self.unlockAnimation.Draw(displaySurf, self.location)
            
    def GetRect(self):
        return pygame.rect((self.location), (Const.LOCKWIDTH, Const.LOCKHEIGHT))
    
    
    