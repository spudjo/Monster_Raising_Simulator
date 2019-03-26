from random import randint
import pygame

class Berry():

    def __init__(self, Container):
        self.container = Container

        self.name = "Berry"
        self.type = "Food"
        self.nutrition = 10
        self.weight = 5
        self.x = randint(10, self.container.width-20)
        self.y = randint(10, self.container.height-10)

        print("(" + str(self.x) + ", " + str(self.y) + ")")
        self.body = pygame.image.load("assets/food/9.png")
        self.container.surface.blit(self.body, (self.x,  self.y))
        print(self.container.width)

        self.width = 14
        self.height = 12
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.container.surface, (25, 25, 25), self.hitbox, 1)

    def update_position(self):
        self.container.surface.blit(self.body, (self.x, self.y))
        pygame.draw.rect(self.container.surface, (25, 25, 25), self.hitbox, 1)


    def update(self):
        self.update_position()

