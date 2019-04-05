# Class for Formless body types
# Slimes, etc
from creature_files.miscellaneous.Resources import Resources
from creature_files.body_parts.Eye import Eye
from creature_files.body_parts.Brain import Brain
from creature_files.body_parts.Heart import Heart
from creature_files.body_parts.Stomach import Stomach
from creature_files.body_parts.Lung import Lung
from creature_files.miscellaneous.Stats import Stats
from creature_files.behaviour.World_Movement import World_Movement as World_Movement
import creature_files.miscellaneous.Weight as Weight
import creature_files.miscellaneous.Value as Value


class Body_Formless:

    def __init__(self, creature, world):

        self.config = creature.config[str.upper(self.__class__.__name__)]
        self.creature = creature
        self.world = world
        self.name = self.creature.race + " Body"
        self.type = "Body"

        # Body Parts
        self.body_parts = self.generate_body_parts()

        # Stats
        self.stats = Stats(self)  # body base stats, these are the stats that can increase by leveling up

        self.stats_full = Stats(self)
        self.stats_full = Stats.update_body_stats(self.stats_full, self.stats, self.body_parts)   # combine stats from all body parts,
                                                                                                  # these increase through training
        # Resources
        self.resources = Resources(self)

        # Behaviours
        self.world_movement = World_Movement(self, world)

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

    # match each string with function to create body part
    @staticmethod
    def get_body_part_dict():

        dict = {
            'BRAIN': Brain,
            'EYE': Eye,
            'HEART': Heart,
            'LUNG': Lung,
            'STOMACH': Stomach
        }
        return dict

    # return an array of all body parts inside creature matching string (e.g. 'brain' or 'stomach')
    def get_body_parts(self, body_part_name):

        body_parts = []
        for part in self.body_parts:
            if str.lower(part.type) == str.lower(body_part_name):
                body_parts.append(part)
        return body_parts

    def remove_body_part(self, part):
        self.body_parts.remove(part)
        print("Part removed!")


    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    # TODO: might make more sense to move this to miscellaneous.Weight module
    def update_weight(self):

        self.weight = Weight.combine_weight(float(self.config['weight']), self.body_parts)

    # calls update function associated with each body part
    def update_body_parts(self):

        for part in self.body_parts:
            part.update()

    # update functions called at each world update
    def update(self):

        self.update_body_parts()
        self.stats_full = Stats.update_body_stats(self.stats_full, self.stats, self.body_parts)
        self.resources.update()

        self.world_movement.update()
        self.update_weight()

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    # displays list of all body parts
    def display_body_parts(self):

        print("Body Parts:")
        for part in self.body_parts:
            print(" " + part.type)

    # display name, type, value and weight of each body part
    def display_body_part_values(self):

        for part in self.body_parts:
            part.display_values()
            print("")

    # displays name, type, value, weight and stats of each body part
    def display_body_part_values_full(self):

        for part in self.body_parts:
            part.display_values_full()
            print("")

    # display creature's full base stats (body + each body part) with body stats in parentheses)
    def display_body_base_stats(self):

        print("B A S E - S T A T S")
        for value in self.stats_full.base:
            print(str.capitalize(value) + ": " + str(self.stats_full.base[value]) + "(" + str(self.stats.base[value]) + ")")

    # display creature's full explore stats (body + each body part) with body stats in parentheses)
    def display_body_explore_stats(self):

        print("E X P L O R E - S T A T S")
        for value in self.stats_full.explore:
            print(str.capitalize(value) + ": " + str(self.stats_full.explore[value]) + "(" + str(self.stats.explore[value]) + ")")

    # display creature's full resist stats (body + each body part) with body stats in parentheses)
    def display_body_resist_stats(self):

        print("R E S I S T A N C E - S T A T S")
        for value in self.stats_full.resist:
            print(str.capitalize(value) + ": " + str(self.stats_full.resist[value]) + "(" + str(self.stats.resist[value]) + ")")

    # display creature's full stats (body + each body part) with body stats in parentheses)
    def display_body_full_stats(self):
        self.display_body_base_stats()
        self.display_body_explore_stats()
        self.display_body_resist_stats()

    # displays value and weight of body
    def display_miscellaneous_values(self):

        print("Value: " + str(int(self.value)) + " ¥")
        print("Weight: " + str(self.weight) + " lbs")

    # display functions called on world update
    def display_values(self):

        self.display_miscellaneous_values()
        print("")
        print("R E S O U R C E S")
        self.resources.health.display_values()
        self.resources.aether.display_values()
        self.resources.stamina.display_values()
        self.resources.stamina.display_activity_level()
        print("")
        self.get_body_parts('stomach')[0].display_hunger_values_full()
        print("")
        self.display_body_base_stats()
        print("Stat Points: " + str(self.stats.base_points))
        print("")


