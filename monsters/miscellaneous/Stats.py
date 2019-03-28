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
class Stats:

    def __init__(self, str, int, end, dex, spd, luk):

        self.base = self.get_base_stats(str, int, end, dex, spd, luk)
        self.element_resistances = self.get_resistance_stats(50, 50, 50, 50, 50, 50, 50, 50, 50, 50)
        self.vision = 250

    @staticmethod
    def get_base_stats(str, int, end, dex, spd, luk):

        base = {
            'str': str,
            'int': int,
            'end': end,
            'dex': dex,
            'spd': spd,
            'luk': luk
        }
        return base

    @staticmethod
    def get_resistance_stats(fire, water, earth, wind, wood, metal, light, dark, time, space):

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

    # add multiple Stats.base values together and return
    # used to calculate creature's overall stats based on the individual stats of their body parts
    def add_base_stats(self, body_parts):

        for part in body_parts:
            self.base['str'] += part.stats.base.get('str')
            self.base['int'] += part.stats.base.get('int')
            self.base['end'] += part.stats.base.get('end')
            self.base['dex'] += part.stats.base.get('dex')
            self.base['spd'] += part.stats.base.get('spd')
            self.base['luk'] += part.stats.base.get('luk')
        return self

    def display_values(self):

        print("B A S E - S T A T S")
        print("Str: " + str(self.base.get('str')))
        print("Int: " + str(self.base.get('int')))
        print("End: " + str(self.base.get('end')))
        print("Dex: " + str(self.base.get('dex')))
        print("Spd: " + str(self.base.get('spd')))
        print("Luk: " + str(self.base.get('luk')))
