# Food / digestion / excretion system, influenced by Endurance stat (not yet implemented)
# stats are End and Luk
from monsters.miscellaneous.Stats import Stats


class Stomach:

    def __init__(self):

        self.type = "Stomach"
        self.weight = 3
        self.stats = Stats(0, 0, 2, 0, 0, 1)

        self.hunger_max = 100
        self.hunger_current = 50
        self.hunter_rate = 1    # hunger gain per tick

        self.contents = []
        self.digestion_rate = 1     # amount of nutrients absorbed from food per tick
        self.digestion_efficiency = 1  # influences the amount of waste material produced per tick (urine / feces)
        self.capacity_max = 1000
        self.capacity_current = 200

        #
        self.guts = .7

        self.urine_max = 1
        self.urine_current = 1
        self.fecal_max = 1
        self.fecal_current = 1

    def eat(self, food):

        self.contents.append(food)

    def digest_food(self):

        pass

    def defecate(self):

        pass

    def urinate(self):

        pass

    def display_values(self):

        print("S T O M A C H")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))
        self.stats.display_values()

    def update(self):

        pass
