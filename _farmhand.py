from __builtins__ import *
from _farm_utils import *

# A library for common farming
# behaviors.
FARM_TICKS = 600

def clear_plot(plot_dims, start_pos=[]):
    # plot_dims: [int, int]
    # start_pos: [int, int]

    if len(start_pos) == 2:
        goto(start_pos)

    plot_size = plot_dims[0] * plot_dims[1]

    for x in range(plot_dims[0]):
        for y in range(plot_dims[1]):
            i = x * plot_dims[1] + y

            harvest()

            if i + 1 < plot_size:
                move(get_next_move(plot_dims[1], i))


def farm_it(plot_size, etype):
    # plot_size: int
    # etype: Entities
    # Returns False if unable to plant etype
 
    if (
            get_entity_type() != etype
            or can_harvest()
    ):
        harvest()

        if get_ground_type() != get_gtype_for(etype):
            till()

        return etype == Entities.Grass or plant(etype)

    latency = plot_size * FARM_TICKS / get_drone_speed()
    grow_factor = get_grow_time_for(etype) / latency
    min_water = latency * 0.01 + (grow_factor - 1) * 0.25

    if min_water > 0.75:
        min_water = 0.75

    if (
            num_items(Items.Water) > 0
            and get_water() <= min_water
    ):
        use_item(Items.Water)

    return True


def farm_plot(plot_dims, lo_etypes, start_pos=[]):
    # plot_dims: [int, int]
    # lo_etypes: List[Entities]
    # start_pos: [int, int]
    # Returns False if unable to plant any etype

    if len(start_pos) == 2:
        goto(start_pos)

    plot_size = plot_dims[0] * plot_dims[1]

    for x in range(plot_dims[0]):
        for y in range(plot_dims[1]):
            i = x * plot_dims[1] + y

            etype = lo_etypes[i % len(lo_etypes)]

            if not farm_it(plot_size, etype):
                return False

            if i + 1 < plot_size:
                move(get_next_move(plot_dims[1], i))

    return True


def get_next_move(Y, i):
    # Y: int - the number of rows
    # i: int - the number of moves
    # Returns the next direction

    if (i + 1) % Y == 0:
        return East
    if (i + 1) // Y % 2 == 0:
        return North
    return South
