# stats are Dex and Vision
from monsters.miscellaneous.Stats import Stats


class Eye:

    def __init__(self, body):

        self.type = str(body.whole_body.race) + " Eye"
        self.weight = 0.5
        self.stats = Stats(0, 0, 0, 1, 0, 0,
                           100, 50, 0, 0)

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_values_full(self):

        self.display_values()
        self.stats.display_values()

    def display_values(self):

        print("E Y E")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    def update(self):

        pass
