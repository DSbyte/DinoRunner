#The GUI is made using Pygame

import pygame
import sys
import random

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

cactus = pygame.image.load('images/cactus.png')
cactus = pygame.transform.scale(cactus, (125, 125))
cactus_list = []

SPAWNCACTUS = pygame.USEREVENT
pygame.time.set_timer(SPAWNCACTUS, 1200)

def baseAnimation():
    screen.blit(baseSurface, (basePos,275))
    screen.blit(baseSurface, (basePos + 820 ,275))

def create_cactus():
    new_cactus = cactus.get_rect(midtop = (random.choice([820,950]),165))
    sec_cactus = cactus.get_rect(midtop = (1000 - random.choice([100,150]), 165))
    return new_cactus, sec_cactus

def move_cactus(cactus_list):
    start_time = 0
    for c in cactus_list:
        c.centerx -= 5

    return cactus_list

def draw_cactus(cactus_list):
    for c in cactus_list:
        screen.blit(cactus, c)
       
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if dino_rect.centery == 245:
                    dino_movement = 0
                    dino_movement -= 12.5
        if event.type == SPAWNCACTUS:
            cactus_list.extend(create_cactus())
            


    
    
    screen.blit(backgroundSurface, (0,0))
    # screen.blit(cactus, (100,165))

    # Dino
    dino_movement = min((dino_movement + gravity),10)
    dino_rect.centery = min ((dino_rect.centery + dino_movement), 245)
    screen.blit(dino, dino_rect)

    # Cactus
    cactus_list = move_cactus(cactus_list)
    draw_cactus(cactus_list)

    basePos-=1
    if basePos < -820:
        basePos=0

    baseAnimation()

    pygame.display.update()
    clock.tick(60)


