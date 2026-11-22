from __builtins__ import *
from _farmhand import *

# A program to harvest Hay
PLOT_DIMS = [2, 2]
START_POS = [0, 0]


def main():
    while farm_plot(PLOT_DIMS, [Entities.Grass], START_POS):
        continue

    clear_plot(PLOT_DIMS, START_POS)


if __name__ == "__main__":
    main()
