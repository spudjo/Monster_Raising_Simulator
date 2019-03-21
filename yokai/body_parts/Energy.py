# Yokai energy system, based on Endurance stat (not yet implemented)

from Activity_Level import Activity_Level


class Energy(object):

    def __init__(self):

        self.activity_level = Activity_Level(2)
        self.max = 100
        self.current = 50

        self.expenditure_base = 1                                             # energy expenditure level to be used as a
                                                                              # base for all energery related calculations
        self.expenditure_factor = self.calculate_energy_expenditure_factor()  # multiples expenditure base by a factor
                                                                              # based on Activity level
        self.expenditure_current = 0         # current energy expenditure per second based on base and factor

# ----------------------------------------------------------------------------------------------------------------------
#   Calculation Functions

    @staticmethod
    def calculate_energy_expenditure_factor():

        sleep_factor = 4
        rest_factor = 2
        idle_factor = -0.5
        light_factor = -1
        moderate_factor = -2
        heavy_factor = -4
        return sleep_factor, rest_factor, idle_factor, light_factor, moderate_factor, heavy_factor

# ----------------------------------------------------------------------------------------------------------------------
#   Update Functions

    def update_energy_expenditure_current(self):

        self.expenditure_current = self.expenditure_base * self.expenditure_factor[self.activity_level.value]

    def update_energy_current(self):

        self.current = self.current + self.expenditure_current
        if self.current >= self.max:
            self.activity_level = Activity_Level['Idle']
            self.current = self.max
        elif self.current <= 0:
            self.activity_level = Activity_Level['Sleep']
            self.current = 0

    def update(self):

        self.update_energy_current()
        self.update_energy_expenditure_current()

# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_energy_stats(self):

        print("Activity Level: " + str(self.activity_level.name))
        print("Energy Level: " + str(self.current) + "/" + str(self.max))
        print("Energy Expenditure: " + str(self.expenditure_current) + " / second")
        print("Energy Base: " + str(self.expenditure_base))
        print("Energy Factor: " + str(self.expenditure_factor[self.activity_level.value]))
        print("")
