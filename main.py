'''
Created on 20/02/2015

@author: dongshichao
'''
from zombie import zombie
import numpy as np
from creature import Creature

#input
dimension = 4
moves = "LURRDD"
zombie_position = (1,1)
poors_positions = [(0,0),(2,2),(0,2)]

#initialization 
grid = np.zeros((dimension,dimension))
Zombie = zombie(zombie_position)
victims =[]
for vi in poors_positions:
	temp = Creature(vi)
	victims.append(temp)
grid[Zombie.current_position] = 1
for i in victims:
	grid[i.current_position] = 2

#make move
print grid
Zombie.move(moves,grid)
print Zombie.current_position
print Zombie.scores

