import random


def stat_points_gain_calculator():

    luk = 0
    total = 0
    bonus = 2
    bonus_increase = 1

    for level in range(0, 151):
        if level % 10 == 0 and level is not 0:
            bonus += 2 + bonus_increase
            bonus_increase += 1

        stat_gain = level
        if random.random() > 0.95 - (luk / 250):
            stat_gain = level + level + bonus
        else:
            stat_gain = level + bonus

        print('Level ' + str(level) + ": " + str(stat_gain) + " (" + str(level) + "+" + str(bonus) + ")")
        total += stat_gain
    print(total)



def sigma(number):
    total = 0
    for each in range(1, number+1):
        total += each
    print(total)
    return total

def total_sigma(*args):
    total = 0
    for each in args:
        total += sigma(each)
    print(total)


stat_points_gain_calculator()
print("-----")
total_sigma(50,50,50,50,50,50)
print("-----")
total_sigma(115,60,85,60,90,60)





