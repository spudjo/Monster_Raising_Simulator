# 妖怪牧場
import pygame, sys
from monsters.Slime import Slime
from food.Berry import Berry
from monsters.miscellaneous.Activity_Level import Activity_Level
import time


class World:

    def __init__(self):
        pygame.init()  # initiate pygame
        self.FPS = 60
        self.food_container = []
        self.world_x = 800
        self.world_y = 600
        self.surface = pygame.display.set_mode((self.world_x, self.world_y))  # pygame.Surface object for the window
        self.surface_color = (245, 245, 220)
        self.surface.fill(self.surface_color)
        self.update_counter = 0
        pygame.display.set_caption('Yōkai Ranch')
        self.time_start = time.time()



World = World()
slime = Slime('Monokai', World)
#slime.idle_animation.play()

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

            if event.key == pygame.K_a:
                if slime.body.stamina.activity_level.name == 'Sleep':
                    slime.body.stamina.activity_level = Activity_Level['Rest']
                    #slime.idle_animation.pause()
                elif slime.body.stamina.activity_level.name == 'Rest':
                    slime.body.stamina.activity_level = Activity_Level['Idle']
                elif slime.body.stamina.activity_level.name == "Idle":
                    slime.body.stamina.activity_level = Activity_Level['Light']
                    #slime.idle_animation.play()
                elif slime.body.stamina.activity_level.name == "Light":
                    slime.body.stamina.activity_level = Activity_Level['Moderate']
                elif slime.body.stamina.activity_level.name == "Moderate":
                    slime.body.stamina.activity_level = Activity_Level['Heavy']
                elif slime.body.stamina.activity_level.name == "Heavy":
                    slime.body.stamina.activity_level = Activity_Level['Sleep']



    if World.update_counter == World.FPS:
        #World.surface.fill(World.surface_color)
        print("Time Elapsed: " + str(round(time.time() - World.time_start, 0)) + " " + " seconds")
        #slime.update()
        slime.display_values()
        World.update_counter = 0
    slime.update()
    pygame.draw.rect(World.surface, (25, 0, 0), [slime.body.world_movement.x, slime.body.world_movement.y, 5, 5], 5)
    '''
    if World.update_counter % 1 == 0:
        if not (slime.body.stamina.activity_level.name == 'Sleep' or slime.body.stamina.activity_level.name == 'Rest'):
            World.surface.fill(World.surface_color)
    '''

    pygame.display.update()
    pygame.time.Clock().tick(World.FPS)
    World.update_counter += 1
