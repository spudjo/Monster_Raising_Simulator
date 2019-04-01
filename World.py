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
        self.display_counter = 0

        self.update_increment = 1
        self.display_increment = 1
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

    def clean_waste(self, waste):
        if waste in self.waste_container:
            self.waste_container.remove(waste)

    def clean_food(self, food):
        if food in self.food_container:
            self.food_container.remove(food)



World = World()
paused = False
day_tracker = 0

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused is True:
                    paused = False
                    print("Game Resumed")
                else:
                    paused = True
                    print("Game Paused")

        if event.type == pygame.KEYDOWN and not paused:
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


            # TODO: THIS
            if event.key == pygame.K_c:
                waste_deleted = False
                x, y = pygame.mouse.get_pos()
                click_radius = 10

                for waste in World.waste_container:
                    waste.display_location()
                    for num1 in range(-click_radius, click_radius):
                        for num2 in range(-click_radius, click_radius):

                            #print(("(" + str(x + num1) + ", " + str(y + num2) + ")"))
                            #pygame.draw.rect(World.surface, (0, 0, 255), [x + num1, y + num2, 1, 1], 1)

                            if waste.x == (x + num1) and waste.y == (y + num2) and waste_deleted is False:
                                print("Waste Cleaned!")
                                World.clean_waste(waste)
                                waste_deleted = True
                waste_deleted = False







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
    if not paused:
        World.toggle_hitbox()
        World.toggle_vision()

        if World.update_counter >= World.FPS:

            World.surface.fill(World.surface_color)

            for each in World.food_container:
                each.update()
                #each.display_values()


            for each in World.waste_container:
                each.update()

            for each in World.creature_container:
                each.update()

                #for food in each.body.stomach.contents:
                #    food.display_values()

                # display name
                font = pygame.font.Font('freesansbold.ttf', 20)
                text = font.render(each.name, True, (100, 100, 100))
                textRect = text.get_rect()
                textRect.center = (each.body.world_movement.x_center, each.body.world_movement.y_center - 40)
                World.surface.blit(text, textRect)

            World.update_counter = 0


        if World.display_counter >= World.FPS:
            print("----------------------------------------")
            print("W O R L D - S T A T S")
            print("----------------------------------------")
            print("Time Elapsed: " + str(round(time.time() - World.time_start, 0)) + " seconds")
            print("Creatures: " + str(World.creature_container))
            print("Food: " + str(World.food_container))
            print("Waste: " + str(World.waste_container))
            print("")

            for each in World.food_container:
                pass

            for each in World.waste_container:
                pass

            for each in World.creature_container:
                each.display_values()

            World.display_counter = 0




        pygame.display.update()
        pygame.time.Clock().tick(World.FPS)
        World.update_counter += World.update_increment
        World.display_counter += World.display_increment
