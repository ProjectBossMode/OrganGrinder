'''
Created on Jan 27, 2013

@author: Jeff Einspahr
'''
import pygame, AnimationClass, PlayerClass, Const
from AnimationClass import Animation
from pygame.locals import *

class UI:
    

    def __init__(self, listSpriteSheet, location):
        self.animationList = []
        self.location = location
        
        self.animationList.append(Animation(Const.HEARTEMPTY, Const.HEARTFRAME, Const.HEARTWIDTH, Const.HEARTHEIGHT))
        self.animationList.append(Animation(Const.HEARTTHREEHITS, Const.HEARTFRAME, Const.HEARTWIDTH, Const.HEARTHEIGHT))
        self.animationList.append(Animation(Const.HEARTTWOHITS, Const.HEARTFRAME, Const.HEARTWIDTH, Const.HEARTHEIGHT))
        self.animationList.append(Animation(Const.HEARTONEHIT, Const.HEARTFRAME, Const.HEARTWIDTH, Const.HEARTHEIGHT))
        self.animationList.append(Animation(Const.HEARTFULL, Const.HEARTFRAME, Const.HEARTWIDTH, Const.HEARTHEIGHT))
        
        self.currentAnimation = self.animationList[4]
        
    def Update(self, playerHealth):
        self.currentAnimation = self.animationList[playerHealth]
        
        
    def Draw(self, displaySurf):
        self.currentAnimation.Draw(displaySurf, self.location)