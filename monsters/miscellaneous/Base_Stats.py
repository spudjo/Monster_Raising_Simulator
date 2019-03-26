

class Base_Stats:

    def __init__(self, str, int, end, dex, spd, luk):
        self.base_stat_list = self.get_base_stat_list(str, int, end, dex, spd, luk)

    def get_base_stat_list(self, str, int, end, dex, spd, luk):
        base_stat_list = {
            "Str": str,
            "Int": int,
            "End": end,
            "Dex": dex,
            "Spd": spd,
            "Luk": luk
        }
        return base_stat_list

    def display_values(self):
        print("Str: " + str(self.base_stat_list('Str')))
        print("Int: " + str(self.base_stat_list('Int')))
        print("End: " + str(self.base_stat_list('End')))
        print("Dex: " + str(self.base_stat_list('Dex')))
        print("Spd: " + str(self.base_stat_list('Spd')))
        print("Luk: " + str(self.base_stat_list('Luk')))
