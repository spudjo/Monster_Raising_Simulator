# Monster_Raising_Simulator

A monster raising simulator taking inspiration from games like Monster Rancher and Dwarf Fortress.
Currently working on slime creatures as a base for creature functions.

### Requirements

    To run you must install python modules Pygame, Pyganim
    Run World.py to begin

### Controls:

    1: Spawns a red slime

    2: Spawns a blue slime

    3: Spawn a yellow slime

    4: Spawn an eldritch slime

    9: Spawns Berry (food) at mouse point (max of 3 foods plus an additional 3 per slime spawned (max of 12))

    0: Spawns Drum Stick (food) at mouse point (max of 3 foods plus an additional 3 per slime spawned (max of 12))

    SPACE: Pause the game

    C: Clean waste at mouse

    H: Toggles Creature Hit Boxes

    V: Toggles Creature Vision Ranges

    X: Gives creature EXP points ('exp_gain' in world_config.ini) (current affects every single creature)

    Z: Toggle world speed increase ( 1x / 10x )

    Numpad Keys 1~6: Spend stat points to increase one of six base stats (current affects every single creature)
    
### Current Functionality

    Basic hunger system (hunger, feeding, starvation)
    Basic stamina system (movement, sleep, rest)
    
