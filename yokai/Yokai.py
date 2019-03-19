'''
Yokai types: Formless, Bipedal, Quadruped
Formless Yokai:
    Ghost -> Phantom -> Apparition ->
'''


class Yokai(object):

    def __init__(self):
        self.name = None
        self.race = None
        self.age = None
        self.size = None
        self.health = None
        self.hunger = None
        self.speed = None
        print("Yokai Generated")

    def display_stats(self):
        print("Name: " + str(self.name))
        print("Race: " + str(self.race))
        print("Age: " + str(self.age))
        print("Size: " + str(self.size))
        print("Health: " + str(self.health))
        print("Hunger: " + str(self.hunger))
        print("Speed: " + str(self.speed))

    def move(self): pass

    def eat(self): pass

    def sleep(self): pass
