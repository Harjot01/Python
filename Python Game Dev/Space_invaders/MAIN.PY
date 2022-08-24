import pygame
import random
import math
from pygame.constants import KEYDOWN

#initialising pygame
pygame.init()

#adding sounds
pygame.mixer.init()

#adding background
background = pygame.image.load("background.png")

#Creating game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

#Colors
Red = (255, 0, 0)
Black = (0, 0, 0)

#Player
playerimg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0


#Enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 10
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(5)
    enemyY_change.append(40)

#bullet state
bullet_state = "ready"

#Bullet
bulletimg = pygame.image.load("bullets.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y):
    screen.blit(enemyimg[i], (x, y))

def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False
    
def game_over_text():
    gameover = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(gameover, (260, 257))

#Score


font = pygame.font.Font('freesansbold.ttf', 32)
scorex = 10
scorey = 180
score = 0

def show_score(scorex, scorey):
    score_val = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_val, (scorex, scorey))

over_font = font = pygame.font.Font('font.ttf', 64)

#Game loop
running = True
while running:

    screen.fill(Black)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               playerX_change = 8

            if event.key == pygame.K_LEFT:
               playerX_change = -8

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet(bulletX, bulletY)
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                
           

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #enemy movement
    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i]  = -3
            enemyY[i] += enemyY_change[i]

        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            enemyY[i] > 2000
            pygame.mixer.music.load('explosion.wav')
            pygame.mixer.music.play()
            bulletY = 480
            bullet_state = "ready"
            score += 10
            print(score)

            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i])
        
    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    
    if bullet_state == "fire":
        pygame.mixer.music.load('shot_sound.wav')
        pygame.mixer.music.play()
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    

    player(playerX, playerY)
    show_score(scorex, scorey)
    pygame.display.update()
    