import random
import math


# amount of stat points gained per level up based on range and luk stat
def stat_points_gain_range_calculator(starting_level, ending_level, luck):

    luk = luck
    total = 0
    bonus = 2
    bonus_increase = 1

    for level in range(starting_level, ending_level + 1):
        if level % 10 == 0 and level is not 0:
            bonus += 2 + bonus_increase
            bonus_increase += 1

        # chance for extra bonus points (increase chance based on luck)
        stat_gain = level
        if random.random() > 0.95 - (luk / 250):
            stat_gain += level + bonus
        else:
            stat_gain += bonus

        print('Level ' + str(level) + ": " + str(stat_gain) + " pts (" + str(level) + "+" + str(bonus) + " bonus)")
        total += stat_gain
    print(total)


# amount of stat points gained based on current level and luk stat
def stats_points_gain_calculator(current_level, luk):
    amount_of_bonus_increases = math.floor(current_level / 10)

    luk = luk
    bonus = 2
    bonus_increase = 1

    for each in range(0, amount_of_bonus_increases):
        bonus += 2 + bonus_increase
        bonus_increase += 1

    stat_gain = current_level

    # chance for extra bonus points (increase chance based on luck)
    if random.random() > 0.95 - (luk / 250):
        stat_gain += current_level + bonus
    else:
        stat_gain += bonus

    print('Level ' + str(current_level) + ": " + str(stat_gain) + " pts (" + str(current_level) + "+" + str(bonus) + " bonus)")


# amount of points required for any stat value
# the cost to increase any given stat is equivalent to the stat's current value: Increasing Strength from 10 to 11 costs 10 points
def cost_of_stat(number):
    total = 0
    for each in range(1, number+1):
        total += each
    #print(total)
    return total


# amount of points required for multiple stat values
def cost_of_all_stats(*args):
    total = 0
    for each in args:
        print(each)
        total += cost_of_stat(each)
    print(total)


stat_points_gain_range_calculator(0, 150, 0)