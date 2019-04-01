"""
    str - influences melee damage, muscle mass?, carry weight?
    int - influences aether resource, aether damage...
    end - influences health resource, stamina, hunger, resistances?
    dex - influences accuracy...
    spd - influence attack speed, movement speed, dodging...
    luk - influences crit attacks, dodging...
"""

# TODO: vision (distance, in dark underwater), swimming speed, climbing speed, etc...
#   resistance to disease, mutation (growing extra limbs?), stress (linked to psychology), bleeding, etc...
# TODO: better way of doing get() methods

class Stats:

    def __init__(self, body):

        self.config = body.config

        self.base = self.get_base_stats()
        self.explore = self.get_explore_stats()
        self.resist = self.get_resist_stats(0, 0, 0, 0,
                                            0, 0, 0, 0,
                                            0, 0)


    def get_base_stats(self):
        base = {
            'str': int(self.config['str']),
            'int': int(self.config['int']),
            'end': int(self.config['end']),
            'dex': int(self.config['dex']),
            'spd': int(self.config['spd']),
            'luk': int(self.config['luk'])
        }

        return base

    def get_explore_stats(self):
        explore = {
            'vis': int(self.config['vis']),
            'vis_dark': int(self.config['vis_dark']),
            'swim': int(self.config['swim']),
            'climb': int(self.config['climb'])
        }

        return explore

    @staticmethod
    def get_resist_stats(fire, water, earth, wind,
                             wood, metal, light, dark,
                             time, space):

        resistances = {
            'fire': fire,
            'water': water,
            'earth': earth,
            'wind': wind,
            'wood': wood,
            'metal': metal,
            'light': light,
            'dark': dark,
            'time': time,
            'space': space
        }
        return resistances

    # add all stats together and returns
    # used to calculate creature's overall stats on the individual stats of their body parts
    def combine_stats(self, body_parts):

        for part in body_parts:
            # add all base stats
            for value in part.stats.base:
                self.base[value] += part.stats.base[value]
            # add all explore stats
            for value in part.stats.explore:
                self.explore[value] += part.stats.explore[value]
            # add all resist stats
            for value in part.stats.resist:
                self.resist[value] += part.stats.resist[value]

        return self

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_base_values(self):

        print("B A S E - S T A T S")
        for value in self.base:
            print(str.capitalize(value) + ": " + str(self.base[value]))

    def display_explore_values(self):

        print("E X P L O R E - S T A T S")
        for value in self.explore:
            print(str.capitalize(value) + ": " + str(self.explore[value]))

    def display_resist_values(self):

        print("R E S I S T A N C E - S T A T S")
        for value in self.resist:
            print(str.capitalize(value) + ": " + str(self.resist[value]))

    def display_values(self):

        self.display_base_values()
        print("")
        self.display_explore_values()
        print("")
        self.display_resist_values()
