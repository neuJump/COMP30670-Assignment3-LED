# Import system
import sys

# Import re
import re;

# Import numpy
import numpy as np

class LightTest:
    
    lights = None;

    def __init__(self, size):

        self.size = size
        self.lights = np.array([[0]*self.size for _ in range(self.size)])
        
    def control(self, data, start):
        t1 = data[start:].rsplit(sep=" ", maxsplit=2)
        t2 = t1[0].rsplit(sep=",", maxsplit=1)
        t3 = t1[2].rsplit(sep=",", maxsplit=1)
        
    def transCheck(self, dataSet, transType):
        
        # Regular expression
        regEx = ".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*"
    
    def apply(self, data, lineCount, transType):
          
        # Extract string  
        input, result = self.transCheck(data[lineCount], transType);
        
   