# stats are Int, Dex and Luk
from creature_files.miscellaneous.Stats import Stats


class Brain:

    def __init__(self, body):

        self.config = body.creature.config[str.upper(self.__class__.__name__)]

        self.name = str(body.creature.race) + " Brain"
        self.type = "Brain"
        self.weight = 5
        self.stats = Stats(self)

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_values_full(self):

        self.display_values()
        self.stats.display_values()

    def display_values(self):

        print("B R A I N")
        print("Name: " + str(self.name))
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    def update(self):

        pass
