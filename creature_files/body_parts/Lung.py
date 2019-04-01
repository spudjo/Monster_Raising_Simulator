# stats are Str, End, Spd and Luk
from creature_files.miscellaneous.Stats import Stats


class Lung:

    def __init__(self, body):

        self.config = body.creature.config[str.upper(self.__class__.__name__)]

        self.name = str(body.creature.race) + " Lung"
        self.type = "Lung"
        self.weight = 2
        self.stats = Stats(self)

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_values_full(self):

        self.display_values()
        self.stats.display_values()

    def display_values(self):

        print("L U N G")
        print("Name: " + str(self.name))
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    def update(self):

        pass
