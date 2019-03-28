# stats are Dex and Vision (not yet implemented)
from monsters.miscellaneous.Stats import Stats


class Eye:

    def __init__(self, race):

        self.type = str(race) + " Eye"
        self.weight = 0.5
        self.stats = Stats(0, 0, 0, 1, 0, 0)

    def display_values(self):

        print("E Y E")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))
        self.stats.display_values()

    def update(self):

        pass
