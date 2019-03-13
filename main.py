#!/usr/bin/env python
import sys
import pygame


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
pygame.key.set_repeat(100,100)
CURSOR_ROW = 1
CURSOR   = pygame.image.load('resources/cursor.png')

#CONSTANTS

#Fonts
BIGFONT = pygame.font.Font('font.ttf', 34)
MEDFONT = pygame.font.Font('font.ttf', 28)
FONT = pygame.font.Font('font.ttf', 16)
SMALLFONT = pygame.font.Font('font.ttf', 9)

#TEXTURES
BACKGROUND = pygame.image.load('resources/background.png')
SHIP1   = pygame.image.load('resources/ship1.png')
SHIP2   = pygame.image.load('resources/ship2.png')
SHIP3   = pygame.image.load('resources/ship3.png')
SHIP4   = pygame.image.load('resources/ship4.png')

#representing colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (100,115,175)
RED = (176,52,52)
GREEN = (84,155,70)
ORANGE =(255,150,0)

#STATS to be modified and imported
#[ShipSpeed, Maneuverability, RocketSpeed, MoneyLeft]
STATS1 = [1,1,1,1000]
STATS2 = [1,1,1,1000]
STATS3 = [1,1,1,1000]
STATS4 = [1,1,1,1000]

def save_stats(player_nr):
    global STATS1
    global STATS2
    global STATS3
    global STATS4
    try:
        # Write the file to disk
        high_score_file = open("stats"+str(player_nr)+".txt", "w")
        if player_nr == 1:
            high_score_file.write(str(STATS1))
        if player_nr == 2:
            high_score_file.write(str(STATS2))
        if player_nr == 3:
            high_score_file.write(str(STATS3))
        if player_nr == 4:
            high_score_file.write(str(STATS4))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")


def reset_all_stats():
    global STATS1
    global STATS2
    global STATS3
    global STATS4
    STATS1 = [1,1,1,1000]
    STATS2 = [1,1,1,1000]
    STATS3 = [1,1,1,1000]
    STATS4 = [1,1,1,1000]
    for i in range(1,5):
        try:
            resetfile = open("stats"+str(i)+".txt", 'r+')
            resetfile.truncate(0)
        except IOError:
            # Hm, can't write it.
            print("Unable to save the high score.")
        save_stats(i)


def calc_points(player_nr):
    global STATS1
    global STATS2
    global STATS3
    global STATS4
    if player_nr == 1:
        STATS1[3] = (1030 - (10 * STATS1[0] * STATS1[0] )
                     - (10 * STATS1[1] * STATS1[1] )
                     - (10 * STATS1[2] * STATS1[2] ))
    if player_nr == 2:
        STATS2[3] = (1030 - (10 * STATS2[0] * STATS2[0] )
                     - (10 * STATS2[1] * STATS2[1] )
                     - (10 * STATS2[2] * STATS2[2] ))
    if player_nr == 3:
        STATS3[3] = (1030 - (10 * STATS3[0] * STATS3[0] )
                     - (10 * STATS3[1] * STATS3[1] )
                     - (10 * STATS3[2] * STATS3[2] ))
    if player_nr == 4:
        STATS4[3] = (1030 - (10 * STATS4[0] * STATS4[0] )
                     - (10 * STATS4[1] * STATS4[1] )
                     - (10 * STATS4[2] * STATS4[2] ))
    

def up_stat(player_nr):
    global CURSOR_ROW
    global STATS1
    global STATS2
    global STATS3
    global STATS4

    if player_nr ==1:            
        if CURSOR_ROW == 1:
            STATS1[0] += 1
            if STATS1[0] > 9: STATS1[0] = 9
        if CURSOR_ROW == 2:
            STATS1[1] += 1
            if STATS1[1] > 9: STATS1[1] = 9
        if CURSOR_ROW == 3:
            STATS1[2] += 1
            if STATS1[2] > 9: STATS1[2] = 9
        if CURSOR_ROW == 4:
            STATS1[3] += 1
            if STATS1[3] > 9: STATS1[3] = 9
    if player_nr ==2:            
        if CURSOR_ROW == 1:
            STATS2[0] += 1
            if STATS2[0] > 9: STATS2[0] = 9
        if CURSOR_ROW == 2:
            STATS2[1] += 1
            if STATS2[1] > 9: STATS2[1] = 9
        if CURSOR_ROW == 3:
            STATS2[2] += 1
            if STATS2[2] > 9: STATS2[2] = 9
        if CURSOR_ROW == 4:
            STATS2[3] += 1
    if player_nr ==3:            
        if CURSOR_ROW == 1:
            STATS3[0] += 1
            if STATS3[0] > 9: STATS3[0] = 9
        if CURSOR_ROW == 2:
            STATS3[1] += 1
            if STATS3[1] > 9: STATS3[1] = 9
        if CURSOR_ROW == 3:
            STATS3[2] += 1
            if STATS3[2] > 9: STATS3[2] = 9
        if CURSOR_ROW == 4:
            STATS3[3] += 1
    if player_nr ==4:            
        if CURSOR_ROW == 1:
            STATS4[0] += 1
            if STATS4[0] > 9: STATS4[0] = 9
        if CURSOR_ROW == 2:
            STATS4[1] += 1
            if STATS4[1] > 9: STATS4[1] = 9
        if CURSOR_ROW == 3:
            STATS4[2] += 1
            if STATS4[2] > 9: STATS4[2] = 9
        if CURSOR_ROW == 4:
            STATS4[3] += 1

    calc_points(player_nr)
        
