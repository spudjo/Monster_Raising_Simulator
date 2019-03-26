# stats are Int, Dex and Luk
from monsters.miscellaneous.Stats import Stats


class Brain:

    def __init__(self):

        self.type = "Brain"
        self.weight = 5
        self.stats = Stats(0, 7, 0, 3, 0, 2)

    def display_values(self):

        print("B R A I N")
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))
        self.stats.display_values()

    def update(self):

        pass
