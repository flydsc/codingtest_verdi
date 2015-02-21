'''
Created on 20/02/2015

@author: dongshichao
'''
from zombie import zombie
import numpy as np
from creature import Creature

class control():

	#input
	def __init__(self,dimension,moves,zombie_position,poors_positions):
		self.dimension = dimension
		self.moves = moves
		self.zombie_position = zombie_position
		self.poors_positions = poors_positions
		self.initdata()

	#initialization 
	def initdata(self):
		self.grid = np.zeros((self.dimension,self.dimension))
		self.Zombie = zombie(self.zombie_position)
		self.victims =[]
		for vi in self.poors_positions:
			temp = Creature(vi)
			self.victims.append(temp)
		self.grid[self.Zombie.current_position] = 1
		for i in self.victims:
			self.grid[i.current_position] = 2	

	#make move
	def go(self):
		print self.grid
		self.Zombie.move(self.moves,self.grid)
		print self.Zombie.current_position
		print self.Zombie.scores

if __name__ == '__main__':
	dimension = raw_input()
	moves = "LURRDD"
	zombie_position = (1,1)
	poors_positions = [(0,0),(2,2),(0,2)]

	contr = control(dimension,moves,zombie_position,poors_positions)
	contr.go()

# def inputdata():
