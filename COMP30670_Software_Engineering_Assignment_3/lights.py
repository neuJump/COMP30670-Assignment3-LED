# Import system
import sys

# Import re
import re;

# Import numpy
import numpy as np

class LightTest:
    
    lights = None;

    #def __init__(self, size):
    def listTest(size):

        #self.size = size
        lights = np.array([[0]*size for _ in range(size)])
        return lights
        
   