def down_stat(player_nr):
    global CURSOR_ROW
    global STATS1
    global STATS2
    global STATS3
    global STATS4
    
    if player_nr ==1:            
        if CURSOR_ROW == 1:
            STATS1[0] -= 1
            if STATS1[0] < 1: STATS1[0] = 1
        if CURSOR_ROW == 2:
            STATS1[1] -= 1
            if STATS1[1] < 1: STATS1[1] = 1
        if CURSOR_ROW == 3:
            STATS1[2] -= 1
            if STATS1[2] < 1: STATS1[2] = 1
        if CURSOR_ROW == 4:
            STATS1[3] -= 1
    if player_nr ==2:            
        if CURSOR_ROW == 1:
            STATS2[0] -= 1
            if STATS2[0] < 1: STATS2[0] = 1
        if CURSOR_ROW == 2:
            STATS2[1] -= 1
            if STATS2[1] < 1: STATS2[1] = 1
        if CURSOR_ROW == 3:
            STATS2[2] -= 1
            if STATS2[2] < 1: STATS2[2] = 1
        if CURSOR_ROW == 4:
            STATS2[3] -= 1
            if STATS2[3] < 1: STATS2[3] = 1
    if player_nr ==3:            
        if CURSOR_ROW == 1:
            STATS3[0] -= 1
            if STATS3[0] < 1: STATS3[0] = 1
        if CURSOR_ROW == 2:
            STATS3[1] -= 1
            if STATS3[1] < 1: STATS3[1] = 1
        if CURSOR_ROW == 3:
            STATS3[2] -= 1
            if STATS3[2] < 1: STATS3[2] = 1
        if CURSOR_ROW == 4:
            STATS3[3] -= 1
            if STATS3[3] < 1: STATS3[3] = 1
    if player_nr ==4:            
        if CURSOR_ROW == 1:
            STATS4[0] -= 1
            if STATS4[0] < 1: STATS4[0] = 1
        if CURSOR_ROW == 2:
            STATS4[1] -= 1
            if STATS4[1] < 1: STATS4[1] = 1
        if CURSOR_ROW == 3:
            STATS4[2] -= 1
            if STATS4[2] < 1: STATS4[2] = 1
        if CURSOR_ROW == 4:
            STATS4[3] -= 1
            if STATS4[3] < 1: STATS4[3] = 1
            
    calc_points(player_nr)

