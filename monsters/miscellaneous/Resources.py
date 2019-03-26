from monsters.miscellaneous.Activity_Level import Activity_Level

class Resources:

    def __init__(self, stats):

        self.health = self.Health(50, 50)
        self.aether = self.Aether(50, 50)
        self.stamina = self.Stamina(50, 50)

    # Hit Points
    class Health:

        def __init__(self, max, cur):

            self.max = max
            self.cur = cur

        def display_values(self):

            print("Health: " + str(self.cur) + "/" + str(self.max))

    # Mana Points
    class Aether:

        def __init__(self, max, cur):

            self.max = max
            self.cur = cur

        def display_values(self):

            print("Aether: " + str(self.cur) + "/" + str(self.max))

    # Stamina Points
    class Stamina:

        def __init__(self, max, cur):

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
    #   Update Functions

        def update_stamina_expenditure_current(self):

            self.expenditure_current = self.expenditure_base * self.expenditure_factor[self.activity_level.value]

        def update_stamina_current(self):

            self.cur = self.cur + self.expenditure_current
            if self.cur >= self.max:
                self.activity_level = Activity_Level['Idle']
                self.cur = self.max
            elif self.cur <= 0:
                self.activity_level = Activity_Level['Sleep']
                self.cur = 0

        def update(self):

            self.update_stamina_current()
            self.update_stamina_expenditure_current()

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

        def display_values(self):

            print("Stamina: " + str(round(self.cur, 2)) + "/" + str(self.max))
            print("Stamina Expenditure: " + str(self.expenditure_current) + " / second")
            print("Stamina Base: " + str(self.expenditure_base))
            print("Stamina Factor: " + str(self.expenditure_factor[self.activity_level.value]))
            print("Activity Level: " + str(self.activity_level.name))


