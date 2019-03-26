

class Stats:

    def __init__(self, str, int, end, dex, spd, luk):

        self.base_stats_list = self.get_base_stats_list(str, int, end, dex, spd, luk)

    @staticmethod
    def get_base_stats_list(str, int, end, dex, spd, luk):

        base_stats_list = {
            "Str": str,
            "Int": int,
            "End": end,
            "Dex": dex,
            "Spd": spd,
            "Luk": luk
        }
        return base_stats_list

    def add_base_stats(self, *argv):
        for arg in argv:
            self.base_stats_list['Str'] += arg.base_stats.base_stats_list.get("Str")
            self.base_stats_list['Int'] += arg.base_stats.base_stats_list.get("Int")
            self.base_stats_list['End'] += arg.base_stats.base_stats_list.get("End")
            self.base_stats_list['Dex'] += arg.base_stats.base_stats_list.get("Dex")
            self.base_stats_list['Spd'] += arg.base_stats.base_stats_list.get("Spd")
            self.base_stats_list['Luk'] += arg.base_stats.base_stats_list.get("Luk")
        return self

    def display_values(self):
        print("BASE STATS")
        print("Str: " + str(self.base_stats_list.get('Str')))
        print("Int: " + str(self.base_stats_list.get('Int')))
        print("End: " + str(self.base_stats_list.get('End')))
        print("Dex: " + str(self.base_stats_list.get('Dex')))
        print("Spd: " + str(self.base_stats_list.get('Spd')))
        print("Luk: " + str(self.base_stats_list.get('Luk')))
