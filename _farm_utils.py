from __builtins__ import *

# A library for common farming
# utility actions.


def dist_to(x0, x1):
    # x0: int - starting coordinate
    # x1: int - destination coordinate
    # Returns the signed distance to x1

    wdx0 = get_world_size() - x0
    wdx1 = get_world_size() - x1

    dx = x1 - x0
    wrap_left = x0 + wdx1
    wrap_right = wdx0 + x1

    if dx > 0 and wrap_left < dx:
        return -wrap_left
    if dx < 0 and wrap_right < -dx:
        return wrap_right

    return dx


def get_drone_speed():
    # Returns the current number of ticks
    # the drone uses per second

    if num_unlocked(Unlocks.Speed) == 1:
        return 600
    if num_unlocked(Unlocks.Speed) == 2:
        return 900
    if num_unlocked(Unlocks.Speed) == 3:
        return 1350
    if num_unlocked(Unlocks.Speed) == 4:
        return 2025
    if num_unlocked(Unlocks.Speed) == 5:
        return 3037.5
    return 400


def get_grow_time_for(etype):
    # etype: Entities

    if etype == Entities.Bush:
        return 4.8
    if etype == Entities.Carrot:
        return 7.2
    if etype == Entities.Tree:
        return 8.4
    if etype == Entities.Pumpkin:
        return 3.8
    return 0.5

def get_gtype_for(etype):
    # etype: Entities
    # Returns the proper Grounds for the
    # given Entities.

    if etype == Entities.Grass:
        return Grounds.Grassland

    if etype == Entities.Carrot or etype == Entities.Pumpkin:
        return Grounds.Soil

    return get_ground_type()


def goto(pos):
    # pos: [int, int]

    if len(pos) != 2:
        return

    move_n_dir(dist_to(get_pos_x(), pos[0]), East)
    move_n_dir(dist_to(get_pos_y(), pos[1]), North)


def move_n_dir(signed_dist, direction):
    # signed_dist: int - distance to move in direction
    # direction: North, South, East, or West indicating
    # the direction of movement for signed_ist > 0

    sign = 1
    if signed_dist < 0:
        sign = -1

    for _ in range(sign * signed_dist):
        if signed_dist > 0:
            move(direction)
        else:
            move(reverse_dir(direction))


def reverse_dir(direction):
    # direction: North, South, East, or West
    # Returns the opposite cardinal direction

    if direction == North:
        return South
    if direction == South:
        return North
    if direction == East:
        return West
    return East
