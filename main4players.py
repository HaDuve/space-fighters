#!/usr/bin/env python
import sys
import pygame
import math
import random
import time
from pygame.locals import *

# INITIALIZE

SCREENWIDTH = 800
SCREENHEIGHT = 600

pygame.init()
DISPLAY = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("SpaceFighters")
pygame.display.set_icon(pygame.image.load('resources/ship1big.png'))
fpsClock = pygame.time.Clock()
pygame.mouse.set_visible(0)
pygame.key.set_repeat(1, 10)
frame_nr = frame_start = frame_start2 = 0

# SOUNDS
pygame.mixer.music.load("resources/bg_music.mp3")
missileSound = pygame.mixer.Sound('resources/missile.wav')
explosionSound = pygame.mixer.Sound('resources/explosion.wav')
# CONSTANTS
PLAYERS = 2

# Fonts
SPACEFONT = pygame.font.Font('resources/space.ttf', 34)
BIGFONT = pygame.font.Font('font.ttf', 30)
FONT = pygame.font.Font('font.ttf', 16)
SMALLFONT = pygame.font.Font('font.ttf', 9)

# TEXTURES
BACKGROUND = pygame.image.load('resources/background1600.png')
SHIP1 = pygame.image.load('resources/ship1.png')
SHIP2 = pygame.image.load('resources/ship2.png')
SHIP3 = pygame.image.load('resources/ship3.png')
SHIP4 = pygame.image.load('resources/ship4.png')
ROCKET1 = pygame.image.load('resources/rocket1.png')
ROCKET2 = pygame.image.load('resources/rocket2.png')
ROCKET3 = pygame.image.load('resources/rocket3.png')
ROCKET4 = pygame.image.load('resources/rocket4.png')
ENDGAME = pygame.image.load('resources/endgamescreen1600.png')
LUKASPOWERUP = pygame.image.load('resources/lukas_powerup.png')
EXPLOSION = pygame.image.load('resources/explosion.png')
EXPLOSION_GIF = pygame.image.load('resources/explosion_anim_900x900.png')
EXPLOSION_GIF_BIG = pygame.image.load('resources/explosion_anim_1200x1200.png')
RESPAWN_GIF = pygame.image.load('resources/respawn_anim_900x900_test.png')

# TEXTURES SUPERWEAPONS
SHIP1_LS = pygame.image.load('resources/ship1_lightspeed.png')
SHIP1_SM = pygame.image.load('resources/spacemine1.png')
SHIP1_PH = pygame.image.load('resources/ship1_phantom.png')
SHIP2_LS = pygame.image.load('resources/ship2_lightspeed.png')
SHIP2_SM = pygame.image.load('resources/spacemine2.png')
SHIP2_PH = pygame.image.load('resources/ship2_phantom.png')
SHIP3_LS = pygame.image.load('resources/ship3_lightspeed.png')
SHIP3_SM = pygame.image.load('resources/spacemine3.png')
SHIP3_PH = pygame.image.load('resources/ship3_phantom.png')
SHIP4_LS = pygame.image.load('resources/ship4_lightspeed.png')
SHIP4_SM = pygame.image.load('resources/spacemine4.png')
SHIP4_PH = pygame.image.load('resources/ship4_phantom.png')

# representing colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (100, 115, 175)
RED = (176, 52, 52)
GREEN = (84, 155, 70)
ORANGE = (255, 150, 0)


def load_stats(player_nr):
    if player_nr == 1:
        try:
            high_score_file = open("stats1.txt", "r")
            stats = high_score_file.read()
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
            stats = high_score_file.read()
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
            stats = high_score_file.read()
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
            stats = high_score_file.read()
            high_score_file.close()
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("I'm confused. Starting with no high score.")

        return stats


# INITIALIZE STATS OF THE SHIPS

STATS1 = []
STATS2 = []
STATS3 = []
STATS4 = []



shipspeed = []
maneuv = []
rocketspeed = []
superweapon = []

print(shipspeed, maneuv, rocketspeed, superweapon)


def lies_between(x, y, z):
    a = distance(y, z)
    b = distance(z, x)
    c = distance(x, y)
    return a**2 + b**2 >= c**2 and a**2 + c**2 >= b**2


def distance(A, B):
    return math.sqrt((A.x - B.x)**2 + (A.y - B.y)**2)


class Point:
    def __init__(self,x ,y):
        self.x = x
        self.y = y


