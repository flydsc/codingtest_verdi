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
        
    def __init__(self, initposition):
        '''
        Constructor
        '''
        Creature.__init__(self, initposition)

z = zombie((0,1))
z.up()
print z.current_position