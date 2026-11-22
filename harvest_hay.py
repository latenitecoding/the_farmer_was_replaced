from __builtins__ import *
from _farmhand import *

# A program to harvest Hay
PLOT_DIMS = [2, 2]
START_POS = [0, 0]


# Grow time of Grass is 0.5 s
# Drone Speed: 3037.5 ticks per second
# Grass grows every ~1518.75 ticks
# Farming 4 cells of Grass is 1600 ticks
def main():
    while farm_plot(PLOT_DIMS, [Entities.Grass], START_POS):
        continue

    clear_plot(PLOT_DIMS, START_POS)


if __name__ == "__main__":
    main()
