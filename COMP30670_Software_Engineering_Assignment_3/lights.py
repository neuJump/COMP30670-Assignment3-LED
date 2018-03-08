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
        #t1 = data[start:].rsplit(sep=" ", maxsplit=2)
        #t2 = t1[0].rsplit(sep=",", maxsplit=1)
        #t3 = t1[2].rsplit(sep=",", maxsplit=1)
        pass
        
    #def transCheck(self, dataSet, transType):
    def transCheck(dataSet, transType):
        
        # Regular expression
        regEx = ".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*"
        
        if transType == "net":
            
            a1 = str(dataSet).split("\\", 1)
            a2 = a1[0].split("'", 1)
            input = a2[1]
            result = re.match(regEx, input);
            return result
        
        else:
            
            result = re.match(regEx, dataSet);
            return result
    
    def apply(self, data, lineCount, transType):
        
        pass
          
        # Extract string  
        #input, result = self.transCheck(data[lineCount], transType);
        
   