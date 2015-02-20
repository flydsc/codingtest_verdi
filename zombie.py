'''
Created on 21/02/2015

@author: dongshichao
'''
from creature import Creature

class zombie(Creature):
    '''
    this is the definition of the zombies
    '''
    current_position = (0, 0)
    scores = 0

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
        for m in steps:
            self.makemove(m)
            self.score(grid)
    
    def up(self):
        self.transin()
        self.current_position = (self.current_position[0],self.current_position[1]-1)
        self.transin()
        
    def down(self):
        self.transin()
        self.current_position = (self.current_position[0],self.current_position[1]+1)
        self.transin()
        
    def left(self):
        self.transin()
        self.current_position = (self.current_position[0]-1,self.current_position[1])
        self.transin()
        
    def right(self):
        self.transin()
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



z = zombie((0,1))
z.makemove("U")
print z.current_position