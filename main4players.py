#!/usr/bin/env python
import sys
import pygame
import math
import random
from pygame.locals import *


#INITIALIZE

SCREENWIDTH = 800
SCREENHEIGHT = 600

pygame.init()
DISPLAY = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("SpaceFighters")
pygame.display.set_icon(pygame.image.load('resources/ship1big.png'))
fpsClock = pygame.time.Clock()
pygame.mouse.set_visible(0)
pygame.key.set_repeat(1,10)
frame_nr = frame_start = frame_start2= 0

#SOUNDS
missileSound = pygame.mixer.Sound('resources/missile.wav')
explosionSound = pygame.mixer.Sound('resources/explosion.wav')
#CONSTANTS

#Fonts
BIGFONT = pygame.font.Font('font.ttf', 30)
FONT = pygame.font.Font('font.ttf', 16)
SMALLFONT = pygame.font.Font('font.ttf', 9)

#TEXTURES
BACKGROUND = pygame.image.load('resources/background1600.png')
SHIP1   = pygame.image.load('resources/ship1.png')
SHIP2   = pygame.image.load('resources/ship2.png')
SHIP3   = pygame.image.load('resources/ship3.png')
SHIP4   = pygame.image.load('resources/ship4.png') 
ROCKET1 = pygame.image.load('resources/rocket1.png')
ROCKET2 = pygame.image.load('resources/rocket2.png')
ROCKET3 = pygame.image.load('resources/rocket3.png')
ROCKET4 = pygame.image.load('resources/rocket4.png') 
ENDGAME = pygame.image.load('resources/endgamescreen1600.png')
LUKASPOWERUP = pygame.image.load('resources/lukas_powerup.png')
EXPLOSION = pygame.image.load('resources/explosion.png')



#representing colours
BLACK =(0,0,0)
WHITE =(255,255,255)
BLUE =(100,115,175)
RED =(176,52,52)
GREEN =(84,155,70)
ORANGE =(255,150,0)



def load_stats(player_nr):
    if player_nr == 1:
        try:
            high_score_file = open("stats1.txt", "r")
            stats = str(high_score_file.read())
            high_score_file.close()
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")
    
        return stats
    
    if player_nr == 2:
        try:
            high_score_file = open("stats2.txt", "r")
            stats = str(high_score_file.read())
            high_score_file.close()
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")
    
        return stats
    if player_nr == 3:
        try:
            high_score_file = open("stats3.txt", "r")
            stats = str(high_score_file.read())
            high_score_file.close()
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")
    
        return stats
    if player_nr == 4:
        try:
            high_score_file = open("stats4.txt", "r")
            stats = str(high_score_file.read())
            high_score_file.close()
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")
    
        return stats

STATS1 = load_stats(1)
STATS2 = load_stats(2)
STATS3 = load_stats(3)
STATS4 = load_stats(4)

print(STATS1, STATS2, STATS3, STATS4)

shipspeed = [int(STATS1[1]),int(STATS2[1]),int(STATS3[1]),int(STATS4[1])]
maneuv = [int(STATS1[4]),int(STATS2[4]),int(STATS3[4]),int(STATS4[4])]
rocketspeed = [int(STATS1[7]),int(STATS2[7]),int(STATS3[7]),int(STATS4[7])]

print(shipspeed, maneuv, rocketspeed)
    
