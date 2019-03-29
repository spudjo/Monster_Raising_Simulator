# 妖怪牧場
import pygame, sys
from creature_files.creatures.formless.Blue_Slime import Blue_Slime
from food.Berry import Berry
from food.Drum_Stick import Drum_Stick
import time
import configparser

# TODO: world 'cleaning up' (removal of dead creature_files, eaten food, etc) should be controlled by World, current controlled within objects themselves
#   if multiple creatures collide with the same food object on the same update game will crash!

config = configparser.ConfigParser()
config.read('config.ini')
config_world = config['WORLD']


class World:

    def __init__(self):

        pygame.init()  # initiate pygame
        pygame.display.set_caption('Yōkai Ranch')

        self.FPS = 60

        self.creature_container = []
        self.name_array = ['Monokai', 'Creme', 'Slim', 'Alice', 'Bally']
        self.name_tracker = 0
        self.max_creatures = 5

        self.name_container = []

        self.food_container = []
        self.waste_container = []

        self.width = int(config_world['width'])
        self.height = int(config_world['height'])

        self.surface = pygame.display.set_mode((self.width, self.height))  # pygame.Surface object for the window
        self.surface_color = (245, 245, 220)
        self.surface.fill(self.surface_color)

        self.update_counter = 0
        self.update_increment = 1
        self.time_start = time.time()

        self.display_hitbox = False
        self.display_vision = False

    def spawn_slime(self):
        self.name_tracker = len(self.creature_container)
        if self.name_tracker < self.max_creatures:
            self.creature_container.append(Blue_Slime(self.name_array[self.name_tracker], self))

    def toggle_hitbox(self):
        if self.display_hitbox:
            for each in self.creature_container:
                each.body.world_movement.display_hitbox()

    def toggle_vision(self):
        if self.display_vision:
            for each in self.creature_container:
                each.body.world_movement.display_vision_radius()


World = World()





day_tracker = 0

while True:  # main game loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # create food
            if event.key == pygame.K_9:
                x, y = pygame.mouse.get_pos()
                if len(World.food_container) < (3 + (len(World.creature_container) * 3)):
                    berry = Berry(World, x, y)
                    World.food_container.append(berry)

            if event.key == pygame.K_0:
                x, y = pygame.mouse.get_pos()
                if len(World.food_container) < (3 + (len(World.creature_container) * 3)):
                    drum_stick = Drum_Stick(World, x, y)
                    World.food_container.append(drum_stick)

            # set all food is_destroyed to True
            if event.key == pygame.K_d:
                for food in World.food_container:
                    food.destroy()

            if event.key == pygame.K_s:
                World.spawn_slime()

            if event.key == pygame.K_1:
                if World.display_hitbox:
                    World.display_hitbox = False
                else:
                    World.display_hitbox = True

            if event.key == pygame.K_2:
                if World.display_vision:
                    World.display_vision = False
                else:
                    World.display_vision = True

            if event.key == pygame.K_z:
                if World.update_increment == 1:
                    World.update_increment = 10
                else:
                    World.update_increment = 1

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
    World.toggle_hitbox()
    World.toggle_vision()

    if World.update_counter >= World.FPS:
        #'''
        print("----------------------------------------")
        print("W O R L D - S T A T S")
        print("----------------------------------------")
        print("Time Elapsed: " + str(round(time.time() - World.time_start, 0)) + " seconds")
        print("Creatures: " + str(World.creature_container))
        print("Food: " + str(World.food_container))
        print("Waste: " + str(World.waste_container))
        print("")

        World.surface.fill(World.surface_color)

        
        for each in World.food_container:
            each.update()
            #each.display_values()


        for each in World.waste_container:
            each.update()


        for each in World.creature_container:
            each.update()
            each.display_values()
            #for food in each.body.stomach.contents:
            #    food.display_values()

            # display name
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(each.name, True, (100, 100, 100))
            textRect = text.get_rect()
            textRect.center = (each.body.world_movement.x_center, each.body.world_movement.y_center - 40)
            World.surface.blit(text, textRect)


        World.update_counter = 0
        #'''



    #World.surface.fill(World.surface_color)
    #slime.update()
    #slime.display_values()

    pygame.display.update()
    pygame.time.Clock().tick(World.FPS)
    World.update_counter += World.update_increment
