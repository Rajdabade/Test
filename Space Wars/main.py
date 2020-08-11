import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))


# Sound
mixer.music.load("background.mp3")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Wars")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Alien1
alienImg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
num_of_aliens = 6

for i in range(num_of_aliens):
    alienImg.append(pygame.image.load('alien.png'))
    alienX.append(random.randint(0, 736))
    alienY.append(random.randint(50, 150))
    alienX_change.append(0.5)
    alienY_change.append(40)


# Alien2
alienpImg = []
alienpX = []
alienpY = []
alienpX_change = []
alienpY_change = []
num_of_aliensp = 6

for i in range(num_of_aliensp):
    alienpImg.append(pygame.image.load('alienp.png'))
    alienpX.append(random.randint(0, 736))
    alienpY.append(random.randint(50, 150))
    alienpX_change.append(1)
    alienpY_change.append(80)

# boss
bossImg = pygame.image.load('boss.png')
bossX = 250
bossY = -2000
bossY_change = 0.4



# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullets.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)


textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# warning text
warning = pygame.font.Font('freesansbold.ttf', 32)

# Warning text2
warning2 = pygame.font.Font('freesansbold.ttf', 32)

# You Won text
won = pygame.font.Font('freesansbold.ttf', 64)

#level
level_no = 1
level_font = pygame.font.Font('freesansbold.ttf', 64)

levelX = 600
levelY = 10


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 255, 255))
    screen.blit(score, (x, y))


def show_level(x, y):
    level_var = font.render("LEVEL: " + str(level_no), True, (255, 0, 255))
    screen.blit(level_var, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def warning_text():
    war = font.render("Warning aliens are too close", True, (0, 255, 0))
    screen.blit(war, (200, 50))

def warning_text2():
    war2 = font.render("Boss is coming", True, (255,0,0))
    screen.blit(war2, (250,10))

def you_won():
    win = won.render("YOU WON", True, (0,0,255))
    screen.blit(win, (200,250))

def player(x, y):
    screen.blit(playerImg, (x, y))


def alien(x, y, i):
    screen.blit(alienImg[i], (x, y))


def alienp(x, y, i):
    screen.blit(alienpImg[i], (x, y))

def boss(x, y):
    screen.blit(bossImg, (bossX , bossY))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt(math.pow(alienX - bulletX, 2) + (math.pow(alienY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def isCollision2(alienpX, alienpY, bulletX, bulletY):
    distance2 = math.sqrt(math.pow(alienpX - bulletX, 2) + (math.pow(alienpY - bulletY, 2)))
    if distance2 < 41:
        return True
    else:
        return False

def isCollision3(bossX, bossY, bulletX, bulletY):
    distance3 = math.sqrt(math.pow(bossX - bulletX, 2) + (math.pow(bossY - bulletY, 2)))
    if distance3 < 68:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                bossY_change = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0



    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    bossY += bossY_change
    if bossY > 400:
        warning_text()
    
    # Alien1 Movement
    for i in range(num_of_aliens):
        if alienY[i] > 300:
            warning_text()
        # Game Over
        if alienY[i] > 440:
            for j in range(num_of_aliens):
                alienY[j] = 2000
            game_over_text()
            break

        alienX[i] += alienX_change[i]
        if alienX[i] <= 0:
            alienX_change[i] = 0.4
            alienY[i] += alienY_change[i]
        elif alienX[i] >= 736:
            alienX_change[i] = -0.4
            alienY[i] += alienY_change[i]

    # Alien2 Movement
    for i in range(num_of_aliensp):
        if alienpY[i] > 320:
            warning_text()
        # Game Over
        if alienpY[i] > 420:
            for j in range(num_of_aliensp):
                alienpY[j] = 2000
                bossY = 2000
                screen.fill((255,0,0))
            game_over_text()
            break

        alienpX[i] += alienpX_change[i]
        if alienpX[i] <= 0:
            alienpX_change[i] = 0.8
            alienpY[i] += alienpY_change[i]
        elif alienpX[i] >= 736:
            alienpX_change[i] = -0.8
            alienpY[i] += alienY_change[i]

        # Collision1
        collision1 = isCollision(alienX[i], alienY[i], bulletX, bulletY)
        if collision1:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 3
            alienX[i] = random.randint(0, 736)
            alienY[i] = random.randint(50, 150)

        alien(alienX[i], alienY[i], i)

        # Collision2
        collision2 = isCollision(alienpX[i], alienpY[i], bulletX, bulletY)
        if collision2:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 15
            alienpX[i] = random.randint(0, 736)
            alienpY[i] = random.randint(50, 150)
        show_level(levelX, levelY)
        alienp(alienpX[i], alienpY[i], i)

        # Collision3
        collision3 = isCollision3(bossX, bossY, bulletX, bulletY)
        if collision3:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 50
            bossX = -200
            bossY = -200
            screen.fill((255,0,255))

            if collision3:
                for j in range(num_of_aliens and num_of_aliensp):
                    alienY[j] = -2000
                    alienpY[j] = -2000
                
        if bossX == -200:
            bossY = -200
            screen.fill((255,0,255))
            you_won()
            break




        # Levels
        if score_value >= 100:
            level_no = 2

        if score_value >= 250:
            level_no = 3

        if score_value >= 400:
            level_no = 4

        if score_value >= 500:
            level_no = "Last"
            warning_text2()

        
           
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    boss(bossX, bossY)
    show_score(textX, testY)
    pygame.display.update()
