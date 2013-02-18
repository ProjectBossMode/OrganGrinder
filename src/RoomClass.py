'''
Created on Jan 26, 2013

@author: Reza
'''
import sys, pygame, DoorClass, AnimationClass, LockClass, Const
from DoorClass import Door
from AnimationClass import Animation
from LockClass import Lock
from pygame.locals import *

pygame.init()

class Room:

    def __init__(self, roomInfo):
        """
        ORDER OR roomINFO
        
        doorList, lockList, enemyList, roomNum, roomSpriteSheet
        """
        self.room2loc = []
        self.initalEnemyLoc = []
        self.roomDoors = roomInfo[0]
        self.roomLocks = roomInfo[1]
        self.enemyList = roomInfo[2]
        self.roomNum = roomInfo[3]
        self.roomAnimation = Animation(roomInfo[4], Const.NUMROOMFRAMES, Const.ROOMWIDTH, Const.ROOMHEIGHT)
        self.floorList = roomInfo[5]
        self.GetInitialEnemyLocations()
        
        
    
    """    
    def SetUpRoom(self, doorList, lockList, enemyList):
        for door in doorList:
            self.roomDoors.append(Door(door[0], door[1], door[2], door[3], \
                 door[4], door[5]))
            
        for lock in lockList:
            self.roomLocks.append(Lock(lock[0], lock[1], lock[2], lock[3], \
                                     lock[4]))
      
        for enemy in enemyList:
            self.enemyList.append(Enemy(enemy[0], enemy[1], enemy[2], enemy[3]))
    """
    def GetInitialEnemyLocations(self):
        for enemy in self.enemyList:
            self.initalEnemyLoc.append(enemy.GetLocation())
            
    
    def Draw(self, displaySurf):
        self.roomAnimation.Draw(displaySurf, Const.BACKGROUNDLOCATION)
        
        for door in self.roomDoors:
            door.Draw(displaySurf)
    
        for lock in self.roomLocks:
            lock.Draw(displaySurf)
        
        for enemy in self.enemyList:
            enemy.Draw(displaySurf)

        """
        for enemy in self.enemyList:
            enemy.Draw(displaySurf)
        """
    def CheckCollision(self, rectangle1, rectangle2):
        if rectangle1.colliderect(rectangle2):
            return True
        else:
            return False
    
    """
    def CheckLockCollision(self, player):
        for lock in self.roomLocks:
            if self.CheckCollision(lock.GetRect(), player.GetRect()) and \
                player.lastKeyPressed == K_UP and lock.lockedStatus == True:
                doorToUnlock = lock.Unlock(player.inv)
                if doorToUnlock != None:
                    for doors in self.roomDoors:
                        if doorToUnlock == doors.GetDoorNum:
                            doors.Unlock()
    """                     
    def CheckDoorCollision(self, player, lastKeyPressed):
        for door in self.roomDoors:
            if self.CheckCollision(door.GetDoorRect(), player.GetHitBox()):
                if lastKeyPressed == K_UP and door.IsLocked() == False:
                    return door.GetDestination()
        return None
    
    def CheckPlayerAttackCollision(self, player):
        numHits = 0
        if player.isAttacking == True and player.currentAnimation.GetCurrentFrameNum() >= 2:
            for enemy in self.enemyList:
                if self.CheckCollision(enemy.GetHitBox(), player.GetHurtBox()):
                    enemy.ChangeLocation((0,0))
                    numHits += 1
        
        
        return numHits
                
    
    def UpdateDoors(self):
        for door in self.roomDoors:
            door.Update()
            
    def UpdateLocks(self):
        for lock in self.roomLocks:
            lock.Update()
            
    def UpdateEnemies(self, player):
        for enemy in self.enemyList:
            enemy.Update(player)
        
    
    def DeleteRoom(self):
        self.ResetEnemyLocations()
        self.enemyList = []
        del self.roomDoors
        del self.roomLocks
        del self.roomAnimation
        del self.roomNum
        
    def ResetEnemyLocations(self):
        index = 0
        for enemy in self.enemyList:
            enemy.location = self.initalEnemyLoc[index]
            index += 1
            
    def CheckEnemyCollision(self, player):
        for enemy in self.enemyList:
            if self.CheckCollision(enemy.GetHitBox(), player.GetHitBox()):
                player.knockedBack = True
                player.Jump()
        
    def Update(self, player, lastKeyPressed):
        self.roomAnimation.Update()
        self.UpdateDoors()
        self.UpdateLocks()
        self.UpdateEnemies(player)
        player.Update(lastKeyPressed)
        
        for floor in self.floorList:
            for enemy in self.enemyList:
                if floor.CheckCollision(enemy):
                    enemy.isJumping = False
                else:
                    enemy.isJumping = True
        
        for floor in self.floorList:
            if floor.CheckCollision(player):
                player.isJumping = False
            else:
                player.isJumping = True
        
        if self.CheckPlayerAttackCollision(player) <= 0:
            self.CheckEnemyCollision(player)
        
        #self.CheckEnemyColision(player)
        #self.CheckLockCollision(player)
        return self.CheckDoorCollision(player, lastKeyPressed)
        
        
                   
             