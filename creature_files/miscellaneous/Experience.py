# class for Creature Experience


class Experience:

    def __init__(self, creature):

        self.creature = creature

        self.level = int(1)
        self.exp_cur = 0
        self.exp_req = int(self.update_experience_required())
        self.exp_total = self.exp_cur

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    # update exp_cur and exp_total by exp_gain
    def update_experience_current(self, exp_gain):

        self.exp_cur += exp_gain
        self.exp_total += exp_gain

    # update exp_req based on level from experience_chart.txt
    def update_experience_required(self):

        experience_chart = open('assets/experience_chart.txt', 'r')
        experience_list = experience_chart.readlines()
        if self.level <= 98:
            self.exp_req = int(experience_list[self.level].rstrip())
            return int(experience_list[self.level].rstrip())
        else:
            self.exp_req = 0
            return 0

    # update creature's current level as well as exp_cur on level, then updates exp_req
    # TODO: should prompt user if they would like to spend their stat points at each level up as their luk stat will influence
    #   the chance of gaining bonus stat points on level up
    def update_level(self):

        if self.level < 99:
            while self.exp_cur >= self.exp_req:
                print("Level up: " + str(self.level) + " -> " + str(self.level + 1))
                self.level += 1
                self.exp_cur -= self.exp_req
                self.update_experience_required()
                self.creature.body.stats.update_base_stat_points_on_level()
                #print("Base Points " + str(self.creature.body.stats.base_points))
                if self.level == 99:
                    break

    def update(self):

        self.update_level()

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_values(self):
        print("Level: " + str(self.level))
        print("Experience: " + "{:,}".format(self.exp_cur) + " / " + "{:,}".format(self.exp_req))
        print("Total Exp: " + "{:,}".format(self.exp_total))
