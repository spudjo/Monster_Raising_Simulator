import pygame


class Poop:

    def __init__(self, Container, x, y):

        self._container = Container

        self.width = 16
        self.height = 11

        self.name = "Poop"
        self.type = "Waste"
        self.nutrition = 5
        self.weight = 2
        self.x = x
        self.y = y

        self.x_center = round(self.x + self.width / 2, 0)
        self.y_center = round(self.y + self.height / 2, 0)

        self.body = pygame.image.load("assets/misc/poop.png")
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

        print("Location: (" + str(self.x_center) + ", " + str(self.y_center) + ")")

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
        #self.display_hitbox

    def update(self):
        self.update_position()
