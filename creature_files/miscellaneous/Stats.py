"""
    str - influences melee damage, muscle mass?, carry weight?


    int - influences aether resource, aether damage...
        - increase by training brain

    end - influences health resource, stamina, hunger, resistances?
    dex - influences accuracy, chance to hit body parts...
    spd - influences attack speed, movement speed, dodging...
    luk - influences crit attacks, dodging, chance to hit body parts...
"""

# TODO: vision (distance, in dark underwater), swimming speed, climbing speed, etc...
#   resistance to disease, mutation (growing extra limbs?), stress (linked to psychology), bleeding, etc...
# TODO: better way of doing get() methods

import random
import math


class Stats:

    def __init__(self, body):

        self.config = body.config
        self.body = body

        self.base_points = 3
        self.base = self.get_base_stats()

        self.explore = self.get_explore_stats()

        self.resist = self.get_resist_stats()

    def get_base_stats(self):

        base = {
            'str': int(self.config['str']) if ('str' in self.config) else 0,
            'int': int(self.config['int']) if ('int' in self.config) else 0,
            'end': int(self.config['end']) if ('end' in self.config) else 0,
            'dex': int(self.config['dex']) if ('dex' in self.config) else 0,
            'spd': int(self.config['spd']) if ('spd' in self.config) else 0,
            'luk': int(self.config['luk']) if ('luk' in self.config) else 0
        }
        return base

    def get_explore_stats(self):

        explore = {
            'vis': int(self.config['vis']) if ('vis' in self.config) else 0,
            'vis_dark': int(self.config['vis_dark']) if ('vis_dark' in self.config) else 0,
            'swim': int(self.config['swim']) if ('swim' in self.config) else 0,
            'climb': int(self.config['climb']) if ('climb' in self.config) else 0
        }
        return explore

    def get_resist_stats(self):

        resistances = {
            'fire': int(self.config['fire']) if ('fire' in self.config) else 0,
            'water': int(self.config['water']) if ('water' in self.config) else 0,
            'earth': int(self.config['earth']) if ('earth' in self.config) else 0,
            'wind': int(self.config['wind']) if ('wind' in self.config) else 0,
            'wood': int(self.config['wood']) if ('wood' in self.config) else 0,
            'metal': int(self.config['metal']) if ('metal' in self.config) else 0,
            'light': int(self.config['light']) if ('light' in self.config) else 0,
            'dark': int(self.config['dark']) if ('dark' in self.config) else 0,
            'time': int(self.config['time']) if ('time' in self.config) else 0,
            'space': int(self.config['space']) if ('space' in self.config) else 0
        }
        return resistances

    # base_stat is one of the 6 base stats as a string
    def increase_base_stat(self, creature, base_stat):
        if self.base_points >= self.base[base_stat]:
            print(str.capitalize(base_stat) + " Increased!")
            print(str(self.base[base_stat]) + "->" + str(self.base[base_stat] + 1))
            self.base_points -= self.base[base_stat]
            self.base[base_stat] += 1
        else:
            print("Insufficient points!")

    def set_to_zero(self):
        for value in self.base:
            self.base[value] = 0
        # copies explore stats from body
        for value in self.explore:
            self.explore[value] = 0
        # copies resist stats from body
        for value in self.resist:
            self.resist[value] = 0

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    # amount of stat points gained based on current level and luk stat
    # the amount of stat points gain is equal to the creature's current level plus a bonus value, which starts at 2 and increases by 1 every 10 levels
    # there is also a 5% chance that creatures will gain 2x their current level in bonus points
    # this chance increases based on luck/250
    def update_base_stat_points_on_level(self):

        current_level = self.body.creature.exp.level

        # every 10 levels, bonus_increase increases by 1
        amount_of_bonus_increases = math.floor(current_level / 10)

        luk = self.base['luk']  # get creature body's luck
        bonus = 2
        bonus_increase = 1

        for each in range(0, amount_of_bonus_increases):
            bonus += 2 + bonus_increase
            bonus_increase += 1

        stat_gain = current_level    # get creature's level

        # chance for extra bonus points (increase chance based on luck)
        if random.random() > 0.95 - (luk / 250):
            stat_gain += current_level + bonus
        else:
            stat_gain += bonus

        self.base_points += stat_gain
        print("Gained " + str(stat_gain) + " stat points!")

    # adds creature's body stats with the stats from all their individual body parts
    def update_body_stats(self, body_stats, body_parts):

        # copies base stats from body
        for value in body_stats.base:
            self.base[value] = body_stats.base[value]
        # copies explore stats from body
        for value in body_stats.explore:
            self.explore[value] = body_stats.explore[value]
        # copies resist stats from body
        for value in body_stats.resist:
            self.resist[value] = body_stats.resist[value]

        # add stats from body parts
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
