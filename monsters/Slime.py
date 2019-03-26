from monsters.body_types.Body_Formless import Body_Formless as Formless

class Slime:

    def __init__(self, name, World):
        self.name = name
        self.race = 'Slime'
        self.age = 1

        self.element = None
        self.body = Formless(World)

# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_values(self):
        print("Name: " + str(self.name))
        print("Race: " + str(self.race))
        print("Age: " + str(round(self.age, 2)))
        print("")
        self.body.display_values()

# changes that will occur every update based on world refresh_rate
# affects stamina expenditure and hunger gain
    def update(self):
        self.age += (1/60)
        self.body.update()
