'''
Created on 21/02/2015

@author: dongshichao
'''
from creature import Creature
from matplotlib.pyplot import grid

class zombie(Creature):
    '''
    this is the definition of the zombies
    '''
    current_position = (0, 0)
    scores = 0
    boun = 0

    def makemove(self,str):
        if str == "U":
            return self.up()
        elif str == "D":
            return self.down()
        elif str == "R":
            return self.right()
        elif str == "L":
            return self.left()
        else:
            print "Wrong move input!"

    def move(self,steps,grid):
        self.boun = grid.shape[0]
        for m in steps:
            self.makemove(m)
            self.score(grid)
    
    def up(self):
        self.transin()
        if self.current_position[1]-1 < 0:
            self.current_position = (self.current_position[0],0)
        else:
            self.current_position = (self.current_position[0],self.current_position[1]-1)
        self.transin()
        
    def down(self):
        self.transin()
        if self.current_position[1]+1 > self.boun:
            self.current_position = (self.current_position[0],self.boun)
        else:
            self.current_position = (self.current_position[0],self.current_position[1]+1)
        self.transin()
        
    def left(self):
        self.transin()
        if self.current_position[0]-1 < 0:
            self.current_position = (0,self.current_position[1])
        else:
            self.current_position = (self.current_position[0]-1,self.current_position[1])
        self.transin()
        
    def right(self):
        self.transin()
        if self.current_position[0] + 1 > self.boun:
            self.current_position = (self.boun,self.current_position[1])
        else:
            self.current_position = (self.current_position[0]+1,self.current_position[1])
        self.transin()

    def score(self,grid):
        if grid[self.current_position] == 2:
            self.scores += 1
        
    def __init__(self, initposition):
        '''
        Constructor
        '''
        Creature.__init__(self, initposition)
