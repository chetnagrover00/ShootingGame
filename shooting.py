import pygame
import random
import math
from pygame import mixer

pygame.init()

mixer.music.load('background.mp3')
mixer.music.play(-1)
screen_height = 680
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
background=pygame.image.load('back.webp')                                
pygame.display.set_caption("SHOOT LOVE")
icon = pygame.image.load('globe.png')
pygame.display.set_icon(icon)

player_Img = pygame.image.load('plant.png')
playerX = 400
playerY = 610
playerX_change = 0

enemy_Img=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_enemies=6

for i in range (num_enemies):
    enemy_Img.append(pygame.image.load('girl.png'))
    enemyX.append(random.randint(0,730))
    enemyY.append(random.randint(0,150))
    enemyX_change.append(1)
    enemyY_change.append(8)

def enemy(x,y,i):
    screen.blit(enemy_Img[i], (x, y))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    
    if distance < 30:
        return True
    else:
        return False    

bullet_Img = pygame.image.load('Hearts.png')
bulletX = 0 
bulletY =520
bulletX_change = 0
bulletY_change = 4 
bullet_state = "ready"

score=0
font = pygame.font.Font('Skate Brand.otf',32)
game_over_font = pygame.font.Font('Skate Brand.otf', 64)
screen_text_font = pygame.font.Font('Skate Brand.otf', 32)
textX = 12
textY = 12

def game_over_text():
    game_over_text = game_over_font.render("GAME OVER!", True, (0, 0, 0))
    screen.blit(game_over_text, (230, 270))
def screen_text():
    screen_text = screen_text_font.render("press Q to quit", True, (0, 0, 0))
    screen.blit(screen_text, (350, 350))


def player(x,y):
    screen.blit(player_Img, (x, y))
def show_score(x, y):
    score_1 = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_1, (x, y))
def game_loop():
    running=True
    
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_Img, (x + 5, y - 30))
   


running= True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_q:
                running = False
            
            
                
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    bullet_sound = mixer.Sound('pop.wav')
                    bullet_sound.play()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
        
            
                              
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0

    elif playerX >= 750:
        playerX = 750

    for i in range (num_enemies):
        if enemyY[i] > 450:
            for j in range(num_enemies):
                enemyY[j] = 2000
            game_over_text()
            screen_text()
            break
        enemyX[i] += enemyX_change[i]    
        if enemyX[i] <= 0:
                enemyX_change[i] = 9
                enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 740:
                enemyX_change[i] = -9
                enemyY[i] += enemyY_change[i]
                
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
                explosion_sound = mixer.Sound('pling.wav')
                explosion_sound.play()
                bulletY = 520
                bullet_state = "ready"
                score += 1
                print(score)
                
                enemyX[i] = random.randint(0,730)
                enemyY[i]= random.randint(0,150)

        enemy(enemyX[i], enemyY[i], i)
        
    if bulletY <= 0:
        bulletY = 520
        bullet_state = "ready"    

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        
   
    show_score(textX, textY)
    player(playerX, playerY)
    pygame.display.update()
    
pygame.quit()
