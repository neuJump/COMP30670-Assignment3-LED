# Import system
import sys

# Import re
import re;

# Import numpy
import numpy as np

class LightTest:
    
    lights = None;
    size = 100

    def __init__(self, size):

        self.size = size
        self.lights = np.array([[0]*self.size for _ in range(self.size)])
        
    def control(data, start):
        t1 = data[start:].rsplit(sep=" ", maxsplit=2)
        t2 = t1[0].rsplit(sep=",", maxsplit=1)
        t3 = t1[2].rsplit(sep=",", maxsplit=1)
        
        # Check if points exceed grid boundaries
        if int(t2[0]) < 0:
            a = 0
        elif int(t2[0]) > 100:
            a = 100
        else:
            a = int(t2[0])
            
        return a
                
    def transCheck(dataSet, transType):
        
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
    
    def apply(data, transType, size):
          
        # Extract string  
        input, result = LightTest.transCheck(data, transType);
        
        # Scrub strings of whitespace
        input = " ".join(input.split())
        input = input.replace(' ,', ',')
        
        lights = np.array([[0]*size for _ in range(size)])
    
        if(result != None):
            
            if re.match(".*(turn on).*", input):
                
                # Rows
                for i in range(0,100):
                    # Columns
                    for x in range(0,100):
                        # Modify multi-dimensional array
                        lights[i][x] = 1
                        
        return lights
        
   