from __builtins__ import *
from _farm_utils import *

# A library for common farming
# behaviors.
FARM_TICKS = 600
MOVE_TICKS = 200

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


def clear_plots(lo_plot_dims, lo_start_pos=[]):
    # lo_plot_dims: List[int, int]
    # lo_start_pos: List[int, int]

    for i in range(len(lo_plot_dims)):
        start_pos = []
        if len(start_pos) > 0:
            start_pos = lo_start_pos[i % len(lo_start_pos)]

        clear_plot(lo_plot_dims[i], start_pos)


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
    min_water = min(latency * 0.01 + (grow_factor - 1) * 0.25, 0.75)

    if (
            num_items(Items.Water) > 0
            and get_water() <= min_water
    ):
        use_item(Items.Water)

    return True


def farm_plot(plot_dims, lo_etypes=[], start_pos=[]):
    # plot_dims: [int, int]
    # lo_etypes: List[Entities]
    # start_pos: [int, int]
    # Returns False if unable to plant any etype

    if len(start_pos) == 2:
        goto(start_pos)

    if len(lo_etypes) == 0:
        lo_etypes = [Entities.Grass]

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


def farm_plots(lo_plot_dims, lolo_etypes=[], lo_start_pos=[]):
    # lo_plot_dims: List[int, int]
    # lolo_etypes: List[List[Entities]]
    # lo_start_pos: List[int, int]
    # Returns False if unable to plany any etype

    if len(lolo_etypes) == 0:
        lolo_etypes = [[Entities.Grass]]

    for i in range(len(lo_plot_dims)):
        lo_etypes = lolo_etypes[i % len(lolo_etypes)]

        start_pos = []
        if len(lo_start_pos) > 0:
            start_pos = lo_start_pos[i % len(lo_start_pos)]

        if not farm_plot(lo_plot_dims[i], lo_etypes, start_pos):
            return False

    return True


def grow_it(plot_size, etype):
    # plot_size: int
    # etype: Entities
    # Returns False if unable to plant etype
 
    if get_entity_type() != etype:
        harvest()

        if get_ground_type() != get_gtype_for(etype):
            till()

        if etype == Entities.Grass:
            return True

        if not plant(etype):
            return False
    elif etype == Entities.Grass or can_harvest():
        return True

    total_ticks = plot_size * FARM_TICKS
    if etype == Entities.Pumpkin:
        total_ticks = plot_size * MOVE_TICKS
        total_ticks += plot_size * 0.2 * (FARM_TICKS - MOVE_TICKS)

    latency = total_ticks / get_drone_speed()
    grow_factor = get_grow_time_for(etype) / latency
    min_water = latency * 0.01 + (grow_factor - 1) * 0.25

    if min_water > 0.75:
        min_water = 0.75

    while (
            num_items(Items.Water) > 0
            and get_water() <= min_water
    ):
        use_item(Items.Water)

    return True


def grow_plot(plot_dims, lo_etypes=[], start_pos=[]):
    # plot_dims: [int, int]
    # lo_etypes: List[Entities]
    # start_pos: [int, int]
    # Returns False if unable to plant any etype

    if len(lo_etypes) == 0:
        lo_etypes = [Entities.Grass]

    plot_size = plot_dims[0] * plot_dims[1]
    c_grow = plot_size

    while c_grow > 0:
        c_grow = 0

        if len(start_pos) == 2:
            goto(start_pos)

        for x in range(plot_dims[0]):
            for y in range(plot_dims[1]):
                i = x * plot_dims[1] + y

                etype = lo_etypes[i % len(lo_etypes)]

                if not grow_it(plot_size, etype):
                    return False

                if (
                        etype != Entities.Grass
                        and (get_entity_type() != etype
                             or not can_harvest())
                ):
                    c_grow += 1

                if i + 1 < plot_size:
                    move(get_next_move(plot_dims[1], i))

    return True


def grow_plots(lo_plot_dims, lolo_etypes=[], lo_start_pos=[]):
    # lo_plot_dims: List[int, int]
    # lolo_etypes: List[List[Entities]]
    # lo_start_pos: List[int, int]
    # Returns False if unable to plany any etype

    if len(lolo_etypes) == 0:
        lolo_etypes = [[Entities.Grass]]

    for i in range(len(lo_plot_dims)):
        lo_etypes = lolo_etypes[i % len(lolo_etypes)]

        start_pos = []
        if len(lo_start_pos) > 0:
            start_pos = lo_start_pos[i % len(lo_start_pos)]

        if not grow_plot(lo_plot_dims[i], lo_etypes, start_pos):
            return False

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
