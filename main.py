#!/usr/bin/env python
import sys
import pygame
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

# BG Music
pygame.mixer.music.load("resources/bg_music.mp3")

#Fonts
SPACEFONT = pygame.font.Font('resources/space.ttf', 34)
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

# TEXTURES SUPERWEAPONS
SHIP1_LS = pygame.image.load('resources/ship1_lightspeed.png')
SHIP1_SM = pygame.image.load('resources/spacemine.png')
SHIP1_PH = pygame.image.load('resources/ship1_phantom.png')
SHIP2_LS = pygame.image.load('resources/ship2_lightspeed.png')
SHIP2_SM = pygame.image.load('resources/spacemine.png')
SHIP2_PH = pygame.image.load('resources/ship2_phantom.png')
SHIP3_LS = pygame.image.load('resources/ship3_lightspeed.png')
SHIP3_SM = pygame.image.load('resources/spacemine.png')
SHIP3_PH = pygame.image.load('resources/ship3_phantom.png')
SHIP4_LS = pygame.image.load('resources/ship4_lightspeed.png')
SHIP4_SM = pygame.image.load('resources/spacemine.png')
SHIP4_PH = pygame.image.load('resources/ship4_phantom.png')

#representing colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (100,115,175)
RED = (176,52,52)
GREEN = (84,155,70)
ORANGE =(255,150,0)

#STATS to be modified and imported
#[ShipSpeed, Maneuverability, RocketSpeed, MoneyLeft, SuperWeapon]
STATS1 = [1,1,1,1000, 1]
STATS2 = [1,1,1,1000, 1]
STATS3 = [1,1,1,1000, 1]
STATS4 = [1,1,1,1000, 1]



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
    STATS1 = [1,1,1,1000, 1]
    STATS2 = [1,1,1,1000, 1]
    STATS3 = [1,1,1,1000, 1]
    STATS4 = [1,1,1,1000, 1]
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
            STATS1[4] += 1
            if STATS1[4] > 3: STATS1[4] = 3
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
            STATS2[4] += 1
            if STATS2[4] > 3: STATS2[4] = 3
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
            STATS3[4] += 1
            if STATS3[4] > 3: STATS3[4] = 3
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
            STATS4[4] += 1
            if STATS4[4] > 3: STATS4[4] = 3

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
            STATS1[4] -= 1
            if STATS1[4] < 1: STATS1[4] = 1
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
            STATS2[4] -= 1
            if STATS2[4] < 1: STATS2[4] = 1
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
            STATS3[4] -= 1
            if STATS3[4] < 1: STATS3[4] = 1
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
            STATS4[4] -= 1
            if STATS4[4] < 1: STATS4[4] = 1
            
    calc_points(player_nr)


