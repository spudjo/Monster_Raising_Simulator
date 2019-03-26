# Class for Formless body types
# Slimes, etc
import monsters.miscellaneous.Resources as Resources
from monsters.body_parts.Brain import Brain
from monsters.body_parts.Heart import Heart
from monsters.body_parts.Stomach import Stomach
from monsters.body_parts.Lungs import Lungs
from monsters.miscellaneous.Psychology import Psychology
from monsters.miscellaneous.Stats import Stats
from monsters.behaviour.World_Movement import World_Movement as World_Movement


class Body_Formless:

    def __init__(self, World):
        # Resources
        self.health = Resources.Health(100, 100)
        self.aether = Resources.Aether(150, 150)
        self.stamina = Resources.Stamina(100, 50)

        # Body Parts
        # TODO: Each bodypart should come with their own resources and base stats (partially done)
        #  which will all contribute to the body's overall stats
        self.brain = Brain()
        self.heart = Heart()
        self.stomach = Stomach()
        self.lungs = Lungs()

        # Behaviours
        self.world_movement = World_Movement(World, self.stamina)
        self.psychology = Psychology()

        # Stats
        # add up stats of all individual body parts to get totals
        # TODO: Look into a better way of doing this
        self.base_stats = Stats(1, 1, 1, 1, 1, 1)
        self.base_stats = Stats.add_base_stats(self.base_stats, self.brain, self.heart,self.stomach,self.lungs)

# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_values(self):

        self.health.display_values()
        self.aether.display_values()
        print("")
        self.stamina.display_values()
        print("")
        self.base_stats.display_values()
        print("")
        self.psychology.display_values()
        print("")

# ----------------------------------------------------------------------------------------------------------------------
#   Update Functions

    def update(self):
        self.stamina.update()
        self.stomach.update()
        self.world_movement.update()
