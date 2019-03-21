# 妖怪牧場
import pygame, sys
from monsters.Slime import Slime
from food.Berry import Berry
from Activity_Level import Activity_Level


class World:

    def __init__(self):
        pygame.init()  # initiate pygame
        self.FPS = 60
        self.food_container = []
        self.world_x = 800
        self.world_y = 600
        self.surface = pygame.display.set_mode((self.world_x, self.world_y))  # pygame.Surface object for the window
        self.surface_color = (245, 245, 220)
        self.surface.fill(self.surface_color)
        pygame.display.set_caption('Yōkai Ranch')


World = World()
slime = Slime('Monokai', World)
slime.body_idle.play()

update_counter = 0
day_tracker = 0

while True:  # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_f:
                if len(World.food_container) < 5:
                    berry = Berry(World.surface)
                    World.food_container.append(World.food_container)

            if event.key == pygame.K_a:
                if slime.energy.activity_level.name == "Sleep":
                    slime.energy.activity_level = Activity_Level['Rest']
                    slime.body_idle.pause()
                elif slime.energy.activity_level.name == "Rest":
                    slime.energy.activity_level = Activity_Level['Idle']
                elif slime.energy.activity_level.name == "Idle":
                    slime.energy.activity_level = Activity_Level['Light']
                    slime.body_idle.play()
                elif slime.energy.activity_level.name == "Light":
                    slime.energy.activity_level = Activity_Level['Moderate']
                elif slime.energy.activity_level.name == "Moderate":
                    slime.energy.activity_level = Activity_Level['Heavy']
                elif slime.energy.activity_level.name == "Heavy":
                    slime.energy.activity_level = Activity_Level['Sleep']

    update_counter += 1
    if update_counter == World.FPS:
        slime.update()
        slime.display_stats()
        update_counter = 0

    slime.body_idle.blit(World.surface, (slime.x, slime.y))
    pygame.display.update()
    pygame.time.Clock().tick(World.FPS)
