'''
Created on 20/02/2015

@author: dongshichao
'''
from zombie import zombie
import numpy as np
from creature import Creature
import re

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
		self.grid[self.Zombie.get_current_position()] = 1
		for i in self.victims:
			self.grid[i.get_current_position()] = 2	

	#make move
	def go(self):
		print self.grid
		self.Zombie.move(self.moves,self.grid)
		print self.Zombie.current_position
		print self.Zombie.scores
		
def input_moves_checked(moves):
	moves.upper()
	for i in moves:
		if i != "U" and i != "D" and i!= "L" and i != "R":
			return True
	return False

def input_move_correction(moves):
	input_check = input_moves_checked(moves)	
	while(input_check):
		moves = raw_input("There seems to be something wrong with your input, please try again\n")
		input_check = input_moves_checked(moves)
	return moves

def input_move():# 	"LURRDD"
	moves = raw_input("please input the zombie route\n L:one step to the left \n R:one step to the right\n U:one step toward upside\n D:one step towards downside\n ")
	moves = input_move_correction(moves)
	return moves

def input_dimension_correction(dimension):
	input_check = input_dimension_checked(dimension)	
	while(input_check):
		dimension = raw_input("There seems to be something wrong with your input, please try again\n")
		input_check = input_dimension_checked(dimension)
	return dimension

def input_dimension_checked(temp_di):
	if re.match("^[0-9]+$",temp_di):
		return False
	else:
		return True
# 	return int(raw_input("please input the dimension of the area: \n"))

def input_dimension():
	temp_di = raw_input("please input the dimension of the area: \n")
	dimension = int(input_dimension_correction(temp_di))
	return dimension 

def input_zombie_checked(temp_cos,dimension):
	if len(temp_cos) != 2:
		return False
	elif not (re.match("^[0-9]+$",temp_cos[0]) and re.match("^[0-9]+$",temp_cos[1])):
		return False
	elif int(temp_cos[0])>dimension or int(temp_cos[1])>dimension:
		return False
	else:
		return True
	
def input_zombie_correction(temp_cos,dimension):
	input_check = input_zombie_checked(temp_cos,dimension)	
	while(not input_check):
		temp = raw_input("There seems to be something wrong with your input, please try again\n")
		temp_cos = temp.split(" ")
		input_check = input_zombie_checked(temp_cos,dimension)
	return temp_cos

def input_zombie(dimension):
	temp = raw_input("please input the zombie coordinate: \n")
	temp_cos = temp.split(" ")
	zombie = input_zombie_correction(temp_cos,dimension)
	return (int(zombie[0]),int(zombie[1]))

def input_poor_correction(temp_cos,dimension):
	temp_new = temp_cos.split(" ")
	input_check = input_zombie_checked(temp_new,dimension)	
	while(not input_check):
		print("There seems to be something wrong with your input, please try again\n")
		input_poors()
	return temp_new

def input_poors_muilti(temp,dimension):
	temp_coo = temp.split(",")
	poors = []
	if len(temp_coo) == 0 :
		return None
	else:
		for i in temp_coo:
			creature = input_poor_correction(i,dimension)
			poors.append((int(creature[0]),int(creature[1])))
	return poors

def input_poors(dimension):
	temp = raw_input("please input the Creature coordinates: \n")
	poors = input_poors_muilti(temp,dimension)
	return poors

def play():
	dimension = input_dimension()
		#coordinate
	zombie_position = input_zombie(dimension-1)
	poors_positions = input_poors(dimension-1)
	moves = input_move()
	#[(0,0),(2,2),(0,2)]
	contr = control(dimension,moves,zombie_position,poors_positions)
	contr.go()
	
if __name__ == '__main__':
	play()

# def inputdata():