def choose_mode(playercount, player = 1):   
    while 1:
        global CURSOR_ROW
        global STATS1
        global STATS2
        global STATS3
        global STATS4

        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND,(0,0))        

        points_pl1 = " Money left for Upgrades :  " + str(STATS1[3]) + " $ "
        bool_money_1 = STATS1[3] >= 0
        points_pl2 = " Money left for Upgrades :  " + str(STATS2[3]) + " $ "
        bool_money_2 = STATS2[3] >= 0
        points_pl3 = " Money left for Upgrades :  " + str(STATS3[3]) + " $ "
        bool_money_3 = STATS3[3] >= 0
        points_pl4 = " Money left for Upgrades :  " + str(STATS4[3]) + " $ "
        bool_money_4 = STATS4[3] >= 0
        stats_text1 = stats_text2 = stats_text3 = player_txt1_ = points_txt_ = ""


        super_text1 = "Chose your Superweapon : < Light Speed >"
        super_text2 = "Chose your Superweapon : < Space Mine >"
        super_text3 = "Chose your Superweapon : < Phantom Shield // NOT READY YET >"

        
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

            if STATS1[4] == 1:
                super_text_ = FONT.render((super_text1), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP1_LS,(40, 160)),(620,420))
            if STATS1[4] == 2:
                super_text_ = FONT.render((super_text2), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP1_SM,(40,40)),(620,540))
            if STATS1[4] == 3:
                super_text_ = FONT.render((super_text3), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP1_PH,(40,40)),(595,540))
                DISPLAY.blit(pygame.transform.scale(SHIP1   ,(40,40)),(635,540))
                DISPLAY.blit(pygame.transform.scale(SHIP1_PH,(40,40)),(675,540))

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

            if STATS2[4] == 1:
                super_text_ = FONT.render((super_text1), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP2_LS,(40, 160)),(620,420))
            if STATS2[4] == 2:
                super_text_ = FONT.render((super_text2), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP2_SM,(40,40)),(620,540))
            if STATS2[4] == 3:
                super_text_ = FONT.render((super_text3), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP2_PH,(40,40)),(595,540))
                DISPLAY.blit(pygame.transform.scale(SHIP2   ,(40,40)),(635,540))
                DISPLAY.blit(pygame.transform.scale(SHIP2_PH,(40,40)),(675,540))

        if player == 3:
            DISPLAY.blit(pygame.transform.scale(SHIP3,(100,100)),(580,50))
            player_txt1 = " PLAYER " + str(player) +" MODIFY STATS "
            player_txt1_ = BIGFONT.render((player_txt1), True, GREEN, BLACK)
            stats_text1 = " Ship Speed : " + STATS3[0] * "|x|"
            stats_text2 = " Maneuverability : " + STATS3[1] * "|x|"
            stats_text3 = " Rocket ,Max Speed : " + STATS3[2] * "|x|"
            if STATS3[3] >= 0:
                points_txt_ = MEDFONT.render((points_pl3), True, WHITE, BLACK)
            else:
                points_txt_ = MEDFONT.render((points_pl3), True, RED, BLACK)

            if STATS3[4] == 1:
                super_text_ = FONT.render((super_text1), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP3_LS,(40, 160)),(620,420))
            if STATS3[4] == 2:
                super_text_ = FONT.render((super_text2), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP3_SM,(40,40)),(620,540))
            if STATS3[4] == 3:
                super_text_ = FONT.render((super_text3), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP3_PH,(40,40)),(595,540))
                DISPLAY.blit(pygame.transform.scale(SHIP3   ,(40,40)),(635,540))
                DISPLAY.blit(pygame.transform.scale(SHIP3_PH,(40,40)),(675,540))

        if player == 4:
            DISPLAY.blit(pygame.transform.scale(SHIP4,(100,100)),(580,50))
            player_txt1 = " PLAYER " + str(player) +" MODIFY STATS "
            player_txt1_ = BIGFONT.render((player_txt1), True, ORANGE, BLACK)
            stats_text1 = " Ship Speed : " + STATS4[0] * "|x|"
            stats_text2 = " Maneuverability : " + STATS4[1] * "|x|"
            stats_text3 = " Rocket Max Speed : " + STATS4[2] * "|x|"
            if STATS4[3] >= 0:
                points_txt_ = MEDFONT.render((points_pl4), True, WHITE, BLACK)
            else:
                points_txt_ = MEDFONT.render((points_pl4), True, RED, BLACK)

            if STATS4[4] == 1:
                super_text_ = FONT.render((super_text1), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP4_LS,(40, 160)),(620,420))
            if STATS4[4] == 2:
                super_text_ = FONT.render((super_text2), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP4_SM,(40,40)),(620,540))
            if STATS4[4] == 3:
                super_text_ = FONT.render((super_text3), True, WHITE, BLACK)
                DISPLAY.blit(pygame.transform.scale(SHIP4_PH,(40,40)),(595,540))
                DISPLAY.blit(pygame.transform.scale(SHIP4   ,(40,40)),(635,540))
                DISPLAY.blit(pygame.transform.scale(SHIP4_PH,(40,40)),(675,540))


        stats_text1_ = FONT.render((stats_text1), True, WHITE, BLACK)
        stats_text2_ = FONT.render((stats_text2), True, WHITE, BLACK)
        stats_text3_ = FONT.render((stats_text3), True, WHITE, BLACK)

        DISPLAY.blit(stats_text1_,(180, 240))
        DISPLAY.blit(stats_text2_,(180, 340))
        DISPLAY.blit(stats_text3_,(180, 440))

        DISPLAY.blit(super_text_, (180, 540))
                     
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
                        if playercount == 2 and bool_money_2:
                            save_stats(1)
                            save_stats(2)
                            save_stats(3)
                            save_stats(4)

                            import main4players
                            main4players.PLAYERS = 2
                            main4players.main()
                        if playercount == 3 and bool_money_3:
                            save_stats(1)
                            save_stats(2)
                            save_stats(3)
                            save_stats(4)
                            import main4players
                            main4players.PLAYERS = 3
                            main4players.main()
                        if playercount == 4 and bool_money_4:
                            save_stats(1)
                            save_stats(2)
                            save_stats(3)
                            save_stats(4)
                            import main4players
                            main4players.PLAYERS = 4
                            main4players.main()
                    elif bool_money_1 and bool_money_2 and bool_money_3 and bool_money_4:
                        choose_mode(playercount, player + 1)

        pygame.display.update()
        fpsClock.tick(60)

def intro():
    main_txt1 = "spacefighters"
    done = False
    i = SCREENHEIGHT
    while not done and i > 102:
        if i > 100:
            i-=2
        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND,(0,0))

        p1_txt = SPACEFONT.render((main_txt1), True, WHITE)
        DISPLAY.blit(p1_txt,(200, i))
        for event in pygame.event.get():
            if not hasattr(event, 'key'): continue

            #QUIT Event
            elif event.type == KEYDOWN:
                done = True
        pygame.display.update()
        fpsClock.tick(60)

def main():
    global PLAYERS
    #MAINLOOP
    intro()
    reset_all_stats()
    pygame.mixer.music.play(0,0)

    while 1:
        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND,(0,0))

        
        #DRAW MAIN MENUE
        main_txt1 = "spacefighters"
        main_txt2 = (" # PLAYERS?   --"+
        "--  KEYS:  P1( left | up | right )  P2( a | w | d )  P3( j | i | l )  P4( f | t | h )")
        main_txt3 = " (2) "
        main_txt4 = " (3) "
        main_txt5 = " (4) "        
        p1_txt = SPACEFONT.render((main_txt1), True, WHITE)
        DISPLAY.blit(p1_txt,(200, 100))
        p2_txt = FONT.render((main_txt2), True, WHITE)
        DISPLAY.blit(p2_txt,(100, 250))
        p3_txt = FONT.render((main_txt3), True, WHITE)
        DISPLAY.blit(p3_txt,(150, 325))
        p4_txt = FONT.render((main_txt4), True, WHITE)
        DISPLAY.blit(p4_txt,(150, 400))
        p5_txt = FONT.render((main_txt5), True, WHITE)
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
                    PLAYERS = 2
                    choose_mode(2)
                    
                if (event.key == K_3):
                    PLAYERS = 3
                    choose_mode(3)
                                        
                if (event.key == K_4):
                    PLAYERS = 4
                    choose_mode(4)
                    



        pygame.display.update()
        fpsClock.tick(60)


if __name__ == "__main__":
    main()
