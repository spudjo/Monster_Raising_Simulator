import random
import Activity_Level
import pygame
import pyganim
import os

class Slime():

    def __init__(self, name, World):
        self.activity_level = Activity_Level.Activity_Level(0)

        self.name = name
        self.race = "Slime"
        self.age = 1
        self.sex = "Male"
        self.weight = 10

        # --------------------------------------------------

        self.health_max = 100
        self.health_cur = 100

        # --------------------------------------------------

        self.energy_max = 100
        self.energy_cur = 100

        self.energy_expenditure_base = 1    # energy expenditure rate of energy loss per second at Idle,
                                            # affected by multiplier based on activity level

        # TODO: adjust energy_expenditure_factor based on endurance stat
        self.energy_expenditure_factor = self.calculate_energy_expenditure_factor()
        self.energy_expenditure = 1

        # --------------------------------------------------

        # eating food will add the object to stomach contents, increasing weight and daily calorie intake
        self.stomach_contents = []
        self.calorie_levels = 1
        self.calorie_requirement = self.calculate_calorie_requirement()

        # --------------------------------------------------

        self.x = World.world_x / 2
        self.y = World.world_y / 2
        self.body = pyganim.PygAnimation([('assets/slime/blue/0.png', 0.25),
                                          ('assets/slime/blue/1.png', 0.25),
                                          ('assets/slime/blue/2.png', 0.25),
                                          ('assets/slime/blue/3.png', 0.25)])
        self.body.play()

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_stats(self):
        print("Name: " + str(self.name))
        print("Race: " + str(self.race))
        print("Age: " + str(round(self.age, 2)))
        print("Sex: " + str(self.sex))
        print("Weight: " + str(self.weight) + " lbs")
        print("Health: " + str(self.health_cur))
        print("Activity Level: " + str(self.activity_level.name))
        print("")
        self.display_energy_stats()
        self.display_calorie_stats()
        self.display_location_stats()

    def display_location_stats(self):
        print("X-Coordinate: " + str(self.x))
        print("X-Coordinate: " + str(self.y))
        print("")

    def display_energy_stats(self):
        print("Energy Level: " + str(self.energy_cur))
        print("Energy Expenditure: " + str(self.energy_expenditure))
        print("")

    def display_calorie_stats(self):
        print("Daily Calorie Requirement: " + str(self.calorie_requirement))
        print("")

# ----------------------------------------------------------------------------------------------------------------------
#   Energy Functions

    def calculate_energy_expenditure_factor(self):
        sleep_factor = 4
        rest_factor = 2
        idle_factor = -1
        light_factor = -1.5
        moderate_factor = -2
        heavy_factor = -4
        return (sleep_factor, rest_factor, idle_factor, light_factor, moderate_factor, heavy_factor)

    def calculate_energy_expenditure(self):
        return self.energy_expenditure_base * self.energy_expenditure_factor[self.activity_level.value]

# ----------------------------------------------------------------------------------------------------------------------
#   Calories Functions

    def calculate_calorie_requirement(self):
        return self.weight * 14

# ----------------------------------------------------------------------------------------------------------------------
#   Update Functions

    def update_energy_cur(self):
        self.energy_expenditure = self.calculate_energy_expenditure()
        new_energy_change = self.energy_cur + self.energy_expenditure
        if new_energy_change >= self.energy_max:
            self.energy_cur = self.energy_max
        elif new_energy_change <= 0:
            self.energy_cur = 0
        else:
            self.energy_cur = new_energy_change


    def update_calorie_tracker(self):
        pass


    # changes that will occur every update based on world refresh_rate
    # affects energy expenditure and hunger gain
    def update(self):
        self.age += (1/60) # increase age
        self.update_energy_cur()


    # TODO: Activity levels affecting hunger levels
    #           0: Sleeping, 1: Idle, 2: Light Activity, 3: Moderate Activity, 4: Heavy Activity
    #       Sleep affecting hunger levels
    #       Calorie System to replace hunger?
    #
    #
    # TODO:
    #       Muscle Mass / Fat, atrophy
    #       Battle Stats
    #       Pathfinding for movement

