class Slime():

    def __init__(self, name):
        self.name = name
        self.race = "Slime"
        self.age = 0
        self.size = 1

        self.health_max = 100
        self.health_cur = 100

        self.hunger_cur = 0
        self.hunger_min = 0

    def display_stats(self):
        print("Name: " + str(self.name))
        print("Race: " + str(self.race))
        print("Age: " + str(self.age))
        print("Size: " + str(self.size))
        print("Health: " + str(self.health_cur))
        print("Hunger: " + str(self.hunger_cur) + "\n")

    def eat(self, food_hunger_value):
        self.hunger_cur = self.hunger_cur - food_hunger_value

    def update(self):
        self.hunger_cur = self.hunger_cur + 1