class Ship(pygame.sprite.Sprite):

    def __init__(self, x,y,player):
        """ PYGAME STUFF HERE"""
        super().__init__()


        """ NON PYGAME STUFF HERE"""

        self.speed = shipspeed[player-1]
        self.direction = 0
        self.k_left = self.k_right = 0
        self.player = player
        self.lukas = False
        self.boolean = False
        self.direc = ""
        self.alive = True

        """ MORE PYGAME STUFF"""
        if self.player == 1:
            self.image = SHIP1
        if self.player == 2:
            self.image = SHIP2
        if self.player == 3:
            self.image = SHIP3
        if self.player == 4:
            self.image = SHIP4
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(range(7,10)) *x / 10
        self.rect.y = random.choice(range(7,10)) *y / 10

    def respawntime(self):
        pass


    def update(self):
        #CHANGE THIS EQUATION TO CANCEL OUT PLAYERS
        # x = 3
        # if self.player == x:
        #     self.alive = False
        #COMPUTE NEW x and y
        if self.alive:
            self.direction = 0
            self.direction += (self.k_left + self.k_right)

            rad = self.direction * math.pi / 180
            self.rect.x += -self.speed*math.sin(rad)
            self.rect.y += -self.speed*math.cos(rad)

            if self.rect.x > SCREENWIDTH:
                self.rect.x = 0
            if self.rect.x < 0:
                self.rect.x = SCREENWIDTH
            if self.rect.y > SCREENHEIGHT:
                self.rect.y = 0
            if self.rect.y < 0:
                self.rect.y = SCREENHEIGHT



            if self.player == 1:
                self.image=(pygame.transform.rotate(SHIP1, self.direction))
            if self.player == 2:
                self.image=(pygame.transform.rotate(SHIP2, self.direction))
            if self.player == 3:
                self.image=(pygame.transform.rotate(SHIP3, self.direction))
            if self.player == 4:
                self.image=(pygame.transform.rotate(SHIP4, self.direction))
            #self.rect = self.image.get_rect()



            #RETURN rad to ZERO
            rad = 0
        else:
            self.rect.x = self.rect.y = SCREENWIDTH * self.player

    def change_angle(self, direc, luka):

        if direc == "LEFT":
            self.boolean =  True
            self.direc = "LEFT"
        if direc == "RIGHT":
            self.boolean =  True
            self.direc = "RIGHT"
        if direc == "LEFT2":
            self.boolean =  False
            self.direc = "LEFT2"
        if direc == "RIGHT2":
            self.boolean =  False
            self.direc = "RIGHT2"


    def change_angle2(self):
        m=maneuv[self.player-1]
        if self.direc == "LEFT" and self.boolean:
            if not self.lukas:
                self.k_left += m
            else:
                self.k_right += -m
        if self.direc == "RIGHT" and self.boolean:
            if not self.lukas:
                self.k_right += -m
            else:
                self.k_left += m


class Rocket(pygame.sprite.Sprite):

    def __init__(self,x,y,direction,exists,player):
        super().__init__()
        self.player = player
        self.direction= direction
        self.exists = exists
        if self.player == 1:
            self.image = ROCKET1
        if self.player == 2:
            self.image = ROCKET2
        if self.player == 3:
            self.image = ROCKET3
        if self.player == 4:
            self.image = ROCKET4
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed=1





    def update(self):
        if self.exists:
            if self.speed < rocketspeed[self.player-1]:
                self.speed+= self.speed*0.1 +0.7
            if self.rect.x > SCREENWIDTH and self.rect.x < 1500:
                self.rect.x = 0
            if self.rect.x < 0 and self.rect.x > -1500:
                self.rect.x = SCREENWIDTH
            if self.rect.y > SCREENHEIGHT and self.rect.y < 1500:
                self.rect.y = 0
            if self.rect.y < 0 and self.rect.y > -1500:
                self.rect.y = SCREENHEIGHT
        else:
            self.rect.x = self.rect.y = SCREENWIDTH + 500
            self.speed = 0
        rad = self.direction * math.pi / 180
        self.rect.x += -self.speed*math.sin(rad)
        self.rect.y += -self.speed*math.cos(rad)
        if self.player == 1:
            self.image = pygame.transform.rotate(ROCKET1, self.direction)
        if self.player == 2:
            self.image = pygame.transform.rotate(ROCKET2, self.direction)
        if self.player == 3:
            self.image = pygame.transform.rotate(ROCKET3, self.direction)
        if self.player == 4:
            self.image = pygame.transform.rotate(ROCKET3, self.direction)

        # if self.exists:
        #     DISPLAY.blit(self.image,(self.rect.x,self.rect.y))

