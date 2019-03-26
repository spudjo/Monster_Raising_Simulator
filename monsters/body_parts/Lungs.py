# stats are Str, End, Spd and Luk
from monsters.miscellaneous.Stats import Stats


class Lungs:

    def __init__(self):

        self.type = "Lungs"
        self.weight = 3
        self.stats = Stats(1, 0, 2, 0, 2, 1)

    def display_values(self):

        print("L U N G S")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))
        self.stats.display_values()

    def update(self):

        pass
