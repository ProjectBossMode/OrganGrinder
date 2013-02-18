'''
Created on Jan 26, 2013

@author: Jeff Einspahr
'''
import pygame, AnimationClass, Const, random
from AnimationClass import Animation
from pygame.locals import *
from random import *

class Enemy:

    def __init__(self, listSpriteSheet, location):
        self.animationList = []
        self.isJumping = True
        self.currentWaitTime = 0
        self.currentGravity = 0
        self.isAttacking = False
        self.currentgravity = 0
        self.location = location
        self.enemyHeight = Const.ENEMYHEIGHT
        self.currentPatrolDirection = randint(0,1)
        self.patrolDistance = 0
        self.animationList.append(Animation(Const.ENEMYWALKSPRITESHEET, Const.ENEMYMOVINGFRAMES, Const.ENEMYWIDTH, Const.ENEMYHEIGHT))
        self.currentAnimation = self.animationList[0]

    def GetHeight(self):
        return self.enemyHeight

    def GetLocation(self):
        return [self.location[0], self.location[1]]
    
    def SeekPlayer(self, player):
        self.currentAnimation.ChangeTimePerFrame(5)
        if self.location[0] < player.location[0]:
            self.currentAnimation.FlipImage(False)
            self.location[0] += Const.ENEMYSEEKSPEED
            self.flipImage = False
            if self.location[0] <= 30:
                self.location[0] = 30
        if self.location[0] > player.location[0]:
            self.currentAnimation.FlipImage(True)
            self.location[0] -= Const.ENEMYSEEKSPEED
            self.flipImage = False
            if (self.location[0] + Const.CHARWIDTH) >= (Const.ROOMWIDTH - 30):
                self.location[0] = Const.ROOMWIDTH - Const.CHARWIDTH - 30
    
    def Wait(self):
        if self.currentWaitTime >= Const.WAITTIME:
            self.currentWaitTime = 0
            return True
        else:
            self.currentWaitTime += 1
            return False
    
    def Patrol(self):
        self.currentAnimation.ChangeTimePerFrame(10)
        if self.patrolDistance <= 0:
            if self.Wait():
                if self.currentPatrolDirection == 0:
                    self.currentPatrolDirection = 1
                else:
                    self.currentPatrolDirection = 0
                    
                self.patrolDistance = randint(100,175)
        else:
            if self.currentPatrolDirection == 0:
                self.currentAnimation.FlipImage(True)
                self.location[0] -= Const.ENEMYPATROLSPEED
                if self.location[0] <= 30:
                    self.location[0] = 30
            else:
                self.currentAnimation.FlipImage(False)
                self.location[0] += Const.ENEMYPATROLSPEED
                if self.location[0] >= Const.ROOMWIDTH - Const.ENEMYWIDTH - 30:
                    self.location[0] = Const.ROOMWIDTH - Const.ENEMYWIDTH - 30
            
            self.patrolDistance -= Const.ENEMYPATROLSPEED
        
    def CheckState(self, player):
        if player.knockedBack == False:
            if self.location[0] < player.location[0] and player.location[0] - self.location [0] < Const.SEEKDISTANCE:
                self.SeekPlayer(player)
                return
            elif self.location[0] > player.location[0] and self.location[0] - player.location [0] < Const.SEEKDISTANCE:
                self.SeekPlayer(player)
                return

        self.Patrol()
    
    def ChangeLocation(self, location):
        self.location[0] = location[0]
        self.location[1] = location[1]
    
    def ApplyGravity(self):
        if self.isJumping == False:
            self.currentGravity = 0
            return
        else:
            self.currentGravity += 1
            if self.currentGravity >= Const.MAXGRAV:
                self.currentGravity = Const.MAXGRAV
            self.location[1] = (self.location[1] + self.currentGravity)       
    
    def GetHitBox(self):
        return pygame.Rect((self.location), (Const.ENEMYWIDTH, Const.ENEMYHEIGHT))
    
    def Update(self, player):
        if self.location[1] > 0:
            self.CheckState(player)
            self.ApplyGravity()
            self.currentAnimation.Update()
        
        
    def Draw(self, displaySurf):
        self.currentAnimation.Draw(displaySurf, self.location)
            