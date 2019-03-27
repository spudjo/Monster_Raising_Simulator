# Food / digestion / excretion system, influenced by Endurance stat (not yet implemented)
# stats are End and Luk
from monsters.miscellaneous.Stats import Stats


class Stomach:

    def __init__(self):

        self.type = "Stomach"
        self.weight = 3
        self.stats = Stats(0, 0, 2, 0, 0, 1)

        self.is_hungry = False
        self.hunger_max = 100
        self.hunger_cur = 80
        self.hunger_threshold = 60      # amount of hunger til creature will seek out food
        self.hunger_rate = 1            # hunger gain per tick

        self.contents = []
        self.digestion_rate = 2         # amount of nutrients absorbed from food per tick
        self.digestion_efficiency = 1   # influences the amount of waste material produced per tick (urine / feces)
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
        self.weight += food.weight


    def digest_food(self):
        for food in self.contents:
            food.nutrition -= self.digestion_rate
            self.hunger_cur += self.digestion_rate
            if food.nutrition == 0:
                self.weight -= food.weight
                self.is_destroyed = True


    def defecate(self):

        pass

    def urinate(self):

        pass

# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_hunger_values(self):
        print("Hunger: " + str(self.hunger_cur) + "/" + str(self.hunger_max))
        print("Is Hungry: " + str(self.is_hungry))
        print("Contents: " + str(self.contents))
        print("Digestion Rate: " + str(self.digestion_rate))

    def display_values(self):

        print("S T O M A C H")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))
        #self.stats.display_values()
        self.display_hunger_values()

# ----------------------------------------------------------------------------------------------------------------------
#   Update Functions

    def update_is_hungry(self):
        if self.hunger_cur >= self.hunger_threshold:
            self.is_hungry = True
        else:
            self.is_hungry = False

    def update_hunger_cur(self):
        if self.hunger_cur >= self.hunger_max:
            self.hunger_cur = self.hunger_max
        else:
            self.hunger_cur += self.hunger_rate
        # digest food if any in stomach
        if len(self.contents) > 0:
            self.digest_food()


    def update(self):
        self.update_hunger_cur()
        self.update_is_hungry()

