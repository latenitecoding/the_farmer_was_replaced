from __builtins__ import *

N = 4
PLOT_SIZE = N * N
DRONE_SPEED = 1350
FARM_TICKS = 600
GROW_TIME = 8.4

LATENCY = PLOT_SIZE * FARM_TICKS / DRONE_SPEED
GROW_FACT = GROW_TIME / LATENCY


def farm_trees(i):
	# water-over-wait
	if can_harvest():
		harvest()

		if i % 2 == 0:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)

	elif (
			num_items(Items.Water) > 0
			and get_water() < LATENCY * 0.01 + (GROW_FACT - 1) * 0.25
	):
		use_item(Items.Water)

	return True


while True:
	for x in range(N):
		for y in range(N):
			farm_trees(x * N + y)
			
			if y + 1 == N:
				move(East)
			elif x % 2 == 0:
				move(North)
			else:
				move(South)