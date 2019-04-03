# health based on End
# aether based on Int
# stamina based on End (?)
# Exponential growth based on stats

"""

Formulas

MAX_HP = BASE_HP + (10 + (0.5 * END)) * LEVEL
MAX_AP = BASE_AP + (10 + (0.5 * INT)) * LEVEL


"""
from creature_files.miscellaneous.Activity_Level import Activity_Level


# TODO: resources affected by base stats
#   starving influences Psychology (happiness, stress. sanity)
class Resources:

    def __init__(self, body):

        self.config_health = body.creature.config['HEALTH']
        self.config_aether = body.creature.config['AETHER']
        self.config_stamina = body.creature.config['STAMINA']
        self.body = body

        self.int = body.stats.base['int']
        self.end = body.stats.base['end']
        self.level = body.creature.level

        self.health = self.Health(self.config_health, body)
        self.aether = self.Aether(self.config_aether, body)
        self.stamina = self.Stamina(self.config_stamina, body)

    class Health:

        def __init__(self, config, body):

            self.config = config
            self.body = body
            self.stomach = body.get_body_parts('stomach')[0]

            self.max = int(self.config['max']) + (10 + (0.5 * self.body.stats.base['end'])) * self.body.creature.level
            self.cur = self.max
            self.regen = int(config['regen'])
            self.is_regen = False

        # ----------------------------------------------------------------------------------------------------------------------
        #   Update Functions

        def update_max(self):

            if int(self.config['max']) == 0:
                self.max = 0
            else:
                self.max = int(self.config['max']) + (10 + (0.5 * self.body.stats.base['end'])) * self.body.creature.level

        def update_on_zero_health(self):

            if self.cur <= 0:
                self.body.creature.is_destroyed = True
                self.body.world.creature_container.remove(self.body.creature)

        def update_on_sleep(self):
            # increase current health if is_regen is True, typically if creature is sleeping
            if self.body.resources.stamina.activity_level.name == 'Sleep':
                self.is_regen = True
                if self.is_regen:
                    if self.cur + self.regen >= self.max:
                        self.cur = self.max
                    else:
                        self.cur += self.regen

        def update_on_starving(self):

            if self.stomach.is_starving:
                if self.cur - 1 <= 0:
                    self.cur = 0
                else:
                    self.cur -= 1

        def update(self):

            self.update_max()
            if self.stomach.is_starving:
                self.update_on_starving()
            else:
                self.update_on_sleep()
            self.update_on_zero_health()

        # ----------------------------------------------------------------------------------------------------------------------
        #   Display Functions

        def display_values_full(self):

            self.display_values()
            print("Regen: " + str(self.regen))
            print("Is Regen: " + str(self.is_regen))

        def display_values(self):

            print("Health: " + str(self.cur) + "/" + str(self.max))

    class Aether:

        def __init__(self, config, body):

            self.config = config
            self.body = body
            self.stomach = body.get_body_parts('stomach')[0]

            self.max = int(self.config['max']) + (10 + (0.5 * self.body.stats.base['int'])) * self.body.creature.level
            self.cur = self.max
            if int(self.config['max']) == 0:
                self.cur = 0
            else:
                self.cur = self.max

            self.regen = int(config['regen'])
            self.is_regen = False

        # ----------------------------------------------------------------------------------------------------------------------
        #   Update Functions

        def update_max(self):

            if int(self.config['max']) == 0:
                self.max = 0
            else:
                self.max = int(self.config['max']) + (10 + (0.5 * self.body.stats.base['int'])) * self.body.creature.level

        def update_on_sleep(self):
            # increase current health if is_regen is True, typically if creature is sleeping
            if self.body.resources.stamina.activity_level.name == 'Sleep':
                self.is_regen = True
                if self.is_regen:
                    if self.cur + self.regen >= self.max:
                        self.cur = self.max
                    else:
                        self.cur += self.regen

        def update_on_starving(self):

            if self.stomach.is_starving:
                if self.cur - 1 <= 0:
                    self.cur = 0
                else:
                    self.cur -= 1

        def update(self):

            self.update_max()
            if self.stomach.is_starving:
                self.update_on_starving()
            else:
                self.update_on_sleep()

        # ----------------------------------------------------------------------------------------------------------------------
        #   Display Functions

        def display_values_full(self):

            self.display_values()
            print("Regen: " + str(self.regen))
            print("Is Regen: " + str(self.is_regen))

        def display_values(self):

            print("Aether: " + str(self.cur) + "/" + str(self.max))

    class Stamina:

        def __init__(self, config, body):

            self.config = config
            self.body = body

            self.activity_level = Activity_Level(2)
            self.max = int(config['max'])
            self.cur = self.max

            self.expenditure_base = int(config['exp_base'])               # stamina expenditure level to be used as a
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
        #   Update Functions

        def update_stamina_expenditure_current(self):

            self.expenditure_current = self.expenditure_base * self.expenditure_factor[self.activity_level.value]

        def update_stamina_current(self):

            self.cur = self.cur + self.expenditure_current
            if self.cur >= self.max and self.activity_level == Activity_Level['Sleep']:
                self.activity_level = Activity_Level['Idle']
                self.cur = self.max
            elif self.cur <= 0:
                print(self.activity_level)
                self.activity_level = Activity_Level['Sleep']
                print(self.activity_level)
                self.cur = 0

        def update(self):
            self.update_stamina_current()
            self.update_stamina_expenditure_current()

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

    def display_values(self):
        print("R E S O U R C E S")
        self.health.display_values()
        self.aether.display_values()
        self.stamina.display_values()

    def update(self):
        self.health.update()
        self.aether.update()
        self.stamina.update()


