# stats are Dex and Vision
from creature_files.miscellaneous.Stats import Stats


class Eye:

    def __init__(self, body):

        self.config = body.creature.config[str.upper(self.__class__.__name__)]
        self.body = body

        self.name = str(body.creature.race) + " Eye"
        self.type = "Eye"

        self.value = int(self.config['value'])
        self.weight = float(self.config['weight'])

        self.stats = Stats(self)

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    def update(self):

        pass

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_values_full(self):

        self.display_values()
        self.stats.display_values()

    def display_values(self):

        print("E Y E")
        print("Name: " + str(self.name))
        print("Type: " + str(self.type))
        print("Value: " + str(int(self.value)) + " ¥")
        print("Weight: " + str(self.weight))
