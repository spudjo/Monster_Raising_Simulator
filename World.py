from yokai import *
from yokai.Slime import Slime
import time

def main():

    world_width = 800
    world_height = 600

    refresh_rate = 1
    slime = Slime("Monokai")

    while True:

        slime.update()
        slime.display_stats()
        time.sleep(refresh_rate)


if __name__ == '__main__':
    main()