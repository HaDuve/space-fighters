#!/usr/bin/env python
import sys
import pygame
import math
import random
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


class Ship:

    def __init__(self, x, y, player):
        self.image = SHIP1
        self.x = random.choice(range(5, 11)) * x / 10
        self.y = random.choice(range(5, 11)) * y / 10
        self.speed = shipspeed[player - 1]
        self.direction = 0
        self.k_left = self.k_right = 0
        self.player = player
        self.lukas = False
        self.boolean = False
        self.direc = ""
        self.alive = True

    def respawntime(self):
        pass

    def move(self):
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
        m = maneuv[self.player - 1]
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


class Rocket:

    def __init__(self, x, y, direction, exists, player):
        self.x = x
        self.y = y
        self.speed = 1
        self.direction = direction
        self.exists = exists
        self.player = player

    def move(self):
        if self.exists:
            if self.speed < rocketspeed[self.player - 1]:
                self.speed += self.speed * 0.1 + 0.7
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
        explosionSound.play()

    def update(self):
        # TODO make this temporary with animation based on frame_nr
        DISPLAY.blit(EXPLOSION, (self.x, self.y))


class Luk_powerup():
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
        # Get all Events
        if p1 > p2 and p1 > p3 and p1 > p4:
            score = "Player 1 has won with " + str(p1) + " points!"
        if p1 < p2 and p2 > p3 and p2 > p4:
            score = "Player 2 has won with " + str(p2) + " points!"
        if p3 > p1 and p3 > p2 and p3 > p4:
            score = "Player 3 has won with " + str(p3) + " points!"
        if p4 > p1 and p4 > p2 and p4 > p3:
            score = "Player 4 has won with " + str(p4) + " points!"
        text_dead = BIGFONT.render(score, True, WHITE, BLACK)
        DISPLAY.blit(text_dead, (200, 150))
        text_dead1 = FONT.render("Blue   (Player1): " + str(p1), True, WHITE, BLUE)
        text_dead2 = FONT.render("Red    (Player2): " + str(p2), True, WHITE, RED)
        text_dead3 = FONT.render("Green (Player3): " + str(p3), True, WHITE, GREEN)
        text_dead4 = FONT.render("Orange (Player4): " + str(p4), True, WHITE, ORANGE)
        text_restart = FONT.render(" <<< Restart Game >>> <Y> OR <N>", True, WHITE, BLACK)

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
        pygame.display.update()
        fpsClock.tick(30)


def intro(ships):
    main_txt1 = "ready up"
    done = False
    i = SCREENHEIGHT
    while not done and i > 102:
        if i > 100:
            i -= 1
        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND,(0,0))

        p1_txt = SPACEFONT.render(main_txt1, True, WHITE)
        DISPLAY.blit(p1_txt,(200, i))

        for ship in ships:
            if ship.alive:
                DISPLAY.blit(ship.image, (ship.x, ship.y))


        pygame.display.update()
        fpsClock.tick(60)


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

    # INITIALIZE SHIPS AND DIRECTION
    explosionSound.set_volume(0)
    missileSound.set_volume(0)
    x = SCREENWIDTH
    y = SCREENHEIGHT
    ship1 = Ship(x * 0.8, y * 0.8, 1)
    ship2 = Ship(x * 0.2, y * 0.8, 2)
    ship3 = Ship(x * 0.1, y * 0.1, 3)
    ship4 = Ship(x * 0.8, y * 0.2, 4)
    ship1.move()
    ship2.move()
    ship3.move()
    ship4.move()



    rocket1 = Rocket(999, 999, 0, False, 1)
    rocket2 = Rocket(999, 999, 0, False, 2)
    rocket3 = Rocket(999, 999, 0, False, 3)
    rocket4 = Rocket(999, 999, 0, False, 4)
    explosion = Explode(x + 500, y + 500)
    explosion1 = Explode(x + 500, y + 500)
    explosion2 = Explode(x + 500, y + 500)
    explosion3 = Explode(x + 500, y + 500)
    explosion4 = Explode(x + 500, y + 500)
    explosionSound.set_volume(0.5)
    missileSound.set_volume(0.3)

    # INITIALIZE LUKAS POWERUP
    luk = Luk_powerup()
    luk_initialized = False
    luk.alive = False

    # INITIALIZE POINTS FOR PLAYERS
    p1_score = 0
    p2_score = 0
    p3_score = 0
    p4_score = 0

    frame_nr = frame_start = frame_start1 = frame_start2 = frame_start3 = 0

    # MAINLOOP

    intro([ship1, ship2, ship3, ship4])
    while 1:

        frame_nr += 1
        DISPLAY.fill(BLACK)
        DISPLAY.blit(BACKGROUND, (0, 0))
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
        explosion.update()
        explosion1.update()
        explosion2.update()
        explosion3.update()
        explosion4.update()

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
        p3_txt = BIGFONT.render(" " + str(p3_score) + " ", True, WHITE, GREEN)
        DISPLAY.blit(p3_txt, (50, SCREENHEIGHT - 50))
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
                    pygame.quit()
                    sys.exit()

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


if __name__ == "__main__":
    main()
