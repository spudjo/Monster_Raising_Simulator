# monster location for interaction with World
import random


class Location:

    def __init__(self, World, speed_current, body_idle):

        self.x = World.world_x / 2
        self.y = World.world_y / 2
        #self.hitbox_w = hitbox_w
        #self.hitbox_h = hitbox_h
        self.World = World
        self.speed_current_x = speed_current
        self.speed_current_y = speed_current
        self.body_idle = body_idle

        if random.uniform(0, 1) > .5:
            self.speed_current_x *= -1

        if random.uniform(0, 1) > .5:
            self.speed_current_y *= -1

    def wander(self):

        x_threshold = random.uniform(0, 1)
        y_threshold = random.uniform(0, 1)

        if x_threshold > random.uniform(0, 1):
            if (random.uniform(0, 1)) > .8:
                x_new = self.x + (-self.speed_current_x * random.uniform(0.5, 1))
            else:
                x_new = self.x + (self.speed_current_x * random.uniform(0.5, 1))

            if self.x >= self.World.world_x - 100 or self.x <= 50:
                self.speed_current_x = -self.speed_current_x
                x_new = self.x + self.speed_current_x

            self.x = x_new

        if y_threshold > random.uniform(0, 1):
            if (random.uniform(0, 1)) > .8:
                y_new = self.y + (-self.speed_current_y * random.uniform(0.5, 1))
            else:
                y_new = self.y + (self.speed_current_y * random.uniform(0.5, 1))

            if self.y >= self.World.world_y - 100 or self.y <= 50:
                self.speed_current_y = -self.speed_current_y
                y_new = self.y + self.speed_current_y

            self.y = y_new

        self.body_idle.blit(self.World.surface, (self.x, self.y))



    def display_location(self):
        print("X-Coord: " + str(self.x))
        print("Y-Coord: " + str(self.y))
