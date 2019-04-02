from creature_files.body_types.Body_Formless import Body_Formless as Formless
import configparser


class Template:

    def __init__(self, name, World):

        self.config = configparser.ConfigParser()
        self.config.read('creature_files/creatures_config/formless/' + self.__class__.__name__ + '.ini')
        config_general = self.config['creature']

        self.name = name
        self.race = config_general['race']
        self.description = config_general['description']
        self.age = 1
        self.level = 1
        self.exp = 0

        self.element = None
        self.is_destroyed = True
        self.body = Formless(self, World)

# ----------------------------------------------------------------------------------------------------------------------
#   Display Functions

    def display_values(self):
        print("G E N E R A L")
        print("Name: " + str(self.name))
        print("Race: " + str(self.race))
        print("Description: " + str(self.description))
        print("Age: " + str(round(self.age, 2)))
        print("Level: " + str(self.level))
        print("Exp: " + str(self.exp))
        self.body.display_values()

# changes that will occur every update based on world refresh_rate
# affects stamina expenditure and hunger gain
    def update(self):

        self.age += (1/60)
        self.body.update()

    # returns class name as a string with underscreatures replaced with spaces
    def get_class_name(self):

        class_name = self.__class__.__name__
        class_name_spaces = ""
        for char in class_name:
            if char is '_':
                char = ' '
            class_name_spaces += char
        return class_name_spaces
