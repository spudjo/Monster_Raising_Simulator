# monster location for interaction with World
import random
import pygame
import pyganim

class World_Movement:

    def __init__(self, World, Stamina):

        self.world = World
        self.stamina = Stamina

        self.width = 48
        self.height = 42

        self.x = self.world.world_x / 2
        self.y = self.world.world_y / 2

        self.hitbox_x = self.x + self.width
        self.hitbox_y = self.y + self.height

        self.center_x = (self.x + self.hitbox_x) / 2
        self.center_y = (self.y + self.hitbox_y) / 2

        self.wandering_speed_x = 10
        self.wandering_speed_y = 10

        # randomize wandering x direction
        if random.random() > .5:
            self.wandering_speed_x *= -1

        # randomize wandering x direction
        if random.random() > .5:
            self.wandering_speed_y *= -1

        self.sleep_animation = pyganim.PygAnimation([('assets/slime/blue/sleep/0.png', 25),
                                                     ('assets/slime/blue/sleep/1.png', 25)])

        self.rest_animation = pyganim.PygAnimation([('assets/slime/blue/rest/0.png', 25),
                                                    ('assets/slime/blue/rest/1.png', 25)])

        self.idle_animation = pyganim.PygAnimation([('assets/slime/blue/idle/0.png', 25),
                                                    ('assets/slime/blue/idle/1.png', 25)])

    def sleep_movement(self):
        self.sleep_animation.play()
        self.sleep_animation.blit(self.world.surface, (self.x, self.y))

    def rest_movement(self):
        self.rest_animation.play()
        self.rest_animation.blit(self.world.surface, (self.x, self.y))

    # slime idle movement behaviour
    def idle_movement(self):

        # chance used for movement chance
        x_chance_to_move = random.uniform(0, 1)
        y_chance_to_move = random.uniform(0, 1)

        # makes chance of creature's x changing on wander random
        if x_chance_to_move > 0.5:
            # reverse direction when close to World x border
            if self.x >= self.world.world_x - 100 and self.wandering_speed_x > 0:
                self.wandering_speed_x = -self.wandering_speed_x
            elif self.x <= 50 and self.wandering_speed_x < 0:
                self.wandering_speed_x = -self.wandering_speed_x

            # change x in opposite direction 20% of the time
            if x_chance_to_move > .9:
                self.wandering_speed_x = -self.wandering_speed_x
            self.x = self.x + (self.wandering_speed_x * random.uniform(0.5, 1))

        # makes chance of creature's y changing on wander random
        if y_chance_to_move > 0.5:
            # reverse direction when close to World y border
            if self.y >= self.world.world_y - 100 and self.wandering_speed_y > 0:
                self.wandering_speed_y = -self.wandering_speed_y
            elif self.y <= 50 and self.wandering_speed_y < 0:
                self.wandering_speed_y = -self.wandering_speed_y

            # change y in opposite direction 20% of the time
            if y_chance_to_move > .9:
                self.wandering_speed_y = -self.wandering_speed_y
            self.y = self.y + (self.wandering_speed_y * random.uniform(0.5, 1))

        self.idle_animation.play()
        self.idle_animation.blit(self.world.surface, (self.x, self.y))

# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_coordinates(self):
        print("X-Coord: " + str(self.x))
        print("Y-Coord: " + str(self.y))

    def display_wandering_values(self):
        print("X-Wandering: " + str(self.wandering_speed_x))
        print("Y-Wandering: " + str(self.wandering_speed_y))

    def display_values(self):
        self.display_coordinates()
        self.display_wandering_values()

# ----------------------------------------------------------------------------------------------------------------------
#   Update Functions

    def update_movement(self):
        if self.stamina.activity_level.name == 'Sleep':
            self.sleep_movement()

        elif self.stamina.activity_level.name == 'Rest':
            self.rest_movement()

        elif self.stamina.activity_level.name == "Idle":
            self.idle_movement()

        elif self.stamina.activity_level.name == "Light":
            self.idle_animation.blit(self.world.surface, (self.x, self.y))

        elif self.stamina.activity_level.name == "Moderate":
            self.idle_animation.blit(self.world.surface, (self.x, self.y))

        elif self.stamina.activity_level.name == "Heavy":
            self.idle_animation.blit(self.world.surface, (self.x, self.y))
        pygame.draw.rect(self.world.surface, (25, 25, 25), [self.x, self.y, 48, 42], 1)

    def update_hitbox_values(self):
        self.hitbox_x = self.x + self.width
        self.hitbox_y = self.y + self.height

    def update(self):
        self.update_movement()
        self.update_hitbox_values()
