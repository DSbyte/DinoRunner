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

def baseAnimation():
    screen.blit(baseSurface, (basePos,300))
    screen.blit(baseSurface, (basePos + 820 ,300))

    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(backgroundSurface, (0,0))
    
    basePos-=1
    if basePos < -820:
        basePos=0

    baseAnimation()

    pygame.display.update()
    clock.tick(60)


