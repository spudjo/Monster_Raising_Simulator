# Food / digestion / excretion system, influenced by Endurance stat (not yet implemented)
# stats are End and Luk
from creature_files.miscellaneous.Stats import Stats
from miscellaneous.Poop import Poop
from miscellaneous.Urine import Urine
import random


class Stomach:

    def __init__(self, body):

        self.config = body.creature.config[str.upper(self.__class__.__name__)]

        self.body = body
        self.world = body.world  # used for expelling waste!

        self.name = str(body.creature.race) + " Stomach"
        self.type = "Stomach"

        self.value = float(self.config['value'])
        self.weight = float(self.config['weight'])

        self.stats = Stats(self)

        self.contents = []
        self.is_starving = False
        self.is_hungry = False

        self.hunger_max = int(self.config['hunger_max'])
        self.hunger_cur = round((self.hunger_max / 2) * random.uniform(.75, 1.25), 0)
        self.hunger_threshold = int(self.config['hunger_threshold'])      # amount of hunger til creature will seek out food
        self.hunger_rate = int(self.config['hunger_rate'])            # hunger gain per tick
        self.digestion_rate = int(self.config['digestion_rate'])         # amount of nutrients absorbed from food per tick
        self.digestion_efficiency = int(self.config['digestion_efficiency'])   # influences the amount of waste material produced per tick (urine / feces)

        self.urine_max = int(self.config['urine_max'])
        self.urine_cur = round(int(self.urine_max / 2) * random.uniform(.75, 1.25), 0)
        self.fecal_max = int(self.config['fecal_max'])
        self.fecal_cur = round(int(self.fecal_max / 2) * random.uniform(.75, 1.25), 0)

    # function to eat food objects, called from World_Movement class on collision with food object when is_hungry equals True
    # food object is added to stomach content, food is_eaten variable is set to True and food's weight is added to stomach weight, which
    # will later be added to overall body weight on update
    def eat(self, food):

        if food in self.world.food_container:
            self.contents.append(food)
            self.world.food_container.remove(food)
        self.body.world_movement.closest_food = None
        self.weight += food.weight

    # controls digestion of each food objects in stomach content0
    def digest_food(self):
        # iterate through each food in stomach.content
        for food in self.contents:
            food_nutrition_cur = food.nutrition      # get food's current nutrition for hunger decrease calculation
            food.nutrition -= self.digestion_rate    # decrease food's current nutrition food by digestion rate
            if food.nutrition < 0:
                food.nutrition = 0  # if digestion rate would bring food nutrition to less than or equal to 0, simply set it to 0

            nutrition_gain = (food_nutrition_cur - food.nutrition) * (self.digestion_efficiency / 100)
            waste_gain = (food_nutrition_cur - food.nutrition) - nutrition_gain

            if self.hunger_cur - nutrition_gain < 0:
                self.hunger_cur = 0 # simply set current hunger to 0 if nutrition gain would bring it lower than zero, preventing negative hunger
            else:
                self.hunger_cur -= nutrition_gain   # decreases food's nutrition loss from hunger

            self.update_urine(waste_gain)
            self.update_fecal(waste_gain)

            if food.nutrition == 0:
                self.weight -= food.weight  # when food's nutrition is zero, remove it's weight from stomach, set food to destroyed and remove it
                food.is_destroyed = True    # from stomach contenta as food is fully digested and no longer exists in the stomach
                self.contents.remove(food)

    def defecate(self):

        poop = Poop(self.world, round(self.body.world_movement.x_center, 0), round(self.body.world_movement.y_center, 0))
        self.world.waste_container.append(poop)
        self.fecal_cur = 0

    def urinate(self):

        urine = Urine(self.world, round(self.body.world_movement.x_center, 0), round(self.body.world_movement.y_center, 0))
        self.world.waste_container.append(urine)
        self.urine_cur = 0

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    # increase urine levels based on waste_gain from digest_food()
    def update_urine(self, waste_gain):

        if self.urine_cur + waste_gain >= self.urine_max:
            self.urine_cur = self.urine_max
            self.urinate()
        else:
            self.urine_cur += waste_gain

    # increase fecal levels based on waste_gain from digest_food()
    def update_fecal(self, waste_gain):

        if self.fecal_cur + waste_gain >= self.fecal_max:
            self.fecal_cur = self.fecal_max
            self.defecate()
        else:
            self.fecal_cur += waste_gain

    # sets creature to starving if hunger is at max, decreasing their HP
    def update_is_starving(self):

        if self.hunger_cur >= self.hunger_max:
            self.is_starving = True
        else:
            self.is_starving = False

    # set is_hungry to True if current hunger equals or exceeds threshold
    def update_is_hungry(self):

        if self.hunger_cur >= self.hunger_threshold:
            self.is_hungry = True
        else:
            self.is_hungry = False

    # increase current hunger every update tick based on hunger_rate
    def update_hunger_cur(self):

        if self.hunger_cur + self.hunger_rate >= self.hunger_max:
            self.hunger_cur = self.hunger_max
        else:
            self.hunger_cur += self.hunger_rate

    def update(self):

        self.update_hunger_cur()
        self.update_is_hungry()
        self.update_is_starving()
        self.digest_food()

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_values_full(self):

        self.display_values()
        self.display_hunger_values_full
        self.stats.display_values()

    def display_hunger_values_full(self):

        self.display_hunger_values()
        self.display_waste_values()

    def display_waste_values(self):

        print("Urine: " + str(round(self.urine_cur, 0)) + "/" + str(self.urine_max))
        print("Fecal: " + str(round(self.fecal_cur, 0)) + "/" + str(self.fecal_max))

    def display_hunger_values(self):

        print("Hunger: " + str(round(self.hunger_cur, 0)) + "/" + str(self.hunger_max))
        print("Is Hungry: " + str(self.is_hungry))
        print("Is Starving: " + str(self.is_starving))
        print("Contents: " + str(self.contents))
        print("Digestion Rate: " + str(self.digestion_rate))

    def display_values(self):

        print("S T O M A C H")
        print("Name: " + str(self.name))
        print("Type: " + str(self.type))
        print("Value: " + str((round(self.value,2))) + " ¥")
        print("Weight: " + str(self.weight))