# Class for Formless body types
# Slimes, etc
from monsters.miscellaneous.Resources import Resources
from monsters.body_parts.Brain import Brain
from monsters.body_parts.Heart import Heart
from monsters.body_parts.Stomach import Stomach
from monsters.body_parts.Lungs import Lungs
from monsters.miscellaneous.Psychology import Psychology
from monsters.miscellaneous.Stats import Stats
from monsters.behaviour.World_Movement import World_Movement as World_Movement
import monsters.miscellaneous.Weight as Weight


class Body_Formless:

    def __init__(self, World):
        # Body Parts
        # TODO: Each bodypart should come with their own resources and base stats (partially done)
        #  which will all contribute to the body's overall stats
        self.brain = Brain()
        self.heart = Heart()
        self.stomach = Stomach()
        self.lungs = Lungs()
        self.body_parts = [self.brain, self.heart, self.stomach, self.lungs]    # add all body parts into an array

        # Stats
        # add up stats of all individual body parts to get totals
        # TODO: Look into a better way of doing stats
        self.stats = Stats(1, 1, 1, 1, 1, 1)  # body base stats
        self.stats = Stats.add_base(self.stats, self.body_parts)
        self.weight = Weight.calculate_weight(10, self.body_parts)

        # Resources
        self.health = Resources.Health(100, 100)
        self.aether = Resources.Aether(150, 150)
        self.stamina = Resources.Stamina(100, 50)

        # Behaviours
        # TODO: should be passing self into world_movement, not self.stamina
        self.world_movement = World_Movement(World, self.stamina)
        self.psychology = Psychology()


# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_body_part_values(self):
        for part in self.body_parts:
            part.display_values()
            print("")

    def display_values(self):
        print("R E S O U R C E S")
        self.health.display_values()
        self.aether.display_values()
        self.stamina.display_values()
        print("")
        self.stats.display_values()
        print("")
        self.psychology.display_values()
        print("")
        print("M I S C E L L A N E O U S")
        print("Weight: " + str(self.weight))
        print("")

# ----------------------------------------------------------------------------------------------------------------------
#   Update Functions

    def update(self):
        self.stamina.update()
        self.stomach.update()
        self.world_movement.update()
