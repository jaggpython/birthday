import pygame
import random

pygame.init()

display_width = 1100
display_height = 650



Screen = pygame.display.set_mode((display_width,display_height))

ballonImg=pygame.image.load("balloons.png")
flash = pygame.image.load("c.png")
x=100
y=100
x1=500
y1=300
flash2 = pygame.image.load("c1.png")
star = pygame.image.load("s.png")
gift = pygame.image.load("g.png")

playerX=600
playerY=500
playerX1=900
playerY1=500
playerX_change = 0

over_font = pygame.font.Font("freesansbold.ttf",64)

def game_over_text():
    over_text = over_font.render("HAPPY BIRTHDAY",True,(225,225,225))
    Screen.blit(over_text,(500,200))

def player(x,y):
    Screen.blit(ballonImg,(x,y))

def player1(x,y):
    Screen.blit(flash,(x,y))

def player2(x,y):
    Screen.blit(flash2,(x,y))
background = pygame.image.load('b.jpg')


pygame.display.set_caption("HAPPY BIRTHDAY")

img = pygame.image.load("h.png")


enemyImg = [] 
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('balloons.png'))    
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(0,150))
    enemyX_change.append(1)
    enemyY_change.append(40)

def enemy(x,y,i):
    Screen.blit(enemyImg[i], (x, y))

running=True



while True:
    Screen.blit(background,(0,0))
    Screen.blit(img,(100,100))
    playerY +=-1
    playerY1 +=-0.2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    
    

    if event.type == pygame.KEYDOWN:
            
        if event.key == pygame.K_LEFT:
            playerX_change = -7
        if event.key == pygame.K_RIGHT:
            playerX_change = 7
        

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change
    player(playerX,playerY)
    player(playerX1,playerY1)
    game_over_text()
    player1(x,y)
    player2(x1,y1)
    Screen.blit(star,(900,50))
    Screen.blit(star,(320,50))
    Screen.blit(gift,(20,500))
    Screen.blit(star,(700,500))

    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]

            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(0,150)

        enemy(enemyX[i],enemyY[i],i)

           
    pygame.display.update()