def choose_mode(playercount, player = 1):   
    while 1:
        global CURSOR_ROW
        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND,(0,0))        

        points_pl1 = " Money left for Upgrades :  " + str(STATS1[3]) + " $ "
        points_pl2 = " Money left for Upgrades :  " + str(STATS2[3]) + " $ "
        points_pl3 = " Money left for Upgrades :  " + str(STATS3[3]) + " $ "
        points_pl4 = " Money left for Upgrades :  " + str(STATS4[3]) + " $ "
        stats_text1 = stats_text2 = stats_text3 = player_txt1_ = points_txt_ = ""
        
        if player == 1:
            DISPLAY.blit(pygame.transform.scale(SHIP1,(100,100)),(580,50))
            player_txt1 = " PLAYER " + str(player) +" MODIFY STATS "
            player_txt1_ = BIGFONT.render((player_txt1), True, BLUE, BLACK)
            stats_text1 = " Ship Speed : " + STATS1[0] * "|x|"
            stats_text2 = " Maneuverability : " + STATS1[1] * "|x|"
            stats_text3 = " Rocket Max Speed : " + STATS1[2] * "|x|"
            if STATS1[3] >= 0:
                points_txt_ = MEDFONT.render((points_pl1), True, WHITE, BLACK)
            else:
                points_txt_ = MEDFONT.render((points_pl1), True, RED, BLACK)
        if player == 2:
            DISPLAY.blit(pygame.transform.scale(SHIP2,(100,100)),(580,50))
            player_txt1 = " PLAYER " + str(player) +" MODIFY STATS "
            player_txt1_ = BIGFONT.render((player_txt1), True, RED, BLACK)
            stats_text1 = " Ship Speed : " + STATS2[0] * "|x|"
            stats_text2 = " Maneuverability : " + STATS2[1] * "|x|"
            stats_text3 = " Rocket Max Speed : " + STATS2[2] * "|x|"
            if STATS2[3] >= 0:
                points_txt_ = MEDFONT.render((points_pl2), True, WHITE, BLACK)
            else:
                points_txt_ = MEDFONT.render((points_pl2), True, RED, BLACK)
        if player == 3:
            DISPLAY.blit(pygame.transform.scale(SHIP3,(100,100)),(580,50))
            player_txt1 = " PLAYER " + str(player) +" MODIFY STATS "
            player_txt1_ = BIGFONT.render((player_txt1), True, GREEN, BLACK)
            stats_text1 = " Ship Speed : " + STATS3[0] * "|x|"
            stats_text2 = " Maneuverability : " + STATS3[1] * "|x|"
            stats_text3 = " Rocket Max Speed : " + STATS3[2] * "|x|"
            if STATS3[3] >= 0:
                points_txt_ = MEDFONT.render((points_pl3), True, WHITE, BLACK)
            else:
                points_txt_ = MEDFONT.render((points_pl3), True, RED, BLACK)
        if player == 4:
            DISPLAY.blit(pygame.transform.scale(SHIP4,(100,100)),(580,50))
            player_txt1 = " PLAYER " + str(player) +" MODIFY STATS "
            player_txt1_ = BIGFONT.render((player_txt1), True, ORANGE, BLACK)
            stats_text1 = " Ship Speed : " + STATS4[0] * "|x|"
            stats_text2 = " Maneuverability : " + STATS4[1] * "|x|"
            stats_text3 = " Rocket Max Speed : " + STATS4[2] * "|x|"
            if STATS3[3] >= 0:
                points_txt_ = MEDFONT.render((points_pl3), True, WHITE, BLACK)
            else:
                points_txt_ = MEDFONT.render((points_pl4), True, RED, BLACK)

        stats_text1_ = FONT.render((stats_text1), True, WHITE, BLACK)
        stats_text2_ = FONT.render((stats_text2), True, WHITE, BLACK)
        stats_text3_ = FONT.render((stats_text3), True, WHITE, BLACK)

        DISPLAY.blit(stats_text1_,(180, 240))
        DISPLAY.blit(stats_text2_,(180, 340))
        DISPLAY.blit(stats_text3_,(180, 440))
                     
        DISPLAY.blit(player_txt1_,(100, 100))
        DISPLAY.blit(points_txt_,(100, 150))
        DISPLAY.blit(CURSOR,(120,CURSOR_ROW*SCREENHEIGHT/6+125))
        
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
                    if CURSOR_ROW > 4:
                        CURSOR_ROW = 4
                if event.key == K_RIGHT:
                    up_stat(player)
                if event.key == K_LEFT:
                    down_stat(player)
                if event.key == K_r:
                    reset_all_stats()

                if event.key == K_RETURN:
                    if player == playercount:                        
                        if playercount == 2:
                            save_stats(1)
                            save_stats(2)
                            save_stats(3)
                            save_stats(4)
                            import main2players
                            main2players.main()
                        if playercount == 3:
                            save_stats(1)
                            save_stats(2)
                            save_stats(3)
                            save_stats(4)
                            import main3players
                            main3players.main()
                        if playercount == 4:
                            save_stats(1)
                            save_stats(2)
                            save_stats(3)
                            save_stats(4)
                            import main4players
                            main4players.main()
                    else:
                        choose_mode(playercount, player + 1)

        pygame.display.update()
        fpsClock.tick(60)
        
def main():
    
    #MAINLOOP
    reset_all_stats()

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
        DISPLAY.blit(p1_txt,(100, 100))
        p2_txt = FONT.render((main_txt2), True, WHITE, BLACK)
        DISPLAY.blit(p2_txt,(100, 250))
        p3_txt = FONT.render((main_txt3), True, WHITE, BLACK)
        DISPLAY.blit(p3_txt,(150, 325))
        p4_txt = FONT.render((main_txt4), True, WHITE, BLACK)
        DISPLAY.blit(p4_txt,(150, 400))
        p5_txt = FONT.render((main_txt5), True, WHITE, BLACK)
        DISPLAY.blit(p5_txt,(150, 475))
        
        DISPLAY.blit(SHIP1,(180,325))
        DISPLAY.blit(SHIP2,(230,325))
        DISPLAY.blit(SHIP1,(180,400))
        DISPLAY.blit(SHIP2,(230,400))
        DISPLAY.blit(SHIP3,(280,400))
        DISPLAY.blit(SHIP1,(180,475))
        DISPLAY.blit(SHIP2,(230,475))
        DISPLAY.blit(SHIP3,(280,475))
        DISPLAY.blit(SHIP4,(330,475))

        
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
