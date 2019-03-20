# 妖怪牧場
import pygame, sys
from pygame.locals import *
import time
from yokai import *
from yokai.Slime import Slime

#'''
pygame.init()  # initiate pygame

display_width = 800
display_height = 600
FPS = 60


surface = pygame.display.set_mode((display_width, display_height)) # pygame.Surface object for the window
surface_color = (245, 245, 220)
surface.fill(surface_color)

pygame.display.set_caption('Yōkai Ranch')

slime = Slime("Name")
slime_image = pygame.image.load(slime.assets[0])
surface.blit(slime_image, (display_width / 2, display_height / 2))


while True:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    pygame.time.Clock().tick(FPS)
#'''