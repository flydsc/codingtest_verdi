'''
Created on 21/02/2015

@author: dongshichao
'''
from creature import Creature

class zombie(Creature):
    '''
    this is the definition of the zombies
    '''
    scores = 0
    boundary = 0
    
    def set_boundary(self,num):
        self.boundary = num
        
    def get_boundary(self):
        return self.boundary
        
    def set_score(self, num):
        self.scores = num
    
    def get_score(self):
        return self.scores

    def makemove(self, str):
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

    def move(self, steps, grid):
        self.set_boundary(grid.shape[0])
        for m in steps:
            self.makemove(m)
            self.score(grid)
    
    def up(self):
        self.transin()
        if self.get_current_position()[1] - 1 < 0:
            self.set_current_position(self.get_current_position()[0], 0)
        else:
            self.set_current_position(self.get_current_position()[0], self.get_current_position()[1] - 1)
        self.transin()
        
    def down(self):
        self.transin()
        if self.get_current_position()[1] + 1 > self.get_boundary():
            self.set_current_position(self.get_current_position()[0], self.get_boundary())
        else:
            self.set_current_position(self.get_current_position()[0], self.get_current_position()[1] + 1)
        self.transin()
        
    def left(self):
        self.transin()
        if self.get_current_position()[0] - 1 < 0:
            self.set_current_position(0, self.get_current_position()[1])
        else:
            self.set_current_position(self.get_current_position()[0] - 1, self.get_current_position()[1])
        self.transin()
        
    def right(self):
        self.transin()
        if self.get_current_position()[0] + 1 > self.get_boundary():
            self.set_current_position(self.get_boundary(), self.get_current_position()[1])
        else:
            self.set_current_position(self.get_current_position()[0] + 1, self.get_current_position()[1])
        self.transin()

    def score(self, grid):
        if grid[self.get_current_position()] == 2:
            self.set_score(self.get_score() + 1)
        
    def __init__(self, initposition):
        '''
        Constructor
        '''
        Creature.__init__(self, initposition)
        self.set_score(0)
