# stats are Str, End, Spd and Luk
from creature_files.miscellaneous.Stats import Stats
from creature_files.miscellaneous.Resources import Resources


class Heart:

    def __init__(self, body):

        self.config = body.creature.config[str.upper(self.__class__.__name__)]
        self.body = body

        self.name = str(body.creature.race) + " Heart"
        self.type = "Heart"

        self.value = int(self.config['value'])
        self.weight = float(self.config['weight'])

        self.health = Resources.Part_Health(self.config, self)
        self.stats = Stats(self)

        # body part's health reduced to zero, settings it's stats to 1
        self.is_crippled = False

        # body part completely destroyed, removed from body
        self.is_destroyed = False

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    def update_on_zero_health(self):

        if self.health.cur <= 0:
            self.is_crippled = True

    def update_on_crippled(self):

        if self.is_crippled:
            self.stats.set_to_zero()

    def update_on_destroyed(self):

        if self.is_destroyed:
            self.body.remove_body_part(self)

    def update(self):

        self.update_on_zero_health()
        self.update_on_crippled()
        self.update_on_destroyed()

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_status_values(self):

        print("Is Crippled: " + str(self.is_crippled))
        print("Is Destroyed: " + str(self.is_destroyed))

    def display_values_full(self):

        self.display_values()
        self.display_status_values()
        self.stats.display_values()

    def display_values(self):

        print("H E A R T")
        print("Name: " + str(self.name))
        print("Type: " + str(self.type))
        self.health.display_values()
        print("Value: " + str(int(self.value)) + " ¥")
        print("Weight: " + str(self.weight))
