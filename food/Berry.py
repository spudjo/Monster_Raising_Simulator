from random import randint
import Activity_Level
import pygame

class Berry():

    def __init__(self, surface):
        self.name = "Berry"
        self.nutrition = 10
        self.x = randint(10, surface.get_width()-20)
        self.y = randint(10, surface.get_height()-10)

        body = pygame.image.load("assets/food/9.png")
        surface.blit(body, (self.x,  self.y))

