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
          
        # Extract string  
        input, result = self.transCheck(data[lineCount], transType);
        
        # Scrub strings of whitespace
        input = " ".join(input.split())
        input = input.replace(' ,', ',')
        
        if(result != None):
            
            if re.match(".*(turn on).*", input):
                
                self.control(input, 8)
                    
                # Rows
                for i in range(int(self.a),int(self.c)):
                    # Columns
                    for x in range(int(self.b),int(self.d)):
                        # Modify multi-dimensional array
                        self.lights[i][x] = 1
                        
            elif re.match(".*(turn off).*", input):
                
                self.control(input, 9)
                
                # Rows
                for i in range(int(self.a),int(self.c)):
                    # Columns
                    for x in range(int(self.b),int(self.d)):
                        # Modify multi-dimensional array
                        self.lights[i][x] = 0
                        
            elif re.match(".*(switch).*", input):
                 
                self.control(input, 7)
                
                # Rows
                for i in range(int(self.a),int(self.c)):
                    # Columns
                    for x in range(int(self.b),int(self.d)):
                        # Modify multi-dimensional array
                        if self.lights[i][x] == 0: 
                            self.lights[i][x] = 1
                        elif self.lights[i][x] == 1:
                            self.lights[i][x] = 0

    def lightsCount(self):
        # Count numpy array
        return np.count_nonzero(self.lights)
    

if __name__ == "__main__":
    sys.exit(main())
        
   