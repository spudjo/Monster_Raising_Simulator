# 妖怪牧場
import pygame, sys
from Slime import Slime
from Berry import Berry
from Activity_Level import Activity_Level
import time


class World():

    def __init__(self):
        pygame.init()  # initiate pygame
        self.FPS = 60
        self.food_container = []
        self.world_x = 800
        self.world_y = 600
        self.surface = pygame.display.set_mode((self.world_x, self.world_y))  # pygame.Surface object for the window
        self.surface_color = (245, 245, 220)
        self.surface.fill(self.surface_color)
        pygame.display.set_caption('Yōkai Ranch')


World = World()
slime = Slime("Monokai", World.world_x / 2, World.world_y / 2, World)
update_counter = 0
day_tracker = 0

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if len(World.food_container) < 5:
                    berry = Berry(World.surface)
                    World.food_container.append(World.food_container)

    update_counter += 1

    if update_counter == World.FPS:

        #slime.activity_level = Activity_Level.Sleep
        slime.update()
        slime.display_stats()
        update_counter = 0


    pygame.display.update()
    pygame.time.Clock().tick(World.FPS)