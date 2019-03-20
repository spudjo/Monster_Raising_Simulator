# 妖怪牧場
import pygame, sys
from Slime import Slime
from Berry import Berry
from Activity_Level import Activity_Level
import time

# ----------------------------------------------------------------------------------------------------------------------
#'''
pygame.init()  # initiate pygame
display_width = 800
display_height = 600
FPS = 60
surface = pygame.display.set_mode((display_width, display_height)) # pygame.Surface object for the window
surface_color = (245, 245, 220)
surface.fill(surface_color)
pygame.display.set_caption('Yōkai Ranch')
# ----------------------------------------------------------------------------------------------------------------------

slime = Slime("Monokai", display_width / 2, display_height / 2, surface)
update_counter = 0
food_container = []


while True:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if len(food_container) < 5:
                    berry = Berry(surface)
                    food_container.append(food_container)


    update_counter += 1

    if update_counter == FPS:

        #slime.activity_level = Activity_Level.Sleep
        slime.update()
        slime.display_stats()
        update_counter = 0


    pygame.display.update()
    pygame.time.Clock().tick(FPS)