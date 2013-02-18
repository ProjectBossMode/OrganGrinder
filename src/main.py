'''
Created on Jan 26, 2013

@author: Reza
'''

import pygame, sys, MapClass, Const
from MapClass import Map 
from pygame.locals import *
 
pygame.init()

FPS = 60
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((Const.WINDOWWIDTH, Const.WINDOWHEIGHT)) 
pygame.mixer.music.load(Const.BGMUSIC_FN)

def main():
    map = Map()
    gamePlaying = True
    gameState = Const.TITLE
    lastKeyPressed = None
    
    pygame.mixer.music.play(-1)       
    
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                lastKeyPressed = event.key
        
        if gameState == Const.TITLE:
            DISPLAYSURF.blit(Const.TITLESCREEN, (0,0))
            if lastKeyPressed == K_SPACE:
                gameState = Const.PLAYING
        elif gameState == Const.PLAYING:
            gamePlaying = map.Update(lastKeyPressed)   
            map.Draw(DISPLAYSURF)
            if gamePlaying == False:
                gameState = Const.GAMEOVER
        elif gameState == Const.GAMEOVER:
            pygame.mixer.music.pause()
            DISPLAYSURF.blit(Const.GAMEOVERSCREEN, (0,0))
            
        pygame.display.update()
        lastKeyPressed = None
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()