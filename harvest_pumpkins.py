from __builtins__ import *
from _farmhand import *

# A program to harvest Pumpkins
PLOT_DIMS = [6, 6]
START_POS = [0, 0]


def main():
    col_pairs = []
    col_pairs_start = []
    for i in range(PLOT_DIMS[0] // 2):
        col_pairs.append([2, PLOT_DIMS[1]])
        col_pairs_start.append([2 * i, 0])

    while farm_plot(PLOT_DIMS, [Entities.Pumpkin], START_POS):
        if not grow_plots(col_pairs, [[Entities.Pumpkin]], col_pairs_start):
            break

    clear_plots(PLOT_DIMS, START_POS)


if __name__ == "__main__":
    main()
