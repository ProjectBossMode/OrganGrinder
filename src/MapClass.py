'''
Created on Jan 26, 2013

@author: Reza
'''

import pygame, sys, RoomClass, PlayerClass, DoorClass, LockClass, Const, RoomInfo, copy, UIClass
from UIClass import UI
from RoomClass import Room
from PlayerClass import Player
from DoorClass import Door
from LockClass import Lock

pygame.init()

playerSpriteSheetList = [Const.PLAYERIDLESPRITE, Const.PLAYERWALKSPRITE, Const.PLAYERATTACKSPRITE]

class Map:
    

    
    def __init__(self):
        self.roomList = []
        self.ui = UI(Const.HEARTFULL, (50, 50))
        self.roomList.append(RoomInfo.ROOM1)
        self.roomList.append(RoomInfo.ROOM2)
        self.roomList.append(RoomInfo.ROOM3)
        
        self.player = Player(playerSpriteSheetList)
        self.currentRoom = None
        self.previousRoom = None
        self.firstCall = True
        self.SwitchRoom(1)
    
    def SwitchRoom(self, roomNum):
        if self.firstCall == True:
            self.currentRoom =  Room(self.roomList[roomNum - 1])
            self.firstCall = False
            
        if self.previousRoom != None:
            self.previousRoom = self.currentRoom
            self.previousRoom.DeleteRoom()
            self.currentRoom =  Room(self.roomList[roomNum - 1])
            self.previousRoom = None
        
    def Update(self, lastKeyPressed):
        nextRoom = self.currentRoom.Update(self.player, lastKeyPressed)
        self.ui.Update(self.player.currentHealth)
        if nextRoom != None:
            self.previousRoom = self.currentRoom
            self.SwitchRoom(nextRoom[0])
            
            if nextRoom[1] == 2:
                self.player.ChangeLocation((0,self.player.location[1]))
            elif nextRoom[1] == 1:
                self.player.ChangeLocation((1300, self.player.location[1]))
                
            """
            if len(self.currentRoom.roomDoors) >= 1:
                self.player.ChangeLocation(((self.currentRoom.roomDoors[nextRoom[1] - 1].GetLocation()[0]), self.player.location[1]))
            else:
                self.player.ChangeLocation(((self.currentRoom.roomDoors[0].GetLocation()[0]), self.player.location[1]))
            """
            
        return self.player.currentHealth
            
    
    def Draw(self, displaySurf):
        self.currentRoom.Draw(displaySurf)
        self.player.Draw(displaySurf)
        self.ui.Draw(displaySurf)