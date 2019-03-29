# stats are Str, End, Spd and Luk
from creature_files.miscellaneous.Stats import Stats


class Lung:

    def __init__(self, body):

        self.type = str(body.whole_body.race) + " Lung"
        self.weight = 2
        self.stats = Stats(1, 0, 1, 0, 1, 0,
                           0, 0, 0, 0)

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_values_full(self):

        self.display_values()
        self.stats.display_values()

    def display_values(self):

        print("L U N G")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    def update(self):

        pass
