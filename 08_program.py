from __builtins__ import *

# Farm: 400 ticks
# Speed: 1350 ticks
# Hay Grow: 675 ticks
# 2x2 grid -> 1600 ticks
while True:
    for x in range(2):
        for y in range(2):
            harvest()

            i = x * 2 + y

            if i == 0:
                move(North)
            elif i == 1:
                move(East)
            elif i == 2:
                move(South)
            else:
                move(West)