class Ship:

    def __init__(self, x, y, player):
        self.image = SHIP1
        self.x = random.choice(range(5, 9)) * x / 10
        self.y = random.choice(range(5, 9)) * y / 10
        # TODO BALANCE SPEED HERE
        self.speed = 0.7 * shipspeed[player - 1]
        self.direction = 0
        self.k_left = self.k_right = 0
        self.player = player
        self.lukas = False
        self.boolean = False
        self.direc = ""
        self.alive = True
        self.ls_start = [0,0]
        self.ls_end = [0,0]
        self.ls_alive = False
        self.last = pygame.time.get_ticks()
        self.respawn_duration = 1600
        self.respawn_animation = 0
        self.respawn_running = True
        self.respawn_x = self.x
        self.respawn_y = self.y

    def respawn(self):
        if True:        
            self.alive = False
            now = pygame.time.get_ticks()
            # 2 represents animation speed -> 2 equals 50% speed
            if now % 2 == 0:
                self.respawn_animation += 1
            if now - self.last <= self.respawn_duration:
                DISPLAY.blit(RESPAWN_GIF, (self.respawn_x - 50, self.respawn_y - 50),
                             pygame.Rect((self.respawn_animation % 9) * 900 / 9,
                                         (self.respawn_animation // 9) * 900 / 9,
                                         900 / 9, 900 / 9))
            else:
                self.respawn_running = False
                self.alive = True
                self.x = self.respawn_x
                self.y = self.respawn_y

    def move(self):
        # RESPAWN
        if self.respawn_running and self. player <= PLAYERS:
            self.respawn()
        # CANCEL OUT PLAYERS

        if self.player > PLAYERS:
            self.alive = False
        # COMPUTE NEW x and y
        if self.alive:
            self.direction = 0
            self.direction += (self.k_left + self.k_right)

            rad = self.direction * math.pi / 180
            self.x += -self.speed * math.sin(rad)
            self.y += -self.speed * math.cos(rad)

            if self.x > SCREENWIDTH:
                self.x = 0
            if self.x < 0:
                self.x = SCREENWIDTH
            if self.y > SCREENHEIGHT:
                self.y = 0
            if self.y < 0:
                self.y = SCREENHEIGHT

            if self.player == 1:
                image = pygame.transform.rotate(SHIP1, self.direction)
                self.image = image
            if self.player == 2:
                image = pygame.transform.rotate(SHIP2, self.direction)
                self.image = image
            if self.player == 3:
                image = pygame.transform.rotate(SHIP3, self.direction)
                self.image = image
            if self.player == 4:
                image = pygame.transform.rotate(SHIP4, self.direction)
                self.image = image

            DISPLAY.blit(image, (self.x, self.y))

            # RETURN rad to ZERO for better angle control
            rad = 0
        # If your not alive, be away from the screen and other ships, which are not alive
        else:
            self.x = self.y = SCREENWIDTH * self.player

    def change_angle(self, direc, luka):

        if direc == "LEFT":
            self.boolean = True
            self.direc = "LEFT"
        if direc == "RIGHT":
            self.boolean = True
            self.direc = "RIGHT"
        if direc == "LEFT2":
            self.boolean = False
            self.direc = "LEFT2"
        if direc == "RIGHT2":
            self.boolean = False
            self.direc = "RIGHT2"

    def change_angle2(self):
        # TODO BALANCE MANEUV HERE
        m = 0.6 * maneuv[self.player - 1]
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

    def start_lightspeed(self, other1, other2, other3) -> list:
        if self.alive:
            self.ls_alive = True
            self.ls_start = [self.x,self.y]
            rad = self.direction * math.pi / 180    
            self.ls_end = [ 
                            self.x + 50*(-self.speed * math.sin(rad)),
                            self.y + 50*(-self.speed * math.cos(rad))
                            ]
            image = pygame.transform.rotate(SHIP1_LS, self.direction)
            DISPLAY.blit(image, (self.x, self.y))

            # Compute if other ships die, depending on if they are near the rect center
            p_start = Point(self.ls_start[0], self.ls_start[1])
            p_end = Point(self.ls_end[0], self.ls_end[1])

            p_other1 = Point(other1.x, other1.y)
            p_other2 = Point(other2.x, other2.y)
            p_other3 = Point(other3.x, other3.y)

            #Which ships are hit?
            bool_123 = [False, False, False]

            #  DESTROY OTHER SHIPS
            if lies_between(p_other1, p_start, p_end) and (distance(p_end, p_other1) < 100
                                                        or distance(p_start, p_other1) < 100):
                bool_123[0] = True
                
            if lies_between(p_other2, p_start, p_end) and (distance(p_end, p_other2) < 100
                                                        or distance(p_start, p_other2) < 100):
                bool_123[1] = True
            
            if lies_between(p_other3, p_start, p_end) and (distance(p_end, p_other3) < 100
                                                        or distance(p_start, p_other3) < 100):
                bool_123[2] = True

            self.alive = False
            return bool_123

    def stop_lightspeed(self):
        if not self.alive and self.ls_alive:
            self.ls_alive = False
            self.alive = True
            self.x = self.ls_end[0]
            self.y = self.ls_end[1]
            image = pygame.transform.rotate(SHIP1_LS, self.direction)
            DISPLAY.blit(image, (self.x, self.y))

    def start_spacemine(self, frame_nr):
        return Spacemine(self.x ,self.y, self.k_left, self.k_right, self.speed, self.player, frame_nr, True)


class Spacemine:
    def __init__(self, x, y, left, right, speed, player,now,alive):
        self.x = x
        self.y = y
        self.direction = left + right
        self.alive = alive
        self.speed = 0.2 * speed
        self.player = player
        self.radius = 20
        rad = 0
        now = 0
        self.last = pygame.time.get_ticks()
        self.duration = 16000
        self.hasexploded = False
        
    def update(self):
        if self.alive:
            now = pygame.time.get_ticks()
            
            rad = self.direction * math.pi / 180
            self.x += -self.speed * math.sin(rad)
            self.y += -self.speed * math.cos(rad)
            if self.x > SCREENWIDTH and self.x < SCREENWIDTH + 10:
                self.x = 0
            if self.x < 0 and self.x > -SCREENWIDTH - 10:
                self.x = SCREENWIDTH
            if self.y > SCREENHEIGHT and self.y < SCREENHEIGHT + 10:
                self.y = 0
            if self.y < 0 and self.y > -SCREENHEIGHT - 10:
                self.y = SCREENHEIGHT
            if self.player == 1:
                    m_color = SHIP1_SM
            elif self.player == 2:
                    m_color = SHIP2_SM
            elif self.player == 3:
                    m_color = SHIP3_SM
            elif self.player == 4:
                    m_color = SHIP4_SM

            if now - self.last <= self.duration - 6000:
                DISPLAY.blit(pygame.transform.scale(m_color,(40,40)),(self.x,self.y))
                self.radius = 20 * 1.5
            elif now - self.last <= self.duration - 5000:
                DISPLAY.blit(pygame.transform.scale(m_color,(43,43)),(self.x,self.y))
                self.radius = 22 * 1.5
            elif now - self.last <= self.duration - 4000:
                DISPLAY.blit(pygame.transform.scale(m_color,(46,46)),(self.x,self.y))
                self.radius = 24 * 1.5
            elif now - self.last <= self.duration - 3000:
                DISPLAY.blit(pygame.transform.scale(m_color,(49,49)),(self.x,self.y))
                self.radius = 26 * 1.5
            elif now - self.last <= self.duration - 2000:
                DISPLAY.blit(pygame.transform.scale(m_color,(52,52)),(self.x,self.y))
                self.radius = 28 * 1.5
            elif now - self.last <= self.duration - 1000:
                DISPLAY.blit(pygame.transform.scale(m_color,(57,57)),(self.x,self.y))
                self.radius = 31 * 1.5
            elif now - self.last <= self.duration:
                DISPLAY.blit(pygame.transform.scale(m_color,(63,63)),(self.x,self.y))
                self.radius = 35 * 1.5
            else:
                self.alive = False
            

class Rocket:

    def __init__(self, x, y, direction, exists, player):
        self.x = x
        self.y = y
        
        self.direction = direction
        self.exists = exists
        self.player = player
        
        # TODO BALANCE ROCKETSPEED HERE
        self.speed = 0.2 * rocketspeed[self.player - 1] + 0.5
        self.maxspeed = rocketspeed[self.player - 1] * 1.5

    def move(self):
        if self.exists:
            if self.speed < self.maxspeed:
                self.speed = self.speed * 1.01 + 0.01 * rocketspeed[self.player - 1]
            if self.x > SCREENWIDTH and self.x < SCREENWIDTH + 10:
                self.x = 0
            if self.x < 0 and self.x > -SCREENWIDTH - 10:
                self.x = SCREENWIDTH
            if self.y > SCREENHEIGHT and self.y < SCREENHEIGHT + 10:
                self.y = 0
            if self.y < 0 and self.y > -SCREENHEIGHT - 10:
                self.y = SCREENHEIGHT
        else:
            self.x = self.y = SCREENWIDTH + 500
            self.speed = 0
        rad = self.direction * math.pi / 180
        self.x += -self.speed * math.sin(rad)
        self.y += -self.speed * math.cos(rad)
        if self.player == 1:
            image = pygame.transform.rotate(ROCKET1, self.direction)
        if self.player == 2:
            image = pygame.transform.rotate(ROCKET2, self.direction)
        if self.player == 3:
            image = pygame.transform.rotate(ROCKET3, self.direction)
        if self.player == 4:
            image = pygame.transform.rotate(ROCKET4, self.direction)
        if self.exists:
            DISPLAY.blit(image, (self.x, self.y))


class Explode:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.last = pygame.time.get_ticks()
        self.duration = 1600
        self.animation = 0
        explosionSound.play()

    def update(self):
        now = pygame.time.get_ticks()
        # 2 represents animationspeed -> 2 equals 50% speed
        if now % 2 == 0:
            self.animation += 1
        if self.animation > 810:
            self.animation = 0
        if now - self.last <= self.duration:
            if self.x < SCREENWIDTH and self.y < SCREENHEIGHT:
                DISPLAY.blit(EXPLOSION_GIF_BIG, (self.x - 50, self.y - 50),
                             pygame.Rect((self.animation % 9) * 1200 / 9, (self.animation // 9) * 1200 / 9,
                                         1200 / 9, 1200 / 9))
        

class LukPowerup:
    def __init__(self, x=400, y=400):
        self.x = x
        self.y = y
        self.alive = True

    def update(self, frame):
        if self.alive:
            if self.x > SCREENWIDTH:
                self.x = 0
            self.x += 0.8
            self.y += 0
            DISPLAY.blit(LUKASPOWERUP, (self.x, self.y))


def endgame(p1, p2, p3, p4):
    while 1:
        # Initialize as BLACK
        DISPLAY.fill(BLACK)
        DISPLAY.blit(ENDGAME, (0, 0))
        text_dead = BIGFONT.render("Winner Winner Chicken Dinner", True, BLUE, BLACK)
        # Get all Events
        if p1 > p2 and p1 > p3 and p1 > p4:
            score = "BLUE (1) has won with " + str(p1) + " points!"
            text_dead = BIGFONT.render(score, True, BLUE, BLACK)
        if p1 < p2 and p2 > p3 and p2 > p4:
            score = "RED (2) has won with " + str(p2) + " points!"
            text_dead = BIGFONT.render(score, True, RED, BLACK)
        if p3 > p1 and p3 > p2 and p3 > p4:
            score = "GREEN (3) has won with " + str(p3) + " points!"
            text_dead = BIGFONT.render(score, True, GREEN, BLACK)
        if p4 > p1 and p4 > p2 and p4 > p3:
            score = "ORANGE (4) has won with " + str(p4) + " points!"
            text_dead = BIGFONT.render(score, True, ORANGE, BLACK)

        DISPLAY.blit(text_dead, (200, 150))
        text_dead1 = FONT.render("Blue   (Player1): " + str(p1), True, WHITE, BLUE)
        text_dead2 = FONT.render("Red    (Player2): " + str(p2), True, WHITE, RED)
        text_dead3 = FONT.render("Green  (Player3): " + str(p3), True, WHITE, GREEN)
        text_dead4 = FONT.render("Orange (Player4): " + str(p4), True, WHITE, ORANGE)
        text_restart = FONT.render("|  Restart Game?  |  [Y]es  |  [N]o   | [M]ain Menu", True, WHITE, BLACK)

        DISPLAY.blit(text_dead1, (200, 250))
        DISPLAY.blit(text_dead2, (200, 300))
        DISPLAY.blit(text_dead3, (200, 350))
        DISPLAY.blit(text_dead4, (200, 400))
        DISPLAY.blit(text_restart, (200, 500))

        for event in pygame.event.get():
            # QUIT Event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # print(event.key)
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_n:
                    pygame.quit()
                    sys.exit()
                if event.key == K_y or event.key == K_z:
                    main()
                if event.key == K_m:
                    import main
                    main.main()
        pygame.display.update()
        fpsClock.tick(30)


def intro(ships):
    main_txt1 = "ready up"
    done = False
    i = SCREENHEIGHT
    j = i
    while not done:
        if i > 100:
            i -= 1
        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND,(0,0))
        if i > 400:
            p1_txt = SPACEFONT.render(main_txt1, True, WHITE)
        elif i > 300:
            p1_txt = SPACEFONT.render(main_txt1, True, RED)
        elif i > 200:
            p1_txt = SPACEFONT.render(main_txt1, True, ORANGE)
        else:
            p1_txt = SPACEFONT.render(main_txt1, True, GREEN)

        if i > 200:
            j = i
        DISPLAY.blit(p1_txt, (250, j))

        for ship in ships:
            ship.move()

        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue

            # QUIT Event
            elif event.type == KEYDOWN:
                if (event.key == K_RIGHT):
                    ships[0].change_angle("RIGHT", False)
                if (event.key == K_LEFT):
                    ships[0].change_angle("LEFT", False)
                if (event.key == K_d):
                    ships[1].change_angle("RIGHT", False)
                if (event.key == K_a):
                    ships[1].change_angle("LEFT", False)
                if (event.key == K_j):
                    ships[2].change_angle("LEFT", False)
                if (event.key == K_l):
                    ships[2].change_angle("RIGHT", False)
                if (event.key == K_f):
                    ships[3].change_angle("LEFT", False)
                if (event.key == K_h):
                    ships[3].change_angle("RIGHT", False)
            elif event.type == KEYUP:
                if (event.key == K_RIGHT):
                    ships[0].change_angle("RIGHT2", False)
                if (event.key == K_LEFT):
                    ships[0].change_angle("LEFT2", False)
                if (event.key == K_a):
                    ships[1].change_angle("LEFT2", False)
                if (event.key == K_d):
                    ships[1].change_angle("RIGHT2", False)
                if (event.key == K_j):
                    ships[2].change_angle("LEFT2", False)
                if (event.key == K_l):
                    ships[2].change_angle("RIGHT2", False)
                if (event.key == K_f):
                    ships[3].change_angle("LEFT2", False)
                if (event.key == K_h):
                    ships[3].change_angle("RIGHT2", False)

        pygame.display.update()
        fpsClock.tick(60)

        if i < 110:
            done = True


def main():
    global STATS1
    global STATS2
    global STATS3
    global STATS4
    global shipspeed, maneuv, rocketspeed, superweapon
    STATS1 = load_stats(1)
    STATS2 = load_stats(2)
    STATS3 = load_stats(3)
    STATS4 = load_stats(4)
    print(STATS1, STATS2, STATS3, STATS4)
    shipspeed = [int(STATS1[1]), int(STATS2[1]), int(STATS3[1]), int(STATS4[1])]
    maneuv = [int(STATS1[4]), int(STATS2[4]), int(STATS3[4]), int(STATS4[4])]
    rocketspeed = [int(STATS1[7]), int(STATS2[7]), int(STATS3[7]), int(STATS4[7])]
    superweapon = [int(STATS1[-2]), int(STATS2[-2]), int(STATS3[-2]), int(STATS4[-2])]
    print(shipspeed, maneuv, rocketspeed, superweapon)

    # INITIALIZE ENTITIES AND MUSIC
    pygame.mixer.music.play(0,0)
    explosionSound.set_volume(0)
    missileSound.set_volume(0)
    x = SCREENWIDTH
    y = SCREENHEIGHT
    ship1 = Ship(x * 0.8, y * 0.8, 1)
    ship2 = Ship(x * 0.2, y * 0.8, 2)
    ship3 = Ship(x * 0.1, y * 0.1, 3)
    ship4 = Ship(x * 0.8, y * 0.2, 4)
    rocket1 = Rocket(999, 999, 0, False, 1)
    rocket2 = Rocket(999, 999, 0, False, 2)
    rocket3 = Rocket(999, 999, 0, False, 3)
    rocket4 = Rocket(999, 999, 0, False, 4)
    explosion = Explode(x + 500, y + 500)
    explosion1 = Explode(x + 500, y + 500)
    explosion2 = Explode(x + 500, y + 500)
    explosion3 = Explode(x + 500, y + 500)
    explosion4 = Explode(x + 500, y + 500)
    explosion_super1 = Explode(x + 500, y + 500)
    explosion_super2 = Explode(x + 500, y + 500)
    explosion_super3 = Explode(x + 500, y + 500)
    explosion_super4 = Explode(x + 500, y + 500)
    explosion_mine1 = Explode(x + 500, y + 500)
    explosion_mine2 = Explode(x + 500, y + 500)
    explosion_mine3 = Explode(x + 500, y + 500)
    explosion_mine4 = Explode(x + 500, y + 500)
    explosion_mine5 = Explode(x + 500, y + 500)
    explosionSound.set_volume(0.3)
    missileSound.set_volume(0.1)
    spaceminelist = []
    otherlist1 = [ship2, ship3, ship4]
    otherlist2 = [ship1, ship3, ship4]
    otherlist3 = [ship1, ship2, ship4]
    otherlist4 = [ship1, ship2, ship3]

    # INITIALIZE LUKAS POWERUP
    luk = LukPowerup()
    luk_initialized = False
    luk.alive = False

    # INITIALIZE POINTS FOR PLAYERS
    p1_score = 0
    p2_score = 0
    p3_score = 0
    p4_score = 0

    frame_nr = frame_start = frame_start1 = frame_start2 = frame_start3 = 0
    frame_cd1 = frame_cd2 = frame_cd3 = frame_cd4 = 0

    # MAINLOOP
    intro_played = False

    while 1:

        frame_nr += 1
        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND, (0,0))
        ship1.move()
        ship2.move()
        ship3.move()
        ship4.move()
        ship1.change_angle2()
        ship2.change_angle2()
        ship3.change_angle2()
        ship4.change_angle2()
        rocket1.move()
        rocket2.move()
        rocket3.move()
        rocket4.move()

        otherlist1 = [ship2, ship3, ship4]
        otherlist2 = [ship1, ship3, ship4]
        otherlist3 = [ship1, ship2, ship4]
        otherlist4 = [ship1, ship2, ship3]
        if spaceminelist:
            for mine in spaceminelist:
                if mine.alive:
                    mine.update()
                    minepoint = Point(mine.x, mine.y)
                    
                    if mine.player == 1:
                        for entity in otherlist1:
                            entitypoint = Point(entity.x, entity.y)
                            if distance(minepoint, entitypoint) < mine.radius + 20:
                                explosion_mine1 = Explode(mine.x,mine.y)
                                spaceminelist.remove(mine)
                                explosion_super1 = Explode(entity.x, entity.y)
                                if entity.player == 1:
                                    ship1 = Ship(x * 0.8, y * 0.8, 1)
                                    p1_score -= 1
                                if entity.player == 2:
                                    ship2 = Ship(x * 0.2, y * 0.8, 2)
                                    p1_score += 3
                                    p2_score -= 1
                                if entity.player == 3:
                                    ship3 = Ship(x * 0.1, y * 0.1, 3)
                                    p1_score += 3
                                    p3_score -= 1
                                if entity.player == 4:
                                    ship4 = Ship(x * 0.8, y * 0.2, 4)
                                    p1_score += 3
                                    p4_score -= 1
                                    
                    if mine.player == 2:
                        for entity in otherlist2:
                            entitypoint = Point(entity.x, entity.y)
                            if distance(minepoint, entitypoint) < mine.radius:
                                explosion_mine2 = Explode(mine.x,mine.y)
                                spaceminelist.remove(mine)
                                explosion_super2 = Explode(entity.x, entity.y)
                                if entity.player == 1:
                                    ship1 = Ship(x * 0.8, y * 0.8, 1)
                                    p1_score += 3
                                    p2_score -= 1
                                if entity.player == 2:
                                    ship2 = Ship(x * 0.2, y * 0.8, 2)
                                    p2_score -= 1
                                if entity.player == 3:
                                    ship3 = Ship(x * 0.1, y * 0.1, 3)
                                    p2_score += 3
                                    p3_score -= 1
                                if entity.player == 4:
                                    ship4 = Ship(x * 0.8, y * 0.2, 4)
                                    p2_score += 3
                                    p4_score -= 1
                                    
                    if mine.player == 3:
                        for entity in otherlist3:
                            entitypoint = Point(entity.x, entity.y)
                            if distance(minepoint, entitypoint) < mine.radius:
                                explosion_mine3 = Explode(mine.x,mine.y)
                                spaceminelist.remove(mine)
                                explosion_super3 = Explode(entity.x, entity.y)
                                if entity.player == 1:
                                    ship1 = Ship(x * 0.8, y * 0.8, 1)
                                    p3_score += 3
                                    p1_score -= 1
                                if entity.player == 2:
                                    ship2 = Ship(x * 0.2, y * 0.8, 2)
                                    p3_score += 3
                                    p2_score -= 1
                                if entity.player == 3:
                                    ship3 = Ship(x * 0.1, y * 0.1, 3)
                                    p3_score -= 1
                                if entity.player == 4:
                                    ship4 = Ship(x * 0.8, y * 0.2, 4)
                                    p4_score += 3
                                    p4_score -= 1
                                    
                    if mine.player == 4:
                        for entity in otherlist4:
                            entitypoint = Point(entity.x, entity.y)
                            if distance(minepoint, entitypoint) < mine.radius:
                                explosion_mine4 = Explode(mine.x,mine.y)
                                spaceminelist.remove(mine)
                                explosion_super4 = Explode(entity.x, entity.y)
                                if entity.player == 1:
                                    ship1 = Ship(x * 0.8, y * 0.8, 1)
                                    p4_score += 3
                                    p1_score -= 1
                                if entity.player == 2:
                                    ship2 = Ship(x * 0.2, y * 0.8, 2)
                                    p4_score += 3
                                    p2_score -= 1
                                if entity.player == 3:
                                    ship3 = Ship(x * 0.1, y * 0.1, 3)
                                    p4_score += 3
                                    p3_score -= 1
                                if entity.player == 4:
                                    ship4 = Ship(x * 0.8, y * 0.2, 4)
                                    p4_score -= 1
                    
                elif not mine.alive and not mine.hasexploded:
                    explosion_mine5 = Explode(mine.x, mine.y)
                    mine.hasexploded = True

        
        explosion.update()
        explosion1.update()
        explosion2.update()
        explosion3.update()
        explosion4.update()
        explosion_super1.update()
        explosion_super2.update()
        explosion_super3.update()
        explosion_super4.update()
        explosion_mine1.update()
        explosion_mine2.update()
        explosion_mine3.update()
        explosion_mine4.update()
        explosion_mine5.update()
                    
        luk.update(frame_nr)
        if not luk.alive and frame_nr % 100 == 0:
            luk.x = (random.choice(range(0, 10)) * 80)
            luk.y = (random.choice(range(0, 10)) * 60)
        if frame_nr > 300 and not luk_initialized:
            luk.alive = True
            luk_initialized = True

        # DRAW SCORE
        p1_txt = BIGFONT.render(" " + str(p1_score) + " ", True, WHITE, BLUE)
        DISPLAY.blit(p1_txt, (SCREENWIDTH - 50, 50))
        p2_txt = BIGFONT.render(" " + str(p2_score) + " ", True, WHITE, RED)
        DISPLAY.blit(p2_txt, (50, 50))
        if PLAYERS > 2:
            p3_txt = BIGFONT.render(" " + str(p3_score) + " ", True, WHITE, GREEN)
            DISPLAY.blit(p3_txt, (50, SCREENHEIGHT - 50))
        if PLAYERS > 3:
            p4_txt = BIGFONT.render(" " + str(p4_score) + " ", True, WHITE, ORANGE)
            DISPLAY.blit(p4_txt, (SCREENWIDTH - 50, SCREENHEIGHT - 50))

        # ENDGAME
        if p1_score > p2_score + 20 and p1_score > p3_score + 20 and p1_score > p4_score + 20:
            endgame(p1_score, p2_score, p3_score, p4_score)
        if p2_score > p1_score + 20 and p2_score > p3_score + 20 and p2_score > p4_score + 20:
            endgame(p1_score, p2_score, p3_score, p4_score)
        if p3_score > p1_score + 20 and p3_score > p2_score + 20 and p3_score > p4_score + 20:
            endgame(p1_score, p2_score, p3_score, p4_score)
        if p4_score > p1_score + 20 and p4_score > p2_score + 20 and p4_score > p3_score + 20:
            endgame(p1_score, p2_score, p3_score, p4_score)

        # KollisionListe

        # SHIP COLLISIONS
        collisionx12 = ship1.x < ship2.x + 30 and ship1.x > ship2.x - 30
        collisiony12 = ship1.y < ship2.y + 30 and ship1.y > ship2.y - 30
        collision12 = (collisionx12 and collisiony12)

        collisionx23 = ship2.x < ship3.x + 30 and ship2.x > ship3.x - 30
        collisiony23 = ship2.y < ship3.y + 30 and ship2.y > ship3.y - 30
        collision23 = (collisionx23 and collisiony23)

        collisionx13 = ship1.x < ship3.x + 30 and ship1.x > ship3.x - 30
        collisiony13 = ship1.y < ship3.y + 30 and ship1.y > ship3.y - 30
        collision13 = (collisionx13 and collisiony13)

        collisionx14 = ship1.x < ship4.x + 30 and ship1.x > ship4.x - 30
        collisiony14 = ship1.y < ship4.y + 30 and ship1.y > ship4.y - 30
        collision14 = (collisionx14 and collisiony14)

        collisionx24 = ship2.x < ship4.x + 30 and ship2.x > ship4.x - 30
        collisiony24 = ship2.y < ship4.y + 30 and ship2.y > ship4.y - 30
        collision24 = (collisionx24 and collisiony24)

        collisionx34 = ship3.x < ship4.x + 30 and ship3.x > ship4.x - 30
        collisiony34 = ship3.y < ship4.y + 30 and ship3.y > ship4.y - 30
        collision34 = (collisionx34 and collisiony34)

        # ROCKET COLLISIONS

        # ROCKET1
        collisionx1r2 = ship2.x < rocket1.x + 25 and ship2.x > rocket1.x - 25
        collisiony1r2 = ship2.y < rocket1.y + 25 and ship2.y > rocket1.y - 25
        collision1r2 = (collisionx1r2 and collisiony1r2)

        collisionx1r3 = ship3.x < rocket1.x + 25 and ship3.x > rocket1.x - 25
        collisiony1r3 = ship3.y < rocket1.y + 25 and ship3.y > rocket1.y - 25
        collision1r3 = (collisionx1r3 and collisiony1r3)

        collisionx1r4 = ship4.x < rocket1.x + 25 and ship4.x > rocket1.x - 25
        collisiony1r4 = ship4.y < rocket1.y + 25 and ship4.y > rocket1.y - 25
        collision1r4 = (collisionx1r4 and collisiony1r4)

        # ROCKET2
        collisionx2r1 = ship1.x < rocket2.x + 25 and ship1.x > rocket2.x - 25
        collisiony2r1 = ship1.y < rocket2.y + 25 and ship1.y > rocket2.y - 25
        collision2r1 = (collisionx2r1 and collisiony2r1)

        collisionx2r3 = ship3.x < rocket2.x + 25 and ship3.x > rocket2.x - 25
        collisiony2r3 = ship3.y < rocket2.y + 25 and ship3.y > rocket2.y - 25
        collision2r3 = (collisionx2r3 and collisiony2r3)

        collisionx2r4 = ship4.x < rocket2.x + 25 and ship4.x > rocket2.x - 25
        collisiony2r4 = ship4.y < rocket2.y + 25 and ship4.y > rocket2.y - 25
        collision2r4 = (collisionx2r4 and collisiony2r4)

        # ROCKET3
        collisionx3r1 = ship1.x < rocket3.x + 25 and ship1.x > rocket3.x - 25
        collisiony3r1 = ship1.y < rocket3.y + 25 and ship1.y > rocket3.y - 25
        collision3r1 = (collisionx3r1 and collisiony3r1)

        collisionx3r2 = ship2.x < rocket3.x + 25 and ship2.x > rocket3.x - 25
        collisiony3r2 = ship2.y < rocket3.y + 25 and ship2.y > rocket3.y - 25
        collision3r2 = (collisionx3r2 and collisiony3r2)

        collisionx3r4 = ship4.x < rocket3.x + 25 and ship4.x > rocket3.x - 25
        collisiony3r4 = ship4.y < rocket3.y + 25 and ship4.y > rocket3.y - 25
        collision3r4 = (collisionx3r4 and collisiony3r4)

        # ROCKET4
        collisionx4r1 = ship1.x < rocket4.x + 25 and ship1.x > rocket4.x - 25
        collisiony4r1 = ship1.y < rocket4.y + 25 and ship1.y > rocket4.y - 25
        collision4r1 = (collisionx4r1 and collisiony4r1)

        collisionx4r2 = ship2.x < rocket4.x + 25 and ship2.x > rocket4.x - 25
        collisiony4r2 = ship2.y < rocket4.y + 25 and ship2.y > rocket4.y - 25
        collision4r2 = (collisionx4r2 and collisiony4r2)

        collisionx4r3 = ship3.x < rocket4.x + 25 and ship3.x > rocket4.x - 25
        collisiony4r3 = ship3.y < rocket4.y + 25 and ship3.y > rocket4.y - 25
        collision4r3 = (collisionx4r3 and collisiony4r3)

        # KollisionLukas

        collision_xluk1 = ship1.x < luk.x + 30 and ship1.x > luk.x - 30
        collision_yluk1 = ship1.y < luk.y + 30 and ship1.y > luk.y - 30
        collisionluk1 = (collision_xluk1 and collision_yluk1)

        collision_xluk2 = ship2.x < luk.x + 30 and ship2.x > luk.x - 30
        collision_yluk2 = ship2.y < luk.y + 30 and ship2.y > luk.y - 30
        collisionluk2 = (collision_xluk2 and collision_yluk2)

        collision_xluk3 = ship3.x < luk.x + 30 and ship3.x > luk.x - 30
        collision_yluk3 = ship3.y < luk.y + 30 and ship3.y > luk.y - 30
        collisionluk3 = (collision_xluk3 and collision_yluk3)

        collision_xluk4 = ship4.x < luk.x + 30 and ship4.x > luk.x - 30
        collision_yluk4 = ship4.y < luk.y + 30 and ship4.y > luk.y - 30
        collisionluk4 = (collision_xluk4 and collision_yluk4)

        # RESET LUK_POWERUP DEBUFF
        if frame_nr > frame_start + 200:
            ship1.lukas = False
            ship2.lukas = False
            ship3.lukas = False
            ship4.lukas = False
        # RESPAWN LUK_POWERUP
        if frame_nr > frame_start + 750:
            luk.alive = True

            # START LUK_POWERUP
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

        # KOLLISIONS Check #######
        if False:  # dont change this plz // MAYBE ALL ELIFS SHOULD BE IFS!!
            pass

        # SHIP COLLISIONS
        elif collision12:
            explosion = Explode((ship1.x + ship2.x) / 2, (ship1.y + ship2.y) / 2)
            ship1 = Ship(x * 0.8, y * 0.8, 1)
            ship2 = Ship(x * 0.2, y * 0.8, 2)
            p1_score -= 1
            p2_score -= 1

        elif collision13:
            explosion = Explode((ship1.x + ship3.x) / 2, (ship1.y + ship3.y) / 2)
            ship1 = Ship(x * 0.8, y * 0.8, 1)
            ship3 = Ship(x * 0.1, y * 0.1, 3)
            p1_score -= 1
            p3_score -= 1

        elif collision23:
            explosion = Explode((ship2.x + ship3.x) / 2, (ship2.y + ship3.y) / 2)
            ship2 = Ship(x * 0.2, y * 0.8, 2)
            ship3 = Ship(x * 0.1, y * 0.1, 3)
            p2_score -= 1
            p3_score -= 1

        elif collision14:
            explosion = Explode((ship1.x + ship4.x) / 2, (ship1.y + ship4.y) / 2)
            ship1 = Ship(x * 0.8, y * 0.8, 1)
            ship4 = Ship(x * 0.8, y * 0.2, 4)
            p1_score -= 1
            p4_score -= 1

        elif collision24:
            explosion = Explode((ship2.x + ship4.x) / 2, (ship2.y + ship4.y) / 2)
            ship2 = Ship(x * 0.2, y * 0.8, 2)
            ship4 = Ship(x * 0.8, y * 0.2, 4)
            p2_score -= 1
            p4_score -= 1

        elif collision34:
            explosion = Explode((ship4.x + ship3.x) / 2, (ship4.y + ship3.y) / 2)
            ship4 = Ship(x * 0.8, y * 0.2, 4)
            ship3 = Ship(x * 0.1, y * 0.1, 3)
            p2_score -= 1
            p3_score -= 1

        # ROCKET COLLISIONS

        elif collision2r1:
            explosion2 = Explode(rocket2.x, rocket2.y)
            rocket2 = Rocket(999, 999, 0, False, 2)
            ship1 = Ship(x * 0.8, y * 0.8, 1)
            p1_score -= 1
            p2_score += 3

        elif collision1r2:
            explosion1 = Explode(rocket1.x, rocket1.y)
            rocket1 = Rocket(999, 999, 0, False, 1)
            ship2 = Ship(x * 0.2, y * 0.8, 2)
            p2_score -= 1
            p1_score += 3

        elif collision3r1:
            explosion3 = Explode(rocket3.x, rocket3.y)
            rocket3 = Rocket(999, 999, 0, False, 3)
            ship1 = Ship(x * 0.8, y * 0.8, 1)
            p1_score -= 1
            p3_score += 3

        elif collision3r2:
            explosion3 = Explode(rocket3.x, rocket3.y)
            rocket3 = Rocket(999, 999, 0, False, 3)
            ship2 = Ship(x * 0.2, y * 0.8, 2)
            p2_score -= 1
            p3_score += 3

        elif collision2r3:
            explosion2 = Explode(rocket2.x, rocket2.y)
            rocket2 = Rocket(999, 999, 0, False, 2)
            ship3 = Ship(x * 0.1, y * 0.1, 3)
            p3_score -= 1
            p2_score += 3

        elif collision1r3:
            explosion1 = Explode(rocket1.x, rocket1.y)
            rocket1 = Rocket(999, 999, 0, False, 1)
            ship3 = Ship(x * 0.1, y * 0.1, 3)
            p3_score -= 1
            p1_score += 3

        elif collision4r1:
            explosion4 = Explode(rocket4.x, rocket4.y)
            rocket4 = Rocket(999, 999, 0, False, 4)
            ship1 = Ship(x * 0.8, y * 0.8, 1)
            p1_score -= 1
            p4_score += 3

        elif collision4r2:
            explosion4 = Explode(rocket4.x, rocket4.y)
            rocket4 = Rocket(999, 999, 0, False, 4)
            ship2 = Ship(x * 0.2, y * 0.8, 2)
            p2_score -= 1
            p4_score += 3

        elif collision4r3:
            explosion4 = Explode(rocket4.x, rocket4.y)
            rocket4 = Rocket(999, 999, 0, False, 4)
            ship3 = Ship(x * 0.1, y * 0.1, 3)
            p3_score -= 1
            p4_score += 3

        elif collision1r4:
            explosion1 = Explode(rocket1.x, rocket1.y)
            rocket1 = Rocket(999, 999, 0, False, 1)
            ship4 = Ship(x * 0.8, y * 0.2, 4)
            p4_score -= 1
            p1_score += 3

        elif collision2r4:
            explosion2 = Explode(rocket2.x, rocket2.y)
            rocket2 = Rocket(999, 999, 0, False, 2)
            ship4 = Ship(x * 0.8, y * 0.2, 4)
            p4_score -= 1
            p2_score += 3

        elif collision3r4:
            explosion3 = Explode(rocket3.x, rocket3.y)
            rocket3 = Rocket(999, 999, 0, False, 3)
            ship4 = Ship(x * 0.8, y * 0.2, 4)
            p4_score -= 1
            p3_score += 3

        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue

            # QUIT Event
            elif event.type == KEYDOWN:
                # print(event.key)
                if event.key == K_ESCAPE:
                    import main
                    main.main()

                # MOVEMENT with ARROW KEYS

                if (event.key == K_RIGHT):
                    ship1.change_angle("RIGHT", ship1.lukas)
                if (event.key == K_LEFT):
                    ship1.change_angle("LEFT", ship1.lukas)
                if (event.key == K_d):
                    ship2.change_angle("RIGHT", ship2.lukas)
                if (event.key == K_a):
                    ship2.change_angle("LEFT", ship2.lukas)
                if (event.key == K_j):
                    ship3.change_angle("LEFT", ship3.lukas)
                if (event.key == K_l):
                    ship3.change_angle("RIGHT", ship3.lukas)
                if (event.key == K_f):
                    ship4.change_angle("LEFT", ship4.lukas)
                if (event.key == K_h):
                    ship4.change_angle("RIGHT", ship4.lukas)
                # SHOOTING with UP
                if (event.key == K_UP):
                    missileSound.play()
                    rocket1 = Rocket(ship1.x, ship1.y, ship1.direction, True, 1)
                if (event.key == K_w):
                    missileSound.play()
                    rocket2 = Rocket(ship2.x, ship2.y, ship2.direction, True, 2)
                if (event.key == K_i):
                    missileSound.play()
                    rocket3 = Rocket(ship3.x, ship3.y, ship3.direction, True, 3)
                if (event.key == K_t):
                    missileSound.play()
                    rocket4 = Rocket(ship4.x, ship4.y, ship4.direction, True, 4)
                
                # SUPERWEAPON with DOWN
                if (event.key == K_DOWN):
                    # LIGHTSPEED SUPERWEAPON PLAYER 1
                    if superweapon[0] == 1:
                        if frame_nr > frame_cd1 + 200 and ship1.alive:
                            kill_bool = [False, False, False]
                            kill_bool = ship1.start_lightspeed(ship2, ship3, ship4)
                            if kill_bool[0]:
                                explosion_super1 = Explode(ship2.x, ship2.y)
                                ship2 = Ship(x * 0.2, y * 0.8, 2)
                                p2_score -= 1
                                p1_score += 3
                            if kill_bool[1]:
                                explosion_super1 = Explode(ship3.x, ship3.y)
                                ship3 = Ship(x * 0.1, y * 0.1, 3)
                                p3_score -= 1
                                p1_score += 3
                            if kill_bool[2]:
                                explosion_super1 = Explode(ship4.x, ship4.y)
                                ship4 = Ship(x * 0.8, y * 0.2, 4)
                                p4_score -= 1
                                p1_score += 3
                            frame_cd1 = frame_nr
                        ship1.stop_lightspeed()
                    # SPACEMINE SUPERWEAPON PLAYER 1
                    if superweapon[0] == 2:
                        if frame_nr > frame_cd1 + 200 and ship1.alive:
                            frame_cd1 = frame_nr
                            spaceminelist.append(ship1.start_spacemine(frame_nr))
                if (event.key == K_s):
                    # LIGHTSPEED SUPERWEAPON PLAYER 2
                    if superweapon[1] == 1:
                        if frame_nr > frame_cd2 + 200 and ship2.alive:
                            kill_bool = [False, False, False]
                            kill_bool = ship2.start_lightspeed(ship1, ship3, ship4)
                            if kill_bool[0]:
                                explosion_super2 = Explode(ship1.x, ship1.y)
                                ship1 = Ship(x * 0.8, y * 0.8, 1)
                                p1_score -= 1
                                p2_score += 3
                            if kill_bool[1]:
                                explosion_super2 = Explode(ship3.x, ship3.y)
                                ship3 = Ship(x * 0.1, y * 0.1, 3)
                                p3_score -= 1
                                p2_score += 3
                            if kill_bool[2]:
                                explosion_super2 = Explode(ship4.x, ship4.y)
                                ship4 = Ship(x * 0.8, y * 0.2, 4)
                                p4_score -= 1
                                p2_score += 3
                            frame_cd2 = frame_nr
                        ship2.stop_lightspeed()
                    # SPACEMINE SUPERWEAPON PLAYER 2
                    if superweapon[1] == 2:
                        if frame_nr > frame_cd2 + 200 and ship2.alive:
                            frame_cd2 = frame_nr
                            spaceminelist.append(ship2.start_spacemine(frame_nr))
                if (event.key == K_k):
                    # LIGHTSPEED SUPERWEAPON PLAYER 3
                    if superweapon[2] == 1:
                        if frame_nr > frame_cd3 + 200 and ship3.alive:
                            kill_bool = [False, False, False]
                            kill_bool = ship3.start_lightspeed(ship1, ship2, ship4)
                            if kill_bool[0]:
                                explosion_super3 = Explode(ship1.x, ship1.y)
                                ship1 = Ship(x * 0.8, y * 0.8, 1)
                                p1_score -= 1
                                p3_score += 3
                            if kill_bool[1]:
                                explosion_super3 = Explode(ship2.x, ship2.y)
                                ship2 = Ship(x * 0.2, y * 0.8, 2)
                                p2_score -= 1
                                p3_score += 3
                            if kill_bool[2]:
                                explosion_super3 = Explode(ship4.x, ship4.y)
                                ship4 = Ship(x * 0.8, y * 0.2, 4)
                                p4_score -= 1
                                p3_score += 3
                            frame_cd3 = frame_nr
                        ship3.stop_lightspeed()
                    # SPACEMINE SUPERWEAPON PLAYER 3
                    if superweapon[2] == 2:
                        if frame_nr > frame_cd3 + 200 and ship3.alive:
                            frame_cd3 = frame_nr
                            spaceminelist.append(ship3.start_spacemine(frame_nr))
                if (event.key == K_g):
                    # LIGHTSPEED SUPERWEAPON PLAYER 4
                    if superweapon[3] == 1:
                        if frame_nr > frame_cd4 + 200 and ship4.alive:
                            kill_bool = [False, False, False]
                            kill_bool = ship4.start_lightspeed(ship1, ship2, ship3)
                            if kill_bool[0]:
                                explosion_super4 = Explode(ship1.x, ship1.y)
                                ship1 = Ship(x * 0.8, y * 0.8, 1)
                                p1_score -= 1
                                p4_score += 3
                            if kill_bool[1]:
                                explosion_super4 = Explode(ship2.x, ship2.y)
                                ship2 = Ship(x * 0.2, y * 0.8, 2)
                                p2_score -= 1
                                p4_score += 3
                            if kill_bool[2]:
                                explosion_super4 = Explode(ship3.x, ship3.y)
                                ship3 = Ship(x * 0.8, y * 0.2, 4)
                                p3_score -= 1
                                p4_score += 3
                            frame_cd4 = frame_nr
                        ship4.stop_lightspeed()
                    # SPACEMINE SUPERWEAPON PLAYER 4
                    if superweapon[3] == 2:
                        if frame_nr > frame_cd4 + 200 and ship4.alive:
                            frame_cd4 = frame_nr
                            spaceminelist.append(ship4.start_spacemine(frame_nr))


            elif event.type == KEYUP:
                if (event.key == K_RIGHT):
                    ship1.change_angle("RIGHT2", ship1.lukas)
                if (event.key == K_LEFT):
                    ship1.change_angle("LEFT2", ship1.lukas)
                if (event.key == K_a):
                    ship2.change_angle("LEFT2", ship2.lukas)
                if (event.key == K_d):
                    ship2.change_angle("RIGHT2", ship2.lukas)
                if (event.key == K_j):
                    ship3.change_angle("LEFT2", ship3.lukas)
                if (event.key == K_l):
                    ship3.change_angle("RIGHT2", ship3.lukas)
                if (event.key == K_f):
                    ship4.change_angle("LEFT2", ship4.lukas)
                if (event.key == K_h):
                    ship4.change_angle("RIGHT2", ship4.lukas)

        pygame.display.update()
        fpsClock.tick(60)

        if not intro_played:
            intro([ship1, ship2, ship3, ship4])
            intro_played = True


if __name__ == "__main__":
    main()
