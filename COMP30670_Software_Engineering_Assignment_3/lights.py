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
        
        # Check if points exceed grid boundaries
        if int(t2[0]) < 0:
            self.a = 0
        elif int(t2[0]) > self.size:
            self.a = self.size
        else:
            self.a = int(t2[0])
            
        if int(t2[1]) < 0:
            self.b = 0
        elif int(t2[1]) > self.size:
            self.b = self.size
        else:
            self.b = int(t2[1])
        
        if int(t3[0]) < 0:
            self.c = 0
        elif int(t3[0]) > self.size:
            self.c = self.size
        else:
            self.c = int(t3[0]) + 1
        
        if int(t3[1]) < 0:
            self.d = 0
        elif int(t3[1]) > self.size:
            self.d = self.size
        else:
            self.d = int(t3[1]) + 1
                
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
    
    def apply(data, transType):
          
        # Extract string  
        input, result = LightTest.transCheck(data, transType);
        
        # Scrub strings of whitespace
        input = " ".join(input.split())
        input = input.replace(' ,', ',')
        
        return input
        
   