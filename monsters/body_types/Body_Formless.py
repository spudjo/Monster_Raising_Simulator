# Class for Formless body types
# Slimes, etc

class Body_Formless:

    def __init__(self):

    # --------------------------------------------------
    #   Info
        self.type = "Formless"
        self.age = 1
        self.weight = 10

    # --------------------------------------------------
    #   Resources

        self.health_max = 100
        self.health_current = 100

        self.aether_max = 100
        self.aether_current = 100

    # --------------------------------------------------
    #   Battle Stats

        self.strength_real = 1
        self.strength_current = 1

        self.intelligence_real = 1
        self.intelligence_current = 1

        self.endurance_real = 1
        self.endurance_current = 1

        self.dexterity_real = 1
        self.dexterity_current = 1

        self.speed_real = 10
        self.speed_current = 10

        self.luck_real = 1
        self.luck_current = 1

# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_body_stats(self):

        print("Type: " + str(self.type))
        print("Age: " + str(round(self.age, 2)))
        print("Weight: " + str(self.weight))

    def display_resources(self):

        print("Health: " + str(self.health_current) + "/" + str(self.health_max))
        print("Aether: " + str(self.aether_current) + "/" + str(self.aether_max))

    def display_battle_stats(self):

        print("Strength: " + str(self.strength_current) + "(" + str(self.strength_real) + ")")
        print("Intelligence: " + str(self.intelligence_current) + "(" + str(self.intelligence_real) + ")")
        print("Endurance: " + str(self.endurance_current) + "(" + str(self.endurance_real) + ")")
        print("Dexterity: " + str(self.dexterity_current) + "(" + str(self.dexterity_real) + ")")
        print("Speed: " + str(self.speed_current) + "(" + str(self.speed_real) + ")")
        print("Luck: " + str(self.luck_current) + "(" + str(self.luck_real) + ")")

    def display_full_body_stats(self):
        self.display_body_stats()
        self.display_resources()
        self.display_battle_stats()

# ----------------------------------------------------------------------------------------------------------------------
#   Update Functions

    def update(self):
        self.age += (1 / 60)  # increase age