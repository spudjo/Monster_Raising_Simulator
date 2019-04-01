# Class for Formless body types
# Slimes, etc
from creature_files.miscellaneous.Resources import Resources
from creature_files.body_parts.Eye import Eye
from creature_files.body_parts.Brain import Brain
from creature_files.body_parts.Heart import Heart
from creature_files.body_parts.Stomach import Stomach
from creature_files.body_parts.Lung import Lung
from creature_files.miscellaneous.Psychology import Psychology
from creature_files.miscellaneous.Stats import Stats
from creature_files.behaviour.World_Movement import World_Movement as World_Movement
import creature_files.miscellaneous.Weight as Weight

class Body_Formless:

    def __init__(self, creature, world):

        self.config = creature.config[str.upper(self.__class__.__name__)]
        self.creature = creature
        self.world = world

        # Body Parts
        self.eye_l = Eye(self)
        self.eye_r = Eye(self)
        self.brain = Brain(self)
        self.heart = Heart(self)
        self.stomach = Stomach(self)
        self.lung_l = Lung(self)
        self.lung_r = Lung(self)
        self.body_parts = [self.eye_l,
                           self.eye_r,
                           self.brain,
                           self.heart,
                           self.stomach,
                           self.lung_l,
                           self.lung_r]    # add all body parts into an array
        # Stats
        # add up stats of all individual body parts to get totals
        #  TODO: Look into a better way of doing stats
        self.stats = Stats(self)  # body base stats

        self.stats = Stats.combine_stats(self.stats, self.body_parts)

        self.weight = Weight.calculate_weight(10, self.body_parts)

        # Resources

        self.resources = Resources(self)

        # Behaviours
        self.world_movement = World_Movement(self, world)
        self.psychology = Psychology()

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_body_parts(self):

        print("B O D Y - P A R T S")
        for part in self.body_parts:
            print(" " + part.type)

    def display_body_part_values(self):

        for part in self.body_parts:
            part.display_values()
            print("")

    def display_body_part_values_full(self):

        for part in self.body_parts:
            part.display_values_full()
            print("")

    def display_miscellaneous_values(self):

        print("Weight: " + str(self.weight))

    def display_values(self):

        print("Weight: " + str(self.weight))
        print("")
        self.resources.display_values()
        self.resources.stamina.display_activity_level()
        print("")
        #print("")
        #self.stomach.display_values()
        #self.stomach.display_hunger_values_full()
        #print("")
        #self.world_movement.display_closest_food()
        #print("")
        #print("M I S C E L L A N E O U S")
        #self.display_miscellaneous_values()
        #print("")
        self.stats.display_base_values()
        print("")
        #self.stats.display_explore_values()


    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    # TODO: might make more sense to move this to miscellaneous.Weight module
    def update_weight(self):

        self.weight = Weight.calculate_weight(10, self.body_parts)

    def update_body_parts(self):

        for part in self.body_parts:
            part.update()

    def update(self):

        self.resources.update()
        self.update_body_parts()
        self.world_movement.update()
        self.update_weight()
