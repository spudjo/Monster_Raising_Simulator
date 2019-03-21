import pyganim
from monsters.body_parts.Energy import Energy
from monsters.body_types.Body_Formless import Body_Formless as Formless


class Slime:

    def __init__(self, name, World):
        self.name = name
        self.race = "Slime"

        self.body = Formless()
        self.energy = Energy()

        # --------------------------------------------------
        '''
        # eating food will add the object to stomach contents, increasing weight and daily calorie intake
        self.stomach_contents = []
        self.calorie_levels = 1
        self.calorie_requirement = self.calculate_calorie_requirement()

        # --------------------------------------------------
        '''
        self.x = World.world_x / 2
        self.y = World.world_y / 2

        self.body_idle = pyganim.PygAnimation([('assets/slime/blue/0.png', 250),
                                               ('assets/slime/blue/1.png', 250),
                                               ('assets/slime/blue/2.png', 250),
                                               ('assets/slime/blue/3.png', 250)])

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_stats(self):
        print("--------------------------------------------------")
        print("Name: " + str(self.name))
        print("Race: " + str(self.race))
        self.body.display_body_stats()
        print("")
        self.body.display_resources()
        print("")
        self.energy.display_energy_stats()


    def display_location_stats(self):
        print("X-Coordinate: " + str(self.x))
        print("X-Coordinate: " + str(self.y))
        print("")


# changes that will occur every update based on world refresh_rate
# affects energy expenditure and hunger gain
    def update(self):
        self.body.update()
        self.energy.update()
        #self.stomach.update()


    # TODO: Activity levels affecting hunger levels
    #           0: Sleeping, 1: Idle, 2: Light Activity, 3: Moderate Activity, 4: Heavy Activity
    #       Sleep affecting hunger levels
    #       Calorie System to replace hunger?
    #
    #
    # TODO:
    #       Muscle Mass / Fat, atrophy
    #       Pathfinding for movement

