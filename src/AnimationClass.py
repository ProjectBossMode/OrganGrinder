'''
Created on Jan 26, 2013

@author: Reza
'''
import sys, pygame, os, Const

pygame.init()

class Animation:

    def __init__(self, spriteSheet, numFrames, frameWidth, frameHeight, timePerFrame = 10):
        self.spriteList = []
        self.currentFrameNum = 0
        self.timePerFrame = timePerFrame
        self.totalFrames = numFrames
        self.imageFlipped = False
        self.currentFrameTime = 0
        self.MakeAnimation(spriteSheet, numFrames, frameWidth, frameHeight)
        
    def MakeAnimation(self, spriteSheet, numFrames, frameWidth, frameHeight):
        for frame in range(numFrames):
            self.spriteList.append(spriteSheet.subsurface(0, (frame * frameHeight), frameWidth, frameHeight))
    
    def GetCurrentFrameNum(self):
        return self.currentFrameNum        
    
    def FlipImage(self, shouldFlip):
        self.imageFlipped = shouldFlip
    
    def Update(self):
        if self.currentFrameTime >= self.timePerFrame:
            self.currentFrameTime = -1
            self.currentFrameNum += 1
            if self.currentFrameNum >= self.totalFrames:
                self.currentFrameNum = 0
                return True
        self.currentFrameTime += 1
        return False
        
    def ChangeTimePerFrame(self, timePerFrame):
        self.timePerFrame = timePerFrame
            
    def Draw(self, displaySurf, location):
        if self.imageFlipped == False:
            displaySurf.blit(self.spriteList[self.currentFrameNum], location)
        else:
            displaySurf.blit(pygame.transform.flip(self.spriteList[self.currentFrameNum], True, False) , location)