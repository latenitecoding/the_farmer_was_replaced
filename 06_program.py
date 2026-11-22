from __builtins__ import *

# Carrot grows over 7.2 s (~6 s < 7.2 s)
# 600 ticks -> 900 ticks
# Farming = 0.667 s
# 1 tank of water = 0.25 water level
# @ 0.25 water level -> Carrot grows 3.6 s
N = 4
PLOT_SIZE = N * N
DRONE_SPEED = 1350
FARM_TICKS = 600
GROW_TIME = 7.2

LATENCY = PLOT_SIZE * FARM_TICKS / DRONE_SPEED
GROW_FACT = GROW_TIME / LATENCY

def farm_carrots():
	# water-over-wait
	if can_harvest():
		harvest()

		if get_ground_type() != Grounds.Soil:
			till()

		plant(Entities.Carrot)

	elif (
			num_items(Items.Water) > 0
			and get_water() < LATENCY * 0.01 + (GROW_FACT - 1) * 0.25
	):
		use_item(Items.Water)
	return True
	

while True:
	for x in range(N):
		for y in range(N):
			farm_carrots()
			
			if y + 1 == N:
				move(East)
			elif x % 2 == 0:
				move(North)
			else:
				move(South)
