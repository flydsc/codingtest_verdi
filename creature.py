'''
Created on 21/02/2015

@author: dongshichao
'''

class Creature(object):
    '''
    classdocs
    '''
    current_position = (0, 0)
    
    def transin(self):
        in_x = self.current_position[0]
        in_y = self.current_position[1]
        self.current_position = (in_y,in_x)

    def __init__(self, initposition):
        '''
        Constructor
        '''
        self.current_position = initposition
        self.transin()
        
