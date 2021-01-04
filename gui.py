#The GUI is made using Pygame

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((820,332))
clock = pygame.time.Clock()

backgroundSurface = pygame.image.load('images/bg.png').convert()
backgroundSurface = pygame.transform.scale(backgroundSurface, (820,332))

baseSurface = pygame.image.load('images/base.png').convert()
baseSurface = pygame.transform.scale(baseSurface, (820, 100))

basePos = 0

dino = pygame.image.load('images/dino.png').convert()
dino = pygame.transform.scale(dino, (109, 80))
dino_rect = dino.get_rect(center = (100, 270))

dino_movement = 0
gravity = 0.5

# cactus = pygame.image.load('images/cactus.png').convert()
# # cactus = pygame.transform.scale(cactus, (109, 80))

def baseAnimation():
    screen.blit(baseSurface, (basePos,300))
    screen.blit(baseSurface, (basePos + 820 ,300))

    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if dino_rect.centery == 270:
                    dino_movement = 0
                    dino_movement -= 10

    
    screen.blit(backgroundSurface, (0,0))
    # screen.blit(cactus, (0,0))
    dino_movement = min((dino_movement + gravity),10)
    dino_rect.centery = min ((dino_rect.centery + dino_movement), 270)
    screen.blit(dino, dino_rect)

    basePos-=1
    if basePos < -820:
        basePos=0

    baseAnimation()

    pygame.display.update()
    clock.tick(60)


