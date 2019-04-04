# Creature's psychological state
# Currently has no functioning


class Psychology:

    def __init__(self, brain):

        self.config = brain.body.creature.config[str.upper(self.__class__.__name__)]

        self.happiness = int(self.config['happiness'])
        self.stress = int(self.config['stress'])
        self.sanity = int(self.config['sanity'])
        self.loyalty = int(self.config['loyalty'])

        # personality traits based on the big five personality traits, OCEAN
        # works on a scale from 1-100, 100 being highest
        self.o = int(self.config['openness'])  # Openness
        self.c = int(self.config['conscientiousness'])  # Conscientiousness
        self.e = int(self.config['extraversion'])  # Extraversion
        self.a = int(self.config['agreeableness'])  # Agreeableness
        self.n = int(self.config['neuroticism'])  # Neuroticism

    # ----------------------------------------------------------------------------------------------------------------------
    #   Update Functions

    def update(self):

        pass

    # ----------------------------------------------------------------------------------------------------------------------
    #   Display Functions

    def display_values(self):

        print("P S Y C H O L O G Y")
        print("Happiness: " + str(self.happiness))
        print("Stress: " + str(self.stress))
        print("Sanity: " + str(self.sanity))
        print("Loyalty: " + str(self.loyalty))

    def display_personality_values(self):

        print("P E R S O N A L I T Y")
        print("O: " + str(self.o))
        print("C: " + str(self.c))
        print("E: " + str(self.e))
        print("A: " + str(self.a))
        print("N: " + str(self.n))

    def display_values_full(self):

        self.display_values()
        self.display_personality_values()
