# stats are Str, End, Spd and Luk
from monsters.miscellaneous.Stats import Stats


class Heart:

    def __init__(self):

        self.type = "Heart"
        self.weight = 5
        self.stats = Stats(2, 0, 1, 0, 1, 2)

    def display_values(self):

        print("H E A R T")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))
        self.stats.display_values()

    def update(self):

        pass
