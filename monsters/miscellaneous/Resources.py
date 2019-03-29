# health based on End
# aether based on Int
# stamina based on End (?)
# Exponential growth based on stats

from monsters.miscellaneous.Activity_Level import Activity_Level


# TODO: resources affected by base stats
#   starving influences Psychology (happiness, stress. sanity)
class Resources:

    def __init__(self, stats):

        #self.health = self.Health(50, 50)
        #self.aether = self.Aether(50, 50)
        #self.stamina = self.Stamina(50, 50)
        pass

    class Health:

        def __init__(self, body, max, cur, regen):

            self.body = body

            self.max = max
            self.cur = cur
            self.regen = regen
            self.is_regen = False

        # ----------------------------------------------------------------------------------------------------------------------
        #   Display Functions

        def display_values_full(self):
            self.display_values()
            print("Regen: " + str(self.regen))
            print("Is Regen: " + str(self.is_regen))

        def display_values(self):

            print("Health: " + str(self.cur) + "/" + str(self.max))

        # ----------------------------------------------------------------------------------------------------------------------
        #   Update Functions

        def update_on_zero_health(self):

            if self.cur <= 0:
                self.body.whole_body.is_destroyed = False
                self.body.world.creature_container.remove(self.body.whole_body)

        def update_on_sleep(self):
            # increase current health if is_regen is True, typically if creature is sleeping
            if self.body.stamina.activity_level.name == 'Sleep':
                self.is_regen = True
                if self.is_regen:
                    if self.cur + self.regen >= self.max:
                        self.cur = self.max
                    else:
                        self.cur += self.regen

        def update_on_starving(self):

            if self.body.stomach.is_starving:
                if self.cur - 1 <= 0:
                    self.cur = 0
                else:
                    self.cur -= 1

        def update(self):
            if self.body.stomach.is_starving:
                self.update_on_starving()
            else:
                self.update_on_sleep()
            self.update_on_zero_health()

    class Aether:

        def __init__(self, body, max, cur, regen):

            self.body = body

            self.max = max
            self.cur = cur
            self.regen = regen
            self.is_regen = False

        # ----------------------------------------------------------------------------------------------------------------------
        #   Display Functions

        def display_values_full(self):
            self.display_values()
            print("Regen: " + str(self.regen))
            print("Is Regen: " + str(self.is_regen))

        def display_values(self):

            print("Aether: " + str(self.cur) + "/" + str(self.max))

        # ----------------------------------------------------------------------------------------------------------------------
        #   Update Functions

        def update_on_sleep(self):
            # increase current health if is_regen is True, typically if creature is sleeping
            if self.body.stamina.activity_level.name == 'Sleep':
                self.is_regen = True
                if self.is_regen:
                    if self.cur + self.regen >= self.max:
                        self.cur = self.max
                    else:
                        self.cur += self.regen

        def update_on_starving(self):

            if self.body.stomach.is_starving:
                if self.cur - 1 <= 0:
                    self.cur = 0
                else:
                    self.cur -= 1

        def update(self):
            if self.body.stomach.is_starving:
                self.update_on_starving()
            else:
                self.update_on_sleep()

    class Stamina:

        def __init__(self, body, max, cur):

            self.body = body

            self.activity_level = Activity_Level(2)
            self.max = max
            self.cur = cur

            self.expenditure_base = 1                                             # stamina expenditure level to be used as a
                                                                                  # base for all energery related calculations
            self.expenditure_factor = self.calculate_stamina_expenditure_factor()  # multiples expenditure base by a factor
                                                                                  # based on Activity level
            self.expenditure_current = 0         # current stamina expenditure per second based on base and factor

        # ----------------------------------------------------------------------------------------------------------------------
        #   Calculation Functions

        @staticmethod
        def calculate_stamina_expenditure_factor():

            sleep_factor = 4
            rest_factor = 1
            idle_factor = -0.2
            light_factor = -0.5
            moderate_factor = -2
            heavy_factor = -5
            return sleep_factor, rest_factor, idle_factor, light_factor, moderate_factor, heavy_factor

        # ----------------------------------------------------------------------------------------------------------------------
        #   Display Functions

        def display_values_full(self):
            self.display_values()
            print("Stamina Base: " + str(self.expenditure_base))
            print("Stamina Factor: " + str(self.expenditure_factor[self.activity_level.value]))
            self.display_activity_level()

        def display_activity_level(self):
            print("Activity Level: " + str(self.activity_level.name))

        def display_values(self):
            print("Stamina: " + str(round(self.cur, 2)) + "/" + str(self.max))
            print("Stamina Expenditure: " + str(self.expenditure_current) + " / second")


        # ----------------------------------------------------------------------------------------------------------------------
        #   Update Functions

        def update_stamina_expenditure_current(self):

            self.expenditure_current = self.expenditure_base * self.expenditure_factor[self.activity_level.value]

        def update_stamina_current(self):

            self.cur = self.cur + self.expenditure_current
            if self.cur >= self.max and self.activity_level == Activity_Level['Sleep']:
                self.activity_level = Activity_Level['Idle']
                self.cur = self.max
            elif self.cur <= 0:
                self.activity_level = Activity_Level['Sleep']
                self.cur = 0

        def update(self):
            self.update_stamina_current()
            self.update_stamina_expenditure_current()


