from __builtins__ import *
from _farmhand import *

# A program to harvest Pumpkins
# and Weird_Substance
PLOT_DIMS = [8, 8]
START_POS = [0, 0]


def main():
    while farm_plot(PLOT_DIMS, [Entities.Pumpkin], START_POS):
        if not fart_plot(PLOT_DIMS, [Entities.Pumpkin], START_POS):
            break

    clear_plot(PLOT_DIMS, START_POS)


if __name__ == "__main__":
    main()
