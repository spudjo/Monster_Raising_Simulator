'''
    str - influences physical damage...
    int - influences aether resource, aether damage...
    end - influences health resource, stamina, hunger...
    dex - influences accuracy,
    spd - influence attack speed, movement speed, dodging...
    luk - influences crit attacks,
'''

class Stats:

    def __init__(self, str, int, end, dex, spd, luk):

        self.base = self.get_base_stats(str, int, end, dex, spd, luk)

        #TODO: vision, resistances

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

    # add stats from different body_parts into a single object and returns
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
