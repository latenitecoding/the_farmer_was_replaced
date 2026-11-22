from __builtins__ import *

# Bush grows over 4.8 s
while True:
    harvest()
    plant(Entities.Bush)
    move(North)

    harvest()
    plant(Entities.Bush)
    move(North)

    # 2 s

    harvest()
    while True:
        if can_harvest():
            break

    harvest()
    while True:
        if can_harvest():
            break

    # 3 s
 
    harvest()
    while True:
        if can_harvest():
            break

    harvest()
    while True:
        if can_harvest():
            break

    # 4 s
