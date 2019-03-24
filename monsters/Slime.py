import pyganim
from monsters.body_parts.Energy import Energy
from monsters.body_types.Body_Formless import Body_Formless as Formless
from monsters.world_parts.Creature_World_Movement import Creature_World_Movement as Creature_World_Movement


class Slime:

    def __init__(self, name, World):
        self.name = name
        self.race = "Slime"

        self.body = Formless()
        self.energy = Energy()



        self.creature_world_movement = Creature_World_Movement(World, self.body, self.energy)



# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_values(self):
        print("--------------------------------------------------")
        print("Name: " + str(self.name))
        print("Race: " + str(self.race))
        self.body.display_values()
        print("")
        self.energy.display_values()
        print("")
        self.creature_world_movement.display_values()
        print("")



# changes that will occur every update based on world refresh_rate
# affects energy expenditure and hunger gain
    def update(self):
        self.body.update()
        self.energy.update()
        self.creature_world_movement.update()

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

