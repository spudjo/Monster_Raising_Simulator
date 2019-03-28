# stats are Str, End, Spd and Luk
from monsters.miscellaneous.Stats import Stats


class Lung:

    def __init__(self, race):

        self.type = str(race) + " Lung"
        self.weight = 2
        self.stats = Stats(1, 0, 1, 0, 1, 0)

    def display_values(self):

        print("L U N G")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))
        self.stats.display_values()

    def update(self):

        pass
