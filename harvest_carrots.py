from __builtins__ import *
from _farmhand import *

# A program to harvest Carrots
PLOT_DIMS = [[4, 4], [2, 2]]
START_POS = [[0, 0], [4, 0]]


def main():
    while farm_plots(PLOT_DIMS, [[Entities.Carrot]], START_POS):
        continue

    clear_plots(PLOT_DIMS, START_POS)


if __name__ == "__main__":
    main()
