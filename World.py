# 妖怪牧場
import pygame, sys
from monsters.Blue_Slime import Blue_Slime
from food.Berry import Berry
from monsters.miscellaneous.Activity_Level import Activity_Level
import time


class World:

    def __init__(self):

        pygame.init()  # initiate pygame
        self.FPS = 60

        self.creature_container = []
        self.name_array = ['Monokai', 'Creme', 'Sbeve']
        self.name_tracker = 0


        self.food_container = []
        self.width = 800
        self.height = 600
        self.surface = pygame.display.set_mode((self.width, self.height))  # pygame.Surface object for the window
        self.surface_color = (245, 245, 220)
        self.surface.fill(self.surface_color)
        self.update_counter = 0
        pygame.display.set_caption('Yōkai Ranch')
        self.time_start = time.time()

    def update_food_container(self):
        for food in self.food_container:
            if food.is_eaten:
                self.food_container.remove(food)

    def spawn_slime(self):
        if self.name_tracker < 3:
            self.creature_container.append(Blue_Slime(self.name_array[self.name_tracker], self))
            self.name_tracker += 1





World = World()


day_tracker = 0

while True:  # main game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # create food
            if event.key == pygame.K_f:
                x, y = pygame.mouse.get_pos()
                if len(World.food_container) < (3 + (len(World.creature_container) * 3)):
                    berry = Berry(World, x , y)
                    World.food_container.append(berry)

            # set all food is_destroyed to True
            if event.key == pygame.K_d:
                for food in World.food_container:
                    food.destroy()

            if event.key == pygame.K_s:
                World.spawn_slime()

            '''
            if event.key == pygame.K_a:
                if slime.body.stamina.activity_level.name == 'Sleep':
                    slime.body.stamina.activity_level = Activity_Level['Rest']
                elif slime.body.stamina.activity_level.name == 'Rest':
                    slime.body.stamina.activity_level = Activity_Level['Idle']
                elif slime.body.stamina.activity_level.name == "Idle":
                    slime.body.stamina.activity_level = Activity_Level['Light']
                elif slime.body.stamina.activity_level.name == "Light":
                    slime.body.stamina.activity_level = Activity_Level['Moderate']
                elif slime.body.stamina.activity_level.name == "Moderate":
                    slime.body.stamina.activity_level = Activity_Level['Heavy']
                elif slime.body.stamina.activity_level.name == 'Heavy':
                    slime.body.stamina.activity_level = Activity_Level['Sleep']
            '''

    if World.update_counter == World.FPS:

        print("----------------------------------------")
        print("W O R L D - S T A T S")
        print("----------------------------------------")
        print("Time Elapsed: " + str(round(time.time() - World.time_start, 0)) + " seconds")
        print("Creatures: " + str(World.creature_container))
        print("Food: " + str(World.food_container))
        print("")

        World.surface.fill(World.surface_color)


        for each in World.food_container:
            each.update()

        for each in World.creature_container:
            each.update()

        #'''
        for each in World.creature_container:
            each.display_values()
        #'''

        World.update_food_container()

        World.update_counter = 0

    #World.surface.fill(World.surface_color)
    #slime.update()
    #slime.display_values()

    pygame.display.update()
    pygame.time.Clock().tick(World.FPS)
    World.update_counter += 1
