'''
Created on 20/02/2015

@author: dongshichao
'''
import numpy as np
dimension = 4
grid = np.zeros((dimension,dimension))
start = np.zeros(grid.shape)
back = np.zeros(grid.shape)
#print grid
zombine = (1,1)
poors = [(0,0),(2,2),(0,2)]
grid[zombine] = 1
for poor in poors:
    grid[poor] = 2
start[zombine] = -1
#back = grid
nearhood = []
print grid

