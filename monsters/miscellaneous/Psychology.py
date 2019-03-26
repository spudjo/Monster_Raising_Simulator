# Creature's psychological state
# Currently has no functioning

class Psychology:

    def __init__(self):

        self.happiness = 50

        # personality traits based on the big five personality traits, OCEAN
        # works on a scale from 1-100, 100 being highest
        self.o = 50  # Openness
        self.c = 50  # Conscientiousness
        self.e = 50  # Extraversion
        self.a = 50  # Agreeableness
        self.n = 50  # Neuroticism

    def display_values(self):
        print("PSYCHOLOGY")
        print("O: " + str(self.o))
        print("C: " + str(self.o))
        print("E: " + str(self.o))
        print("A: " + str(self.o))
        print("N: " + str(self.o))
