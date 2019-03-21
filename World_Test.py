import pygame, sys
from pygame.locals import *
import pyganim

pygame.init()
windowSurface = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption('Pyganim Basic Demo')

animation = pyganim.PygAnimation([('assets/slime/blue/0.png', 0.25),
                                  ('assets/slime/blue/1.png', 0.25),
                                  ('assets/slime/blue/2.png', 0.25),
                                  ('assets/slime/blue/3.png', 0.25)])
animation.play()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill((100, 50, 50))
    animation.blit(windowSurface, (100, 50))
    pygame.display.update()


