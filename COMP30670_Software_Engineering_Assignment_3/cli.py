# -*- coding: utf-8 -*-

"""Console script for COMP30670_Software_Engineering_Assignment_3."""
import sys
import click

# Import urllib
import urllib.request

# Import lightTest
#import lights

# Import time
import time

def inputParse(data):
    if data.startswith("http"):
        # Network
        transType = "net"
        size = None
        instructions = []
        with urllib.request.urlopen(data) as response:
           # Read lines
           size = int(response.readline())
           for line in response.readlines():
               instructions.append(line)

        return size, instructions, transType
    else:
        # File
        transType = "file"
        size = None
        instructions = []
        with open(data, 'r') as file:
            size = int(file.readline())
            for line in file.readlines():
                
                instructions.append(line)
                
        return size, instructions, transType

@click.command()
@click.option("--input", default=None, help="input URI (file or URL")
def main(input=None):
    """Console script for COMP30670_Software_Engineering_Assignment_3."""
    start = time.time()
    
    print(input)
    
    print("Working...")
    
    # Parse file
    size, instructions, transType = inputParse(input)
    
    lightsCheck = lights.LightTest(size)
 
    lineCount = 0  
    for line in instructions:
        
        lightsCheck.apply(instructions, lineCount, transType)
        lineCount += 1

    print("Number of lights on:", lightsCheck.lightsCount())
    print("Elapsed time:", time.time() - start)
    return 0

if __name__ == "__main__":
    sys.exit(main())
