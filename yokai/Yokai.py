'''
Yokai types: Formless, Ethereal, Bipedal, Quadruped
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
        print("Name: " + str(self.name), end="\r")
        print("Race: " + str(self.race), end="\r")
        print("Age: " + str(self.age), end="\r")
        print("Size: " + str(self.size), end="\r")
        print("Health: " + str(self.health), end="\r")
        print("Hunger: " + str(self.hunger), end="\r")
        print("Speed: " + str(self.speed), end="\r")

    def move(self): pass

    def eat(self): pass

    def sleep(self): pass
