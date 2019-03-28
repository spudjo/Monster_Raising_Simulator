# stats are Str, End, Spd and Luk
from monsters.miscellaneous.Stats import Stats


class Heart:

    def __init__(self, race):

        self.type = str(race) + " Heart"
        self.weight = 5
        self.stats = Stats(2, 0, 1, 0, 1, 2)

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_values_full(self):

        self.display_values()
        self.stats.display_values()

    def display_values(self):

        print("H E A R T")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    def update(self):

        pass
