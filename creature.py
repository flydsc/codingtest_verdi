'''
Created on 21/02/2015

@author: dongshichao
'''

class Creature(object):
    '''
    classdocs
    '''
    current_position = (0, 0)
    
    def set_current_position(self,x,y):
        self.current_position = (x,y)
        
    def get_current_position(self):
        return self.current_position
    
    def transin(self):
        in_x = self.get_current_position()[0]
        in_y = self.get_current_position()[1]
        self.set_current_position(in_y, in_x)
#         self.current_position = (in_y,in_x)

    def __init__(self, initposition):
        '''
        Constructor
        '''
        self.set_current_position(initposition[0], initposition[1])
        self.transin()
        
