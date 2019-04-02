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
import creature_files.miscellaneous.Value as Value


class Body_Formless:

    def __init__(self, creature, world):

        self.config = creature.config[str.upper(self.__class__.__name__)]
        self.creature = creature
        self.world = world

        # Body Parts
        self.body_parts = self.generate_body_parts()

        # Stats
        self.stats = Stats(self)  # body base stats
        self.stats = Stats.combine_stats(self.stats, self.body_parts)   # combine stats from all body parts

        # Resources
        self.resources = Resources(self)

        # Behaviours
        self.world_movement = World_Movement(self, world)
        self.psychology = Psychology()

        # Miscellaneous
        self.value = Value.combine_value(float(self.config['value']), self.body_parts)  # combine weight from all body parts
        self.weight = Weight.combine_weight(float(self.config['weight']), self.body_parts)  # combine weight from all body parts

    # return array of body parts listed in config file
    def generate_body_parts(self):

        create_body_part = self.get_body_part_dict()
        body_parts = []
        for each in self.config['body_parts'].split(':'):
            for part in range(0, int(each[:1])):
                body_parts.append(create_body_part[each[1:]](self))
        return body_parts

    def get_body_part_dict(self):

        dict = {
            'BRAIN': Brain,
            'EYE': Eye,
            'HEART': Heart,
            'LUNG': Lung,
            'STOMACH': Stomach
        }
        return dict

    def get_body_parts(self, body_part_name):

        body_parts = []
        for part in self.body_parts:
            if str.lower(part.type) == str.lower(body_part_name):
                body_parts.append(part)
        return body_parts


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

        print("Value: " + str((round(self.value,2))) + " ¥")
        print("Weight: " + str(self.weight))

    def display_values(self):

        self.display_miscellaneous_values()
        print("")
        print("R E S O U R C E S")
        self.resources.health.display_values()
        self.resources.aether.display_values()
        self.resources.stamina.display_values_full()
        #self.resources.stamina.display_activity_level()
        print("")
        #self.display_body_parts()
        #print("")
        #print("")
        self.get_body_parts('stomach')[0].display_hunger_values_full()
        print("")
        #self.world_movement.display_closest_food()
        #print("")
        #print("")
        #self.stats.display_base_values()
        print("")
        #self.stats.display_explore_values()

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    # TODO: might make more sense to move this to miscellaneous.Weight module
    def update_weight(self):

        self.weight = Weight.combine_weight(float(self.config['weight']), self.body_parts)

    def update_body_parts(self):

        for part in self.body_parts:
            part.update()

    def update(self):

        self.resources.update()
        self.update_body_parts()
        self.world_movement.update()
        self.update_weight()


