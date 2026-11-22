from __builtins__ import *
from _farmhand import *

# A program to harvest Wood
PLOT_DIMS = [[4, 4], [2, 3]]
START_POS = [[0, 0], [4, 0]]


# A Tree grows every 8.4 s
# Drone Speed at 3037.5 ticks per second
# A Tree grows every 25_515 ticks
# Need 42x cells of Trees/Bushes
def main():
    while farm_plots(PLOT_DIMS, [[Entities.Tree, Entities.Bush]], START_POS):
        continue

    clear_plots(PLOT_DIMS, START_POS)


if __name__ == "__main__":
    main()
