'''
Created on 20/02/2015

@author: dongshichao
'''
import zombie
import numpy as np
from creature import Creature

dimension = 4
grid = np.zeros((dimension,dimension))

zombie_position = (1,1)
poors_positions = [(0,0),(2,2),(0,2)]

Zombie = zombie(zombie_position)
victims =[]

for vi in poors_positions:
	temp = Creature(vi)
	victims += temp

grid[Zombie.current_position] = 1
for i in victims:
	grid[i.current_position] = 2

print grid

