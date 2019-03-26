# Class for Formless body types
# Slimes, etc
import monsters.miscellaneous.Resources as Resources
from monsters.body_parts.Stomach import Stomach
from monsters.miscellaneous.Base_Stats import Base_Stats
from monsters.behaviour.World_Movement import World_Movement as World_Movement


class Body_Formless:

    def __init__(self, World):

        # Resources
        self.health = Resources.Health(100, 100)
        self.aether = Resources.Aether(150, 150)
        self.stamina = Resources.Stamina(100, 50)

        # Stats
        self.base_stats = Base_Stats(5, 10, 10, 5, 8, 10)

        # Body Parts
        self.stomach = Stomach()

        # Behaviours
        self.world_movement = World_Movement(World, self.stamina)

# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_values(self):

        self.health.display_values()
        self.aether.display_values()
        print("")
        self.stamina.display_values()
        print("")

# ----------------------------------------------------------------------------------------------------------------------
#   Update Functions

    def update(self):
        self.stamina.update()
        self.stomach.update()
        self.world_movement.update()
