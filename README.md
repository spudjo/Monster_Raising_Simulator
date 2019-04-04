# Monster_Raising_Simulator

A monster raising simulator based on Monster Rancher.
Currently working on slime creatures as a base for creature functions.

Controls:

1: Spawns a red slime (max of 5 creatures)

2: Spawns a blue slime (max of 5 creatures)

9: Spawns Berry (food) at mouse point (max of 3 foods plus an additional 3 per slime spawned (max of 12))

0: Spawns Drum Stick (food) at mouse point (max of 3 foods plus an additional 3 per slime spawned (max of 12))

SPACE: Pause the game

C: Clean waste at mouse

H: Toggles Creature Hitboxes

V: Toggles Creature Vision Ranges

X: Gives creature EXP points ('exp_gain' in world_config.ini) (current affects every single creature)

Z: Toggle world speed increase ( 1x / 10x )

Numpad Keys 1~6: Spend stat points to increase one of six base stats (current affects every single creature)

Slime will become hungry and seek out food as it's hunger reaches a certain level. 
While starving, health and aether will decrease.

Currently Implemented:

Hunger