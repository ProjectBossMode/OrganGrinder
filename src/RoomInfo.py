'''
Created on Jan 26, 2013

@author: Reza
'''

import DoorClass, Const, pygame, PlatformClass, EnemyClass
from EnemyClass import Enemy
from DoorClass import Door
from PlatformClass import Platform
pygame.init()


### ROOM 1 ####          doorList, lockList, enemyList, roomNum, roomSpriteSheet
ROOM1 = []       
    ### DOOR LIST ###        spriteSheet, location, lockStatus, doorNum, connectingDoorNum, connectingRoomNum
DOOR1 = []
temp = Door(Const.DOORIMG, (0, 530), False, 2, 1, 2)
DOOR1.append(temp)

    ### LOCK LIST ###
LOCK1 = []    

    ### ENEMY LIST ###
ENEMY1 = []    

    ### ROOM NUM ###
roomNum = 1      

    ### ROOM IMG ###
roomImg = pygame.image.load(Const.ROOM1_FN)

    ### PLATFORM LIST ###
PLATFORM1 = []
temp = Platform((0, Const.ROOMHEIGHT - 35), (Const.ROOMWIDTH, 50))
PLAYFORM1 = PLATFORM1.append(temp)

ROOM1 = [DOOR1, LOCK1, ENEMY1, roomNum, roomImg, PLATFORM1]
###############################################################################

### ROOM 2 ###
ROOM2 = []
    ### DOOR LIST ###
DOOR2 = []
temp = Door(Const.DOORIMG, (0, 530), False, 2, 1, 3)
DOOR2.append(temp)
temp = Door(Const.DOORIMG, (Const.ROOMWIDTH - Const.DOORWIDTH, 530), False, 1, 2, 1)
DOOR2.append(temp)

    ### LOCK LIST ###
LOCK2 = []

    ### ENEMY LIST ### listSpriteSheet

ENEMY2 = []
temp = Enemy(Const.ENEMYWALKSPRITESHEET, [100, 700])
ENEMY2.append(temp)
    ### ROOM NUM ###
roomNum = 2

    ### ROOM IMG ###
roomImg = pygame.image.load(Const.ROOM2_FN)

    ### PLATFORM LIST ###
PLATFORM2 = []
temp = Platform((0, Const.ROOMHEIGHT - 35), (Const.ROOMWIDTH, 50))
PLAYFORM2 = PLATFORM2.append(temp)

ROOM2 = [DOOR2, LOCK2, ENEMY2, roomNum, roomImg, PLATFORM1]
###############################################################################
###############################################################################

### ROOM 3 ###
ROOM3 = []
    ### DOOR LIST ###
DOOR3 = []
temp = Door(Const.DOORIMG, (Const.ROOMWIDTH - Const.DOORWIDTH, 530), False, 1, 2, 2)
DOOR3.append(temp)

    ### LOCK LIST ###
LOCK3 = []

    ### ENEMY LIST ### listSpriteSheet

ENEMY3 = []
temp = Enemy(Const.ENEMYWALKSPRITESHEET, [30, 700])
ENEMY3.append(temp)
    ### ROOM NUM ###
roomNum = 2

    ### ROOM IMG ###
roomImg = pygame.image.load(Const.ROOM3_FN)

    ### PLATFORM LIST ###
PLATFORM3 = []
temp = Platform((0, Const.ROOMHEIGHT - 35), (Const.ROOMWIDTH, 50))
PLAYFORM3 = PLATFORM2.append(temp)

ROOM3 = [DOOR3, LOCK3, ENEMY3, roomNum, roomImg, PLATFORM1]
###############################################################################
    