#The GUI is made using Pygame

import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((820,332))
clock = pygame.time.Clock()

game_active = True

backgroundSurface = pygame.image.load('images/bg.png').convert()
backgroundSurface = pygame.transform.scale(backgroundSurface, (820,332))

baseSurface = pygame.image.load('images/base.png').convert()
baseSurface = pygame.transform.scale(baseSurface, (820, 100))

basePos = 0

dino = pygame.image.load('images/dino.png').convert()
dino = pygame.transform.scale(dino, (130, 96))
dino_rect = dino.get_rect(center = (130, 270))

dino_movement = 0
gravity = 0.5

cactus = pygame.image.load('images/pipe-red.png').convert()
cactus = pygame.transform.scale(cactus, (21, 128))
cactus_list = []

SPAWNCACTUS = pygame.USEREVENT
pygame.time.set_timer(SPAWNCACTUS, 1200)

def baseAnimation():
    screen.blit(baseSurface, (basePos,275))
    screen.blit(baseSurface, (basePos + 820 ,275))

def create_cactus():
    new_cactus = cactus.get_rect(center = (random.choice([820,950]),270))
    sec_cactus = cactus.get_rect(center = (random.choice([820,950]), 270))
    return new_cactus, sec_cactus

def move_cactus(cactus_list):
    start_time = 0
    for c in cactus_list:
        c.centerx -= 5

    return cactus_list

def draw_cactus(cactus_list):
    for c in cactus_list:
        screen.blit(cactus, c)

def check_collision(cactus_list):
    for c in cactus_list:
        if dino_rect.colliderect(c):
            return False
    return True

       
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if dino_rect.centery == 240:
                    dino_movement = 0
                    dino_movement -= 12.5
        if event.type == SPAWNCACTUS:
            cactus_list.extend(create_cactus())
            


    
    
    screen.blit(backgroundSurface, (0,0))
    # screen.blit(cactus, (100,165))

    if game_active:
        # Dino
        dino_movement = min((dino_movement + gravity),10)
        dino_rect.centery = min ((dino_rect.centery + dino_movement), 240)
        screen.blit(dino, dino_rect)

        game_active = check_collision(cactus_list)
        # Cactus
        cactus_list = move_cactus(cactus_list)
        draw_cactus(cactus_list)

    basePos-=1
    if basePos < -820:
        basePos=0

    baseAnimation()

    pygame.display.update()
    clock.tick(60)


