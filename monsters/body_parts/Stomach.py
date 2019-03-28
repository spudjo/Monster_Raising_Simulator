# Food / digestion / excretion system, influenced by Endurance stat (not yet implemented)
# stats are End and Luk
from monsters.miscellaneous.Stats import Stats


class Stomach:

    def __init__(self, race):

        self.type = str(race) + " Stomach"
        self.weight = 3
        self.stats = Stats(0, 0, 2, 0, 0, 1)

        self.is_starving = False
        self.is_hungry = False
        self.hunger_max = 100
        self.hunger_cur = 60
        self.hunger_threshold = 60      # amount of hunger til creature will seek out food
        self.hunger_rate = 1            # hunger gain per tick

        self.contents = []
        self.digestion_rate = 4         # amount of nutrients absorbed from food per tick
        self.digestion_efficiency = 1   # influences the amount of waste material produced per tick (urine / feces)

        self.capacity_max = 1000
        self.capacity_current = 200

        self.guts = .7  # ability to hold bowels?

        self.urine_max = 1
        self.urine_current = 1
        self.fecal_max = 1
        self.fecal_current = 1

    # function to eat food objects, called from World_Movement class on collision with food object when is_hungry equals True
    # food object is added to stomach content, food is_eaten variable is set to True and food's weight is added to stomach weight, which
    # will later be added to overall body weight on update
    def eat(self, food):

        self.contents.append(food)
        food.become_eaten()
        self.weight += food.weight

    # controls digestion of each food objects in stomach content
    def digest_food(self):
        # iterate through each food in stomach.content
        for food in self.contents:
            food_nutrition_cur = food.nutrition      # get food's current nutrition for hunger decrease calculation
            food.nutrition -= self.digestion_rate    # decrease the nutrition points in food by digestion rate
            if food.nutrition < 0:
                food.nutrition = 0  # if digestion rate would bring food nutrition to less than or equal to 0, simply set it to 0

            self.hunger_cur -= food_nutrition_cur - food.nutrition   # decreases food's nutrition loss from hunger
            if food.nutrition == 0:
                self.weight -= food.weight  # when food's nutrition is zero, remove it's weight from stomach, set food to destroyed and remove it
                food.is_destroyed = True    # from stomach contenta as food is fully digested and no longer exists in the stomach
                self.contents.remove(food)

    def defecate(self):

        pass

    def urinate(self):

        pass

# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_values_full(self):

        self.display_values()
        self.display_hunger_values()

    def display_hunger_values(self):

        print("Hunger: " + str(self.hunger_cur) + "/" + str(self.hunger_max))
        print("Is Hungry: " + str(self.is_hungry))
        print("Is Starving: " + str(self.is_starving))
        print("Contents: " + str(self.contents))
        print("Digestion Rate: " + str(self.digestion_rate))

    def display_values(self):

        print("S T O M A C H")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))

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
            self.is_starving = True
        else:
            self.hunger_cur += self.hunger_rate
            self.is_starving = False
        # digest food if any in stomach
        if len(self.contents) > 0:
            self.digest_food()

    def update(self):

        self.update_hunger_cur()
        self.update_is_hungry()

