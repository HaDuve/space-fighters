#!/usr/bin/env python
import sys
import pygame
import math
import main2players
import main3players
import main4players
from pygame.locals import *

#INITIALIZE
SCREENWIDTH = 800
SCREENHEIGHT= 600
pygame.init()
DISPLAY = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("SpaceFighters")
pygame.display.set_icon(pygame.image.load('resources/ship1.png'))
fpsClock = pygame.time.Clock()
pygame.mouse.set_visible(0)
pygame.key.set_repeat(100, 100)
CURSOR_ROW = 1
CURSOR   = pygame.image.load('resources/cursor.png')

#CONSTANTS

#Fonts
BIGFONT = pygame.font.Font('font.ttf', 30)
FONT = pygame.font.Font('font.ttf', 16)
SMALLFONT = pygame.font.Font('font.ttf', 9)

#TEXTURES
BACKGROUND = pygame.image.load('resources/background.png')
SHIP1   = pygame.image.load('resources/ship1.png')
SHIP2   = pygame.image.load('resources/ship2.png')
SHIP3   = pygame.image.load('resources/ship3.png')
SHIP4   = pygame.image.load('resources/ship4.png')

#representing colours
BLACK =(0,0,0)
WHITE =(255,255,255)
BLUE =(100,115,175)
RED =(176,52,52)
GREEN =(84,155,70)

#STATS to be modified and imported
#[ShipSpeed, Maneuverability, RocketSpeed, #open]
STATS1 = [0,0,0,0]
STATS2 = [0,0,0,0]
STATS3 = [0,0,0,0]
STATS4 = [0,0,0,0]


def choose_mode(playercount, player = 1):
    while 1:
        global CURSOR_ROW
        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND,(0,0))

        if player == 1:
            DISPLAY.blit(SHIP1,(180,550))
        if player == 2:
            DISPLAY.blit(SHIP2,(180,550))
        if player == 3:
            DISPLAY.blit(SHIP3,(180,550))
        if player == 4:
            DISPLAY.blit(SHIP4,(180,550))


        DISPLAY.blit(CURSOR,(120,CURSOR_ROW*SCREENHEIGHT/15+100))
        
        for event in pygame.event.get():
            if not hasattr(event, 'key'): continue
                    #QUIT Event
            elif event.type == KEYDOWN:
               #print(event.key)
                if event.key == K_ESCAPE:
                    main()
                if event.key == K_BACKSPACE:
                    if player > 1:
                        choose_mode(playercount, player - 1)
                    else:
                        main()
                #EDIT STATS WITH RIGHT/LEFT , CHANGE ROW WITH UP/DOWN
                if event.key == K_UP:
                    CURSOR_ROW += -1
                    if CURSOR_ROW < 1:
                        CURSOR_ROW = 1
                if event.key == K_DOWN:
                    CURSOR_ROW += 1
                    if CURSOR_ROW > 10:
                        CURSOR_ROW = 10

                if event.key == K_RETURN:
                    if player == playercount:                        
                        if playercount == 2:
                            main2players.main()
                        if playercount == 3:
                            main3players.main()
                        if playercount == 4:
                            main4players.main()
                    else:
                        choose_mode(playercount, player + 1)

        pygame.display.update()
        fpsClock.tick(60)
        
def main():
    
    #MAINLOOP
    while 1:
        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND,(0,0))

        
        #DRAW MAIN MENUE
        main_txt1 = " S P A C E  F I G H T E R S "
        main_txt2 = (" # PLAYERS?   --"+
        "--  KEYS:  P1( left | up | right )  P2( a | w | d )  P3( j | i | l )  P4( f | t | h )")
        main_txt3 = " (2) "
        main_txt4 = " (3) "
        main_txt5 = " (4) "        
        p1_txt = BIGFONT.render((main_txt1), True, WHITE, BLACK)
        DISPLAY.blit(p1_txt,(210, 150))
        p2_txt = FONT.render((main_txt2), True, WHITE, BLACK)
        DISPLAY.blit(p2_txt,(150, 250))
        p3_txt = FONT.render((main_txt3), True, WHITE, BLACK)
        DISPLAY.blit(p3_txt,(150, 350))
        p4_txt = FONT.render((main_txt4), True, WHITE, BLACK)
        DISPLAY.blit(p4_txt,(150, 450))
        p5_txt = FONT.render((main_txt5), True, WHITE, BLACK)
        DISPLAY.blit(p5_txt,(150, 550))
        
        DISPLAY.blit(SHIP1,(180,350))
        DISPLAY.blit(SHIP2,(230,350))
        DISPLAY.blit(SHIP1,(180,450))
        DISPLAY.blit(SHIP2,(230,450))
        DISPLAY.blit(SHIP3,(280,450))
        DISPLAY.blit(SHIP1,(180,550))
        DISPLAY.blit(SHIP2,(230,550))
        DISPLAY.blit(SHIP3,(280,550))
        DISPLAY.blit(SHIP4,(330,550))

        
        for event in pygame.event.get():
            if not hasattr(event, 'key'): continue
        
            #QUIT Event
            elif event.type == KEYDOWN:
                #print(event.key)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # Choose Players
                
                if (event.key == K_2):
                    choose_mode(2)
                    
                if (event.key == K_3):
                    choose_mode(3)
                                        
                if (event.key == K_4):
                    choose_mode(4)
                    



        pygame.display.update()
        fpsClock.tick(60)


if __name__ == "__main__":
    main()
