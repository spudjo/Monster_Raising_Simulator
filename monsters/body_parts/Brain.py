# stats are Int, Dex and Luk

from monsters.miscellaneous.Stats import Stats

class Brain:
    def __init__(self):
        self.type = "Brain"
        self.weight = 5
        self.base_stats = Stats(0, 6, 0, 3, 0, 2)

    def display_values(self):
        print("Type: " + str(self.type))
        print("Weight: " + str(self.weight))
        print("Base Stats: " + str(self.base_stats))

    def update(self):
        pass