class Explode(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = EXPLOSION
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        explosionSound.play()
    # def update(self):
    #
    #     DISPLAY.blit(EXPLOSION,(self.rect.x,self.rect.y))


def respawn(x,y):
    #explode(x,y)
    pass



class Luk_powerup(pygame.sprite.Sprite):

    def __init__(self,x=400,y=400):
        super().__init__()
        self.image = LUKASPOWERUP
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alive = True

    def update(self):
        if self.alive:
            if self.rect.x > SCREENWIDTH:
                self.rect.x = 0
            self.rect.x += 0.8
            self.rect.y += 0
            #DISPLAY.blit(LUKASPOWERUP,(self.rect.x,self.rect.y))


def endgame(p1, p2, p3, p4):
    while 1:
        #Initialize as BLACK
        DISPLAY.fill(BLACK)
        DISPLAY.blit(ENDGAME,(0,0))
        #Get all Events
        if p1>p2 and p1 > p3 and p1 > p4:
            score = "Player 1 has won with " + str(p1) + " points!"
        if p1<p2 and p2 > p3 and p2 > p4:
            score = "Player 2 has won with " + str(p2) + " points!"
        if p3>p1 and p3 >p2 and p3 > p4:
            score = "Player 3 has won with " + str(p3) + " points!"
        if p4>p1 and p4 >p2 and p4 > p3:
            score = "Player 4 has won with " +str(p4) + " points!"
        text_dead = BIGFONT.render(score, True, WHITE, BLACK)
        DISPLAY.blit(text_dead,(200,150))
        text_dead1 =FONT.render("Blue   (Player1): " + str(p1), True, WHITE, BLUE)
        text_dead2 =FONT.render("Red    (Player2): " + str(p2), True, WHITE, RED)
        text_dead3 =FONT.render("Green (Player3): " + str(p3), True, WHITE, GREEN)
        text_dead4 =FONT.render("Orange (Player4): " + str(p4), True, WHITE, ORANGE)
        text_restart=FONT.render(" <<< Restart Game >>> <Y> OR <N>",True, WHITE, BLACK)
        
        DISPLAY.blit(text_dead1,(200,250))
        DISPLAY.blit(text_dead2,(200,300))
        DISPLAY.blit(text_dead3,(200,350))
        DISPLAY.blit(text_dead4,(200,400))
        DISPLAY.blit(text_restart,(200,500))
        
        for event in pygame.event.get():        
            #QUIT Event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
            #print(event.key)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_n:
                    pygame.quit()
                    sys.exit()
                if event.key == K_y or event.key == K_z:
                    main()
        pygame.display.update()
        fpsClock.tick(30)

def main(player_count=4):
    #INITIALIZE SHIPS AND DIRECTION
    x = SCREENWIDTH
    y = SCREENHEIGHT

    ship1 = Ship(x*0.8, y*0.8, 1) 
    ship2 = Ship(x*0.2, y*0.8, 2)
    ship3 = Ship(x*0.1, y*0.1, 3)
    ship3 = Ship(x*0.1, y*0.1, 3)
    ship4 = Ship(x*0.8, y*0.2, 4)
    rocket1 = Rocket(999,999,0,False,1)
    rocket2 = Rocket(999,999,0,False,2)
    rocket3 = Rocket(999,999,0,False,3)
    rocket4 = Rocket(999,999,0,False,4)
    explosion = Explode(x+500,y+500)
    explosion1 = Explode(x+500,y+500)
    explosion2 = Explode(x+500,y+500)
    explosion3 = Explode(x+500,y+500)
    explosion4 = Explode(x+500,y+500)
    #pygame.mixer.unpause()

    #INITIALIZE LUKAS POWERUP
    luk = Luk_powerup()
    luk_initialized = False
    luk.alive = False

    #CREATE SPRITELISTS
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(ship1)
    all_sprites_list.add(ship2)
    all_sprites_list.add(ship3)
    all_sprites_list.add(ship4)
    all_sprites_list.add(rocket1)
    all_sprites_list.add(rocket2)
    all_sprites_list.add(rocket3)
    all_sprites_list.add(rocket4)
    all_sprites_list.add(explosion)
    all_sprites_list.add(explosion1)
    all_sprites_list.add(explosion2)
    all_sprites_list.add(explosion3)
    all_sprites_list.add(explosion4)

    #INITIALIZE POINTS FOR PLAYERS
    p1_score = 0
    p2_score = 0
    p3_score = 0
    p4_score = 0

    
    frame_nr = frame_start = frame_start1= frame_start2= frame_start3= 0
    #MAINLOOP
    while 1:
        
        frame_nr += 1
        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND,(0,0))
        # ship1.update()
        # ship2.update()
        # ship3.update()
        # ship4.update()
        ship1.change_angle2()
        ship2.change_angle2()
        ship3.change_angle2()
        ship4.change_angle2()
        # rocket1.update()
        # rocket2.update()
        # rocket3.update()
        # rocket4.update()
        # explosion.update()
        # explosion1.update()
        # explosion2.update()
        # explosion3.update()
        # explosion4.update()
        all_sprites_list.update()
        all_sprites_list.draw(DISPLAY)
        
        #luk.update()
        if not luk.alive and frame_nr%100 == 0:
            luk.rect.x = (random.choice(range(0,10)) * 80)
            luk.rect.y = (random.choice(range(0,10)) * 60)
        if frame_nr > 300 and not luk_initialized:
            all_sprites_list.add(luk)
            luk.alive = True
            luk_initialized = True
        
        #DRAW SCORE
        p1_txt = BIGFONT.render(" "+ str(p1_score)+ " ", True, WHITE, BLUE)
        DISPLAY.blit(p1_txt,(SCREENWIDTH - 50, 50))
        p2_txt = BIGFONT.render(" "+ str(p2_score)+ " ", True, WHITE, RED)
        DISPLAY.blit(p2_txt,(50, 50))
        p3_txt = BIGFONT.render(" "+ str(p3_score)+ " ", True, WHITE, GREEN)
        DISPLAY.blit(p3_txt,(50, SCREENHEIGHT - 50))
        p4_txt = BIGFONT.render(" "+ str(p4_score)+ " ", True, WHITE, ORANGE)
        DISPLAY.blit(p4_txt,(SCREENWIDTH - 50, SCREENHEIGHT - 50))

        #ENDGAME
        if p1_score > p2_score +20 and p1_score > p3_score +20 and p1_score > p4_score +20:
            endgame(p1_score, p2_score, p3_score, p4_score)
        if p2_score > p1_score +20 and p2_score > p3_score +20 and p2_score > p4_score +20:
            endgame(p1_score, p2_score, p3_score, p4_score)
        if p3_score > p1_score +20 and p3_score > p2_score +20 and p3_score > p4_score +20:
            endgame(p1_score, p2_score, p3_score, p4_score)
        if p4_score > p1_score +20 and p4_score > p2_score +20 and p4_score > p3_score +20:
            endgame(p1_score, p2_score, p3_score, p4_score)
            
        #KollisionListe

        #SHIP COLLISIONS
        collisionx12 = ship1.rect.x < ship2.rect.x +30 and ship1.rect.x > ship2.rect.x -30
        collisiony12 = ship1.rect.y < ship2.rect.y +30 and ship1.rect.y > ship2.rect.y -30
        collision12 = (collisionx12 and collisiony12)

        collisionx23 = ship2.rect.x < ship3.rect.x +30 and ship2.rect.x > ship3.rect.x -30
        collisiony23 = ship2.rect.y < ship3.rect.y +30 and ship2.rect.y > ship3.rect.y -30
        collision23 = (collisionx23 and collisiony23)

        collisionx13 = ship1.rect.x < ship3.rect.x +30 and ship1.rect.x > ship3.rect.x -30
        collisiony13 = ship1.rect.y < ship3.rect.y +30 and ship1.rect.y > ship3.rect.y -30
        collision13 = (collisionx13 and collisiony13)

        collisionx14 = ship1.rect.x < ship4.rect.x +30 and ship1.rect.x > ship4.rect.x -30
        collisiony14 = ship1.rect.y < ship4.rect.y +30 and ship1.rect.y > ship4.rect.y -30
        collision14 = (collisionx14 and collisiony14)

        collisionx24 = ship2.rect.x < ship4.rect.x +30 and ship2.rect.x > ship4.rect.x -30
        collisiony24 = ship2.rect.y < ship4.rect.y +30 and ship2.rect.y > ship4.rect.y -30
        collision24 = (collisionx24 and collisiony24)

        collisionx34 = ship3.rect.x < ship4.rect.x +30 and ship3.rect.x > ship4.rect.x -30
        collisiony34 = ship3.rect.y < ship4.rect.y +30 and ship3.rect.y > ship4.rect.y -30
        collision34 = (collisionx34 and collisiony34)


        #ROCKET COLLISIONS

        #ROCKET1
        collisionx1r2 = ship2.rect.x < rocket1.rect.x +25 and ship2.rect.x > rocket1.rect.x -25
        collisiony1r2 = ship2.rect.y < rocket1.rect.y +25 and ship2.rect.y > rocket1.rect.y -25
        collision1r2 = (collisionx1r2 and collisiony1r2)

        collisionx1r3 = ship3.rect.x < rocket1.rect.x +25 and ship3.rect.x > rocket1.rect.x -25
        collisiony1r3 = ship3.rect.y < rocket1.rect.y +25 and ship3.rect.y > rocket1.rect.y -25
        collision1r3 = (collisionx1r3 and collisiony1r3)

        collisionx1r4 = ship4.rect.x < rocket1.rect.x +25 and ship4.rect.x > rocket1.rect.x -25
        collisiony1r4 = ship4.rect.y < rocket1.rect.y +25 and ship4.rect.y > rocket1.rect.y -25
        collision1r4 = (collisionx1r4 and collisiony1r4)
        
        #ROCKET2
        collisionx2r1 = ship1.rect.x < rocket2.rect.x +25 and ship1.rect.x > rocket2.rect.x -25
        collisiony2r1 = ship1.rect.y < rocket2.rect.y +25 and ship1.rect.y > rocket2.rect.y -25
        collision2r1 = (collisionx2r1 and collisiony2r1)
   
        collisionx2r3 = ship3.rect.x < rocket2.rect.x +25 and ship3.rect.x > rocket2.rect.x -25
        collisiony2r3 = ship3.rect.y < rocket2.rect.y +25 and ship3.rect.y > rocket2.rect.y -25
        collision2r3 = (collisionx2r3 and collisiony2r3)

        collisionx2r4 = ship4.rect.x < rocket2.rect.x +25 and ship4.rect.x > rocket2.rect.x -25
        collisiony2r4 = ship4.rect.y < rocket2.rect.y +25 and ship4.rect.y > rocket2.rect.y -25
        collision2r4 = (collisionx2r4 and collisiony2r4)
        
        #ROCKET3
        collisionx3r1 = ship1.rect.x < rocket3.rect.x +25 and ship1.rect.x > rocket3.rect.x -25
        collisiony3r1 = ship1.rect.y < rocket3.rect.y +25 and ship1.rect.y > rocket3.rect.y -25
        collision3r1 = (collisionx3r1 and collisiony3r1)

        collisionx3r2 = ship2.rect.x < rocket3.rect.x +25 and ship2.rect.x > rocket3.rect.x -25
        collisiony3r2 = ship2.rect.y < rocket3.rect.y +25 and ship2.rect.y > rocket3.rect.y -25
        collision3r2 = (collisionx3r2 and collisiony3r2)

        collisionx3r4 = ship4.rect.x < rocket3.rect.x +25 and ship4.rect.x > rocket3.rect.x -25
        collisiony3r4 = ship4.rect.y < rocket3.rect.y +25 and ship4.rect.y > rocket3.rect.y -25
        collision3r4 = (collisionx3r4 and collisiony3r4)

        #ROCKET4
        collisionx4r1 = ship1.rect.x < rocket4.rect.x +25 and ship1.rect.x > rocket4.rect.x -25
        collisiony4r1 = ship1.rect.y < rocket4.rect.y +25 and ship1.rect.y > rocket4.rect.y -25
        collision4r1 = (collisionx4r1 and collisiony4r1)

        collisionx4r2 = ship2.rect.x < rocket4.rect.x +25 and ship2.rect.x > rocket4.rect.x -25
        collisiony4r2 = ship2.rect.y < rocket4.rect.y +25 and ship2.rect.y > rocket4.rect.y -25
        collision4r2 = (collisionx4r2 and collisiony4r2)

        collisionx4r3 = ship3.rect.x < rocket4.rect.x +25 and ship3.rect.x > rocket4.rect.x -25
        collisiony4r3 = ship3.rect.y < rocket4.rect.y +25 and ship3.rect.y > rocket4.rect.y -25
        collision4r3 = (collisionx4r3 and collisiony4r3)

        

        #KollisionLukas

        collision_xluk1 = ship1.rect.x < luk.rect.x +30 and ship1.rect.x > luk.rect.x -30
        collision_yluk1 = ship1.rect.y < luk.rect.y +30 and ship1.rect.y > luk.rect.y -30
        collisionluk1 = (collision_xluk1 and collision_yluk1)

        collision_xluk2 = ship2.rect.x < luk.rect.x +30 and ship2.rect.x > luk.rect.x -30
        collision_yluk2 = ship2.rect.y < luk.rect.y +30 and ship2.rect.y > luk.rect.y -30
        collisionluk2 = (collision_xluk2 and collision_yluk2)

        collision_xluk3 = ship3.rect.x < luk.rect.x +30 and ship3.rect.x > luk.rect.x -30
        collision_yluk3 = ship3.rect.y < luk.rect.y +30 and ship3.rect.y > luk.rect.y -30
        collisionluk3 = (collision_xluk3 and collision_yluk3)

        collision_xluk4 = ship4.rect.x < luk.rect.x +30 and ship4.rect.x > luk.rect.x -30
        collision_yluk4 = ship4.rect.y < luk.rect.y +30 and ship4.rect.y > luk.rect.y -30
        collisionluk4 = (collision_xluk4 and collision_yluk4)

        
        #RESET LUK_POWERUP DEBUFF
        if frame_nr > frame_start + 200:
            ship1.lukas = False
            ship2.lukas = False
            ship3.lukas = False
            ship4.lukas = False
        #RESPAWN LUK_POWERUP
        if frame_nr > frame_start + 750:
            luk.alive = True            
            
            
        #START LUK_POWERUP
        if collisionluk1 and luk.alive:
            ship2.lukas = True
            ship3.lukas = True
            ship4.lukas = True
            luk.alive = False
            frame_start = frame_nr
            
        if collisionluk2 and luk.alive:
            ship1.lukas = True
            ship3.lukas = True
            ship4.lukas = True
            luk.alive = False
            frame_start = frame_nr
            
        if collisionluk3 and luk.alive:
            ship1.lukas = True
            ship2.lukas = True
            ship4.lukas = True
            luk.alive = False
            frame_start = frame_nr

        if collisionluk4 and luk.alive:
            ship1.lukas = True
            ship2.lukas = True
            ship3.lukas = True
            luk.alive = False
            frame_start = frame_nr

        
        #KOLLISIONS Check #######
        if False: #dont change this plz // MAYBE ALL ELIFS SHOULD BE IFS!!
            nothing = 0

        #SHIP COLLISIONS
        elif collision12:
            explosion = Explode((ship1.rect.x +ship2.rect.x)/2,(ship1.rect.y +ship2.rect.y)/2)
            ship1.rect.x, ship1.rect.y = x*0.8, y*0.8
            ship2.rect.x, ship2.rect.y = x*0.2, y*0.8
            p1_score -= 1
            p2_score -= 1

        elif collision13:
            explosion = Explode((ship1.rect.x +ship3.rect.x)/2,(ship1.rect.y +ship3.rect.y)/2)
            ship1.rect.x, ship1.rect.y = x*0.8, y*0.8
            ship3.rect.x, ship3.rect.y = x*0.1, y*0.1
            p1_score -= 1
            p3_score -= 1

        elif collision23:
            explosion = Explode((ship2.rect.x +ship3.rect.x)/2,(ship2.rect.y +ship3.rect.y)/2)
            ship2.rect.x, ship2.rect.y = x*0.2, y*0.8
            ship3.rect.x, ship3.rect.y = x*0.1, y*0.1
            p2_score -= 1
            p3_score -= 1

        elif collision14:
            explosion = Explode((ship1.rect.x +ship4.rect.x)/2,(ship1.rect.y +ship4.rect.y)/2)
            ship1.rect.x, ship1.rect.y = x*0.8, y*0.8
            ship4.rect.x, ship4.rect.y = x*0.8, y*0.2
            p1_score -= 1
            p4_score -= 1

        elif collision24:
            explosion = Explode((ship2.rect.x +ship4.rect.x)/2,(ship2.rect.y +ship4.rect.y)/2)
            ship2.rect.x, ship2.rect.y = x*0.2, y*0.8
            ship4.rect.x, ship4.rect.y = x*0.8, y*0.2
            p2_score -= 1
            p4_score -= 1

        elif collision34:
            explosion = Explode((ship4.rect.x +ship3.rect.x)/2,(ship4.rect.y +ship3.rect.y)/2)
            ship4.rect.x, ship4.rect.y = x*0.8, y*0.2
            ship3.rect.x, ship3.rect.y = x*0.1, y*0.1
            p2_score -= 1
            p3_score -= 1

        #ROCKET COLLISIONS

        elif collision2r1:
            explosion2 = Explode(rocket2.rect.x,rocket2.rect.y)
            rocket2 = Rocket(999,999,0,False,2)
            ship1.rect.x, ship1.rect.y = x*0.8, y*0.8
            p1_score -= 1
            p2_score += 3

        elif collision1r2:
            explosion1 = Explode(rocket1.rect.x,rocket1.rect.y)
            rocket1 = Rocket(999,999,0,False,1)
            ship2.rect.x, ship2.rect.y = x*0.2, y*0.8
            p2_score -= 1
            p1_score += 3        

        elif collision3r1:
            explosion3 = Explode(rocket3.rect.x,rocket3.rect.y)
            rocket3 = Rocket(999,999,0,False,3)
            ship1.rect.x, ship1.rect.y = x*0.8, y*0.8
            p1_score -= 1
            p3_score += 3

        elif collision3r2:
            explosion3 = Explode(rocket3.rect.x,rocket3.rect.y)
            rocket3 = Rocket(999,999,0,False,3)
            ship2.rect.x, ship2.rect.y = x*0.2, y*0.8
            p2_score -= 1
            p3_score += 3

        elif collision2r3:
            explosion2 = Explode(rocket2.rect.x,rocket2.rect.y)
            rocket2 = Rocket(999,999,0,False,2)
            ship3.rect.x, ship3.rect.y = x*0.1, y*0.1
            p3_score -= 1
            p2_score += 3

        elif collision1r3:
            explosion1 = Explode(rocket1.rect.x,rocket1.rect.y)
            rocket1 = Rocket(999,999,0,False,1)
            ship3.rect.x, ship3.rect.y = x*0.1, y*0.1
            p3_score -= 1
            p1_score += 3    

        elif collision4r1:
            explosion4 = Explode(rocket4.rect.x,rocket4.rect.y)
            rocket4 = Rocket(999,999,0,False,4)
            ship1.rect.x, ship1.rect.y = x*0.8, y*0.8
            p1_score -= 1
            p4_score += 3

        elif collision4r2:
            explosion4 = Explode(rocket4.rect.x,rocket4.rect.y)
            rocket4 = Rocket(999,999,0,False,4)
            ship2.rect.x, ship2.rect.y = x*0.2, y*0.8
            p2_score -= 1
            p4_score += 3

        elif collision4r3:
            explosion4 = Explode(rocket4.rect.x,rocket4.rect.y)
            rocket4 = Rocket(999,999,0,False,4)
            ship3.rect.x, ship3.rect.y = x*0.1, y*0.1
            p3_score -= 1
            p4_score += 3

        elif collision1r4:
            explosion1 = Explode(rocket1.rect.x,rocket1.rect.y)
            rocket1 = Rocket(999,999,0,False,1)
            ship4.rect.x, ship4.rect.y = x*0.8, y*0.2
            p4_score -= 1
            p1_score += 3

        elif collision2r4:
            explosion2 = Explode(rocket2.rect.x,rocket2.rect.y)
            rocket2 = Rocket(999,999,0,False,2)
            ship4.rect.x, ship4.rect.y = x*0.8, y*0.2
            p4_score -= 1
            p2_score += 3

        elif collision3r4:
            explosion3 = Explode(rocket3.rect.x,rocket3.rect.y)
            rocket3 = Rocket(999,999,0,False,3)
            ship4.rect.x, ship4.rect.y = x*0.8, y*0.2
            p4_score -= 1
            p3_score += 3
        
        for event in pygame.event.get():
            if not hasattr(event, 'key'): continue
        
            #QUIT Event
            elif event.type == KEYDOWN:
                #print(event.key)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # MOVEMENT with ARROW KEYS
                
                if (event.key == K_RIGHT):              
                    ship1.change_angle("RIGHT", ship1.lukas)
                if (event.key == K_LEFT):                    
                    ship1.change_angle("LEFT", ship1.lukas)
                if (event.key == K_d):
                    ship2.change_angle("RIGHT",ship2.lukas)
                if (event.key == K_a):                    
                    ship2.change_angle("LEFT",ship2.lukas)
                if (event.key == K_j):                    
                    ship3.change_angle("LEFT",ship3.lukas)
                if (event.key == K_l):                    
                    ship3.change_angle("RIGHT",ship3.lukas)
                if (event.key == K_f):
                    ship4.change_angle("LEFT",ship4.lukas)
                if (event.key == K_h):                    
                    ship4.change_angle("RIGHT",ship4.lukas)
                # SHOOTING with UP
                if (event.key == K_UP):
                    missileSound.play()
                    rocket1 = Rocket(ship1.rect.x, ship1.rect.y,ship1.direction, True,1)
                    all_sprites_list.add(rocket1)
                if (event.key == K_w):
                    missileSound.play()
                    rocket2 = Rocket(ship2.rect.x, ship2.rect.y,ship2.direction, True,2)
                    all_sprites_list.add(rocket2)
                if (event.key == K_i):
                    missileSound.play()
                    rocket3 = Rocket(ship3.rect.x, ship3.rect.y,ship3.direction, True,3)
                    all_sprites_list.add(rocket3)
                if (event.key == K_t):
                    missileSound.play()
                    rocket4 = Rocket(ship4.rect.x, ship4.rect.y,ship4.direction, True,4)
                    all_sprites_list.add(rocket4)

                    
            elif event.type == KEYUP:
                if (event.key == K_RIGHT):
                    ship1.change_angle("RIGHT2",ship1.lukas)
                if (event.key == K_LEFT):
                    ship1.change_angle("LEFT2",ship1.lukas)
                if (event.key == K_a):
                    ship2.change_angle("LEFT2",ship2.lukas)
                if (event.key == K_d):
                    ship2.change_angle("RIGHT2",ship2.lukas)
                if (event.key == K_j):
                    ship3.change_angle("LEFT2",ship3.lukas)
                if (event.key == K_l):
                    ship3.change_angle("RIGHT2",ship3.lukas)
                if (event.key == K_f):
                    ship4.change_angle("LEFT2",ship4.lukas)
                if (event.key == K_h):
                    ship4.change_angle("RIGHT2",ship4.lukas)
                    

        pygame.display.update()
        fpsClock.tick(60)


if __name__ == "__main__":
    main()
