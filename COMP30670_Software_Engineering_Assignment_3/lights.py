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
        
    def control(data, size):
        
        # Check if points exceed grid boundaries
        if int(data) < 0:
            a = 0
        elif int(data) > size:
            a = size
        else:
            a = int(data)
            
        return a
                
    def transCheck(self, dataSet, transType):
        
        regEx = ".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*"
        
        if transType == "net":
            
            a1 = str(dataSet).split("\\", 1)
            a2 = a1[0].split("'", 1)
            input = a2[1]
            result = re.match(regEx, input);
            return input, result
        
        else:
            
            result = re.match(regEx, dataSet);
            return dataSet, result
    
    def apply(self, data, lineCount, transType):
        
        pass
          
        # Extract string  
        #input, result = self.transCheck(data[lineCount], transType);
        
   