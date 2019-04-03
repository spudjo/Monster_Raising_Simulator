# monster location for interaction with World
# TODO: better way of handling collision detection of creature and walls, look into https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect
#       speed should be influenced by carrying weight (add max carry_weight, based on str)
# TODO: not really sure about some of the functions here, specifically those relating to food,
#       might make more sense to make a separate behaviour class for food related behaviours?

import random
import pygame
import pyganim
import math
from creature_files.miscellaneous.Activity_Level import Activity_Level


class World_Movement:

    def __init__(self, body, container):

        self.container = container
        self.body = body
        self.stomach = body.get_body_parts('stomach')[0]

        self.width = 48     # may keep this hardcoded
        self.height = 42    # may keep this hardcoded

        self.closest_food = None

        # creature_files (x, y) hitbox coordinates
        # there's definitely a better way to do this but im keeping it like this for reasons ¯\_(ツ)_/¯
        self.x = ((self.container.width - self.width) / 2) * random.uniform(0.85, 1.15)
        self.y = ((self.container.height - self.height) / 2) * random.uniform(0.85, 1.15)

        self.x2 = self.x + self.width
        self.y2 = self.y

        self.x3 = self.x
        self.y3 = self.y + self.height

        self.x4 = self.x2
        self.y4 = self.y3

        self.x_center = self.x + self.width / 2
        self.y_center = self.y + self.height / 2

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

        self.movement_speed_x = self.body.stats.base['spd']
        self.movement_speed_y = self.body.stats.base['spd']

        # randomize wandering x direction
        if random.random() > .5:
            self.movement_speed_x *= -1

        # randomize wandering x direction
        if random.random() > .5:
            self.movement_speed_y *= -1

        assets_directory = 'assets/creatures/' + str.lower(self.body.__class__.__name__) + '/' + str.lower(self.body.creature.__class__.__name__) + '/'

        self.sleep_animation = pyganim.PygAnimation([(assets_directory + 'sleep/0.png', 25),
                                                     (assets_directory + 'sleep/1.png', 25)])
        self.rest_animation = pyganim.PygAnimation([(assets_directory + 'rest/0.png', 25),
                                                    (assets_directory + 'rest/1.png', 25)])
        self.idle_animation = pyganim.PygAnimation([(assets_directory + 'idle/0.png', 25),
                                                    (assets_directory + 'idle/1.png', 25)])

    # ----------------------------------------------------------------------------------------------------------------------
    #   Movement Functions

    def move_to_food(self):

        x2 = self.closest_food.x
        y2 = self.closest_food.y

        if self.movement_speed_x >= self.get_distance(self.closest_food):
            self.x = x2
            self.y = y2
        else:
            if self.x is not x2:
                if self.x < x2:
                    if self.movement_speed_x < 0:
                        self.movement_speed_x *= -1
                elif self.x > x2:
                    if self.movement_speed_x > 0:
                        self.movement_speed_x *= -1
                self.x = self.x + self.movement_speed_x

            if self.y is not y2:
                if self.y < y2:
                    if self.movement_speed_y < 0:
                        self.movement_speed_y *= -1
                elif self.y > y2:
                    if self.movement_speed_y > 0:
                        self.movement_speed_y *= -1
                self.y = self.y + self.movement_speed_y

        self.update_coords()
        self.update_hitbox()
        # self.display_hitbox()
        # self.display_vision_radius()
        self.idle_animation.play()
        self.idle_animation.blit(self.container.surface, (self.x, self.y))

        if self.hitbox.colliderect(self.closest_food.hitbox):
            self.stomach.eat(self.closest_food)

    def sleep_movement(self):

        self.update_coords()
        # self.display_hitbox()
        # self.display_vision_radius()
        self.sleep_animation.play()
        self.sleep_animation.blit(self.container.surface, (self.x, self.y))

    def rest_movement(self):

        self.update_coords()
        # self.display_hitbox()
        # self.display_vision_radius()
        self.rest_animation.play()
        self.rest_animation.blit(self.container.surface, (self.x, self.y))

    # slime idle movement behaviour
    def idle_movement(self):
        # chance used for movement chance
        x_chance_to_move = random.uniform(0, 1)
        y_chance_to_move = random.uniform(0, 1)

        # makes chance of creature's x changing on wander random
        if x_chance_to_move > 0.25:
            # reverse direction when close to Container x border
            if self.x2 >= self.container.width and self.movement_speed_x > 0:
                self.movement_speed_x = -self.movement_speed_x
            elif self.x <= 0 and self.movement_speed_x < 0:
                self.movement_speed_x = -self.movement_speed_x

            # change x in opposite direction 15% of the time
            if x_chance_to_move > .85:
                self.movement_speed_x = -self.movement_speed_x
            self.x = self.x + (self.movement_speed_x * random.uniform(0.5, 1))

        # makes chance of creature's y changing on wander random
        if y_chance_to_move > 0.25:
            # reverse direction when close to Container y border
            if self.y4 >= self.container.height and self.movement_speed_y > 0:
                self.movement_speed_y = -self.movement_speed_y
            elif self.y <= 0 and self.movement_speed_y < 0:
                self.movement_speed_y = -self.movement_speed_y

            # change y in opposite direction 15% of the time
            if y_chance_to_move > .85:
                self.movement_speed_y = -self.movement_speed_y
            self.y = self.y + (self.movement_speed_y * random.uniform(0.5, 1))

        self.update_coords()
        self.update_hitbox()
        # self.display_hitbox()
        # self.display_vision_radius()
        self.idle_animation.play()
        self.idle_animation.blit(self.container.surface, (self.x, self.y))

    # ----------------------------------------------------------------------------------------------------------------------
    #   Calculation Functions

    # checks all food in container.food_array and returns instance of the closest food for tracking
    def get_closest_food(self):

        if len(self.container.food_container) > 0:
            for food in self.container.food_container:
                if self.get_distance(food) <= self.body.stats.explore.get('vis'):
                    if self.closest_food is None:
                        self.closest_food = food
                    elif self.get_distance(self.closest_food) > self.get_distance(food):
                        self.closest_food = food
        else:
            self.closest_food = None

    # calculate and return distance between self and another object based on x,y coords (center)
    def get_distance(self, other):

        x2 = other.x_center
        y2 = other.y_center
        return math.sqrt(math.pow((x2 - self.x_center), 2) + math.pow((y2 - self.y_center), 2))

    # sets self.closest_food to instance of closest food object within vision range
    def search_for_food(self):

        self.get_closest_food()

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    def update_hitbox(self):

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def update_movement(self):

        if self.stomach.is_hungry and self.body.resources.stamina.activity_level.name is not 'Sleep':
            self.search_for_food()
            if self.closest_food is not None:
                # sets activity mode to Light if hungry and food is found, then move towards food
                self.body.resources.stamina.activity_level = Activity_Level['Light']
                self.move_to_food()
            else:
                # sets activity mode to idle if hungry, not asleep and no food is found
                self.body.resources.stamina.activity_level = Activity_Level['Idle']

        else:
            # commented out as it will cause creatures to wake up immediately after 1 tick when hungry!
            #self.body.resources.stamina.activity_level = Activity_Level['Idle']
            self.closest_food = None

        if self.body.resources.stamina.activity_level.name == 'Sleep':
            self.sleep_movement()

        elif self.body.resources.stamina.activity_level.name == 'Rest':
            self.rest_movement()

        elif self.body.resources.stamina.activity_level.name == 'Idle':
            self.idle_movement()

        elif self.body.resources.stamina.activity_level.name == 'Light':
            self.idle_animation.play()
            self.idle_animation.blit(self.container.surface, (self.x, self.y))

        elif self.body.resources.stamina.activity_level.name == 'Moderate':
            self.idle_animation.play()
            self.idle_animation.blit(self.container.surface, (self.x, self.y))

        elif self.body.resources.stamina.activity_level.name == 'Heavy':
            self.idle_animation.play()
            self.idle_animation.blit(self.container.surface, (self.x, self.y))

        # update 4 corners of hitbox, useful for collision detection later on

    def update_coords(self):

        self.x2 = self.x + self.width
        self.y2 = self.y

        self.x3 = self.x
        self.y3 = self.y + self.height

        self.x4 = self.x2
        self.y4 = self.y3

        self.x_center = self.x + self.width / 2
        self.y_center = self.y + self.height / 2

    def update(self):

        self.update_movement()

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_vision_radius(self):

        pygame.draw.circle(self.container.surface, (255, 0, 0), (int(round(self.x_center, 0)), int(round(self.y_center, 0))), self.body.stats.explore.get('vis'), 1)

    def display_closest_food(self):

        print("Closest Food: " + str(self.closest_food))
        if self.closest_food is not None:
            print("Distance: " + str(self.get_distance(self.closest_food)))

    def display_coordinates(self):

        print("W O R L D - M O V E M E N T")
        print("X-Coord: " + str(self.x))
        print("Y-Coord: " + str(self.y))

    def display_wandering_values(self):

        print("X-Wandering: " + str(self.movement_speed_x))
        print("Y-Wandering: " + str(self.movement_speed_y))

    def display_values(self):

        self.display_coordinates()
        self.display_wandering_values()

    def display_hitbox(self):

        pygame.draw.rect(self.container.surface, (25, 25, 25), self.hitbox, 1)
        # display_hitbox_corners()

    def display_hitbox_corners(self):

        pygame.draw.rect(self.container.surface, (255, 0, 0), [self.x, self.y, 2, 2], 4)
        pygame.draw.rect(self.container.surface, (0, 255, 0), [self.x2, self.y2, 2, 2], 4)
        pygame.draw.rect(self.container.surface, (0, 0, 255), [self.x3, self.y3, 2, 2], 4)
        pygame.draw.rect(self.container.surface, (50, 50, 50), [self.x4, self.y4, 2, 2], 4)
