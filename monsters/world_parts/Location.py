# monster location for interaction with World

class Location:

    def __init__(self, x, y, hitbox_w, hitbox_h, speed):

        self.x = x
        self.y = y
        self.hitbox_w = hitbox_w
        self.hitbox_h = hitbox_h

    def wander(self, world_x, world_y):
        pass