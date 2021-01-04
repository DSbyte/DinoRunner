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
dino_rect = dino.get_rect(center = (50, 270))

dino_movement = 0
gravity = 0.5

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
                dino_movement = 0
                dino_movement -= 10

    
    screen.blit(backgroundSurface, (0,0))

    dino_movement += gravity
    dino_rect.centery += dino_movement
    screen.blit(dino, dino_rect)

    basePos-=1
    if basePos < -820:
        basePos=0

    baseAnimation()

    pygame.display.update()
    clock.tick(60)


