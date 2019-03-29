from random import randint
import pygame


class Urine:

    def __init__(self, Container, x, y):
        self._container = Container

        self.width = 32
        self.height = 32

        self.name = "Urine"
        self.type = "Waste"
        self.nutrition = 5
        self.weight = 2
        self.x = x
        self.y = y

        self.x_center = self.x + self.width / 2
        self.y_center = self.y + self.height / 2

        self.body = pygame.image.load("assets/misc/urine.png")
        self._container.surface.blit(self.body, (self.x, self.y))

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        # self.display_hitbox()

        self.is_edible = True
        self.is_destroyed = False

    def destroy(self):
        self.is_destroyed = True

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_location(self):
        print("Location: (" + str(self.x) + ", " + str(self.y) + ")")

    def display_values(self):
        print("Name: " + str(self.name))
        print("Type: " + str(self.type))
        self.display_location()
        print("Is Destroyed: " + str(self.is_destroyed))
        print("")

    def display_hitbox(self):
        pygame.draw.rect(self._container.surface, (25, 25, 25), self.hitbox, 1)

    def update_position(self):
        self._container.surface.blit(self.body, (self.x, self.y))
        # self.display_hitbox

    def update(self):
        self.update_position()

