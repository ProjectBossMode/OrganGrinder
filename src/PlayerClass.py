'''
Created on Jan 26, 2013

@author: Jeff Einspahr
'''
import pygame, AnimationClass, Const
from AnimationClass import Animation
from pygame.locals import *

pygame.init()

class Player:

    def __init__(self, listSpriteSheet):
        self.animationList = []
        self.currentHealth = 4
        self.attackAdjust = False
        self.currentKnockBackTime = 0
        self.currentGravity = 0
        self.currentJumpTime = 0
        self.knockedBack = False
        self.flipImage = False
        self.isJumping = True
        self.isAttacking = False
        self.lastKeyPressed = None
        self.location = [1000, 700]
        self.index = 0
        self.dirFacing = Const.LEFT
        self.charHeight = Const.CHARHEIGHT
        self.animationList.append(Animation(Const.PLAYERIDLESPRITE, Const.NUMCHARIDLEFRAMES, Const.CHARWIDTH, Const.CHARHEIGHT, 10))
        self.animationList.append(Animation(Const.PLAYERWALKSPRITE, Const.NUMCHARMOVINGHFRAMES, Const.CHARWIDTH, Const.CHARHEIGHT, 7))
        self.animationList.append(Animation(Const.PLAYERWALKSPRITE, Const.NUMCHARMOVINGHFRAMES, Const.CHARWIDTH, Const.CHARHEIGHT))
        self.animationList.append(Animation(Const.PLAYERATTACKSPRITE, Const.NUMCHARATTACKINGFRAMES, Const.CHARATTACKWIDTH, Const.CHARATTACKHEIGHT, 5))
        self.currentAnimation = self.animationList[0]
        
    def Attack(self, lastKeyPressed):
        if self.lastKeyPressed == K_z and self.isJumping == False:
            self.attackAdjust = True            
            if self.dirFacing == Const.LEFT:
                self.ChangeLocation((self.location[0]-Const.PLAYERHURTBOXADJUSTMENT, self.location[1]))
                self.currentAnimation = self.animationList[3]
                self.isAttacking = True
            elif self.dirFacing == Const.RIGHT:
                #self.ChangeLocation((self.location[0]+Const.PLAYERHURTBOXADJUSTMENT, self.location[1]))
                self.currentAnimation = self.animationList[3]
                self.isAttacking = True
                
            #add hurt box here :)
            
    def GetHeight(self):
        return self.charHeight
            
    def Move(self, lastKeyPressed):
        self.currentAnimation.FlipImage(self.flipImage)
        
        if pygame.key.get_pressed()[K_LEFT]:
            self.dirFacing = Const.LEFT
            self.currentAnimation = self.animationList[1]
            self.ChangeLocation(((self.location[0] - Const.MOVEMENT), self.location[1]))
        elif pygame.key.get_pressed()[K_RIGHT]:
            self.dirFacing = Const.RIGHT
            self.currentAnimation = self.animationList[1]
            self.ChangeLocation(((self.location[0] + Const.MOVEMENT), self.location[1]))        
        else:
            self.currentAnimation = self.animationList[0]
            
        self.CheckOutOfBounds()
            
        if lastKeyPressed == K_SPACE and self.isJumping == False:
            self.Jump()
    
    def CheckOutOfBounds(self):
        if (self.location[0] + Const.CHARWIDTH) >= (Const.ROOMWIDTH - 30):
            self.ChangeLocation(((Const.ROOMWIDTH - Const.CHARWIDTH - 30), self.location[1]))
        
        if self.location[0] <= 30:
            self.ChangeLocation((30, self.location[1]))
    
    def FlipSprite(self):
        if self.dirFacing == Const.LEFT:
            self.currentAnimation.FlipImage(False)
        if self.dirFacing == Const.RIGHT:
            self.currentAnimation.FlipImage(True)
    
    def ChangeLocation(self, location):    
        self.location = location
    
    def Jump(self):
        self.isJumping = True
        self.currentGravity = -(Const.MAXGRAV)
        
    def ApplyGravity(self):
        if self.isJumping == False:
            self.currentGravity = 0
            return
        else:
            self.currentGravity += 1
            if self.currentGravity >= Const.MAXGRAV:
                self.currentGravity = Const.MAXGRAV
            self.ChangeLocation((self.location[0], (self.location[1] + self.currentGravity)))
            
    def Update(self, lastKeyPressed):
        self.lastKeyPressed = lastKeyPressed
        if self.currentAnimation.Update() == False and self.isAttacking == True:
            self.index += 1
            return
        else:
            if self.isAttacking == True and self.attackAdjust == True:
                self.attackAdjust = False
                self.isAttacking = False
                self.currentAnimation = self.animationList[0]
                if self.dirFacing == Const.LEFT:
                    self.ChangeLocation((self.location[0]+Const.PLAYERHURTBOXADJUSTMENT, self.location[1]))
                #elif self.dirFacing == Const.RIGHT:
                    #doesnt need adjustment
                    #break
            if self.knockedBack:
                self.isAttacking = False
                self.Knockback()
                self.ApplyGravity()
                self.FlipSprite()
            else:
                self.currentAnimation.Update()
                self.Move(lastKeyPressed)
                self.isAttacking = False
                self.Attack(lastKeyPressed)
                self.ApplyGravity()
                self.FlipSprite()
            
        self.lastKeyPressed = None
                             
    def Knockback(self):
        if self.isJumping == False:
            self.currentHealth -= 1
            if self.currentHealth <= 0:
                self.currentHealth = 0
            self.knockedBack = False
        else:
            self.ChangeLocation(((self.location[0] + Const.KNOCKBACKDISTANCE), self.location[1]))
            self.CheckOutOfBounds()
            
                                                
    def GetHitBox(self):
        if self.isAttacking == False or self.dirFacing == Const.RIGHT:
            return pygame.Rect((self.location), (Const.CHARWIDTH, Const.CHARHEIGHT))
        if self.isAttacking == True and self.dirFacing == Const.LEFT:
            return pygame.Rect(((self.location[0] + Const.PLAYERHURTBOXADJUSTMENT), self.location[1]), (Const.CHARWIDTH, Const.CHARHEIGHT))
            
    def GetHurtBox(self):
        if self.dirFacing == Const.LEFT:
            return pygame.Rect((self.location[0] - Const.PLAYERHURTBOXADJUSTMENT, self.location[1]), (Const.PLAYERHURTBOXWIDTH, Const.PLAYERHURTBOXWIDTH))
        if self.dirFacing == Const.RIGHT:
            return pygame.Rect((self.location[0] + Const.PLAYERHURTBOXADJUSTMENT + Const.CHARWIDTH, self.location[1]), (Const.PLAYERHURTBOXWIDTH, Const.PLAYERHURTBOXWIDTH))
    
    def Draw(self, displaySurf):
        self.currentAnimation.Draw(displaySurf, self.location)
            
        