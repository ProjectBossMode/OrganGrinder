'''
Created on Jan 26, 2013

@author: Reza
'''
import pygame, Const
pygame.init()


class Platform:

    def __init__(self, location, size):
        self.location = location
        self.size = size
        self.collisionRectangle = pygame.Rect((location), (size))
    
    def CheckRectangleCollision(self, rectangle1, rectangle2):
        if rectangle1.colliderect(rectangle2):
            return True
        else:
            return False
        
    def CheckCollision(self, player):

        if player.location[1] + player.GetHeight() >= self.location[1] and self.CheckRectangleCollision(player.GetHitBox(), self.collisionRectangle):
            player.ChangeLocation((player.location[0], (self.location[1] - player.GetHeight() + 5)))
            return True
        else:
            return False
        
      