# Food / digestion / excretion system, influenced by Endurance stat (not yet implemented)


class Stomach:

    def __init__(self):

        self.hunger_max = 100
        self.hunger_current = 50

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

    def update(self):
        pass
