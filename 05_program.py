from __builtins__ import *

# Bush grows over 4.8 s
# 600 ticks -> 900 ticks
# Farming = 0.667 s
while True:
    for _ in range(2):
        harvest()
        plant(Entities.Bush)
        move(North)

    for _ in range(2):
        harvest()
        plant(Entities.Bush)
        move(East)

    for _ in range(2):
        harvest()
        plant(Entities.Bush)
        move(South)

    for _ in range(2):
        harvest()
        plant(Entities.Bush)
        move(West)
