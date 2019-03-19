from yokai import Yokai

class Slime(Yokai.Yokai):

    def __init__(self, name, x, y):
        super(Slime, self).__init__()
        self.name = name
        self.race = "Slime"
        self.age = 0
        self.size = 1
        self.health = 100
        self.hunger = 100
        self.speed = 5


        print("Slime Generated")

    '''
    def get_assets(self):
        assets_directory = os.listdir("assets/slime/blue")
        assets = []
        for each in assets_directory:
            assets.append("assets/slime/blue/" + each)
        return assets

    def move(self, x_translate, y_translate):
        self.x += x_translate
        self.y += y_translate
        return self.x, self.y
    '''