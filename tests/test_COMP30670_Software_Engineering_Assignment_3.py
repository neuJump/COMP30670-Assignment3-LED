#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `COMP30670_Software_Engineering_Assignment_3` package."""


import unittest
from click.testing import CliRunner

# Import urllib
import urllib.request

# Import project
from COMP30670_Software_Engineering_Assignment_3 import cli
from COMP30670_Software_Engineering_Assignment_3 import lights

class TestComp30670_software_engineering_assignment_3(unittest.TestCase):
    """Tests for `COMP30670_Software_Engineering_Assignment_3` package."""

    def test_command_line_interface(self):
        """Test the CLI."""
        
        # Test file input parsing
        inputFile = "./data/input_test.txt"
        size, instructions, type = cli.inputParse(inputFile)
        assert size is not None
        assert instructions is not None
        assert type == "file"
        
        # Test data returned by the file parsing function
        inputFile = "./data/input_test.txt"
        size, instructions, type = cli.inputParse(inputFile)
        assert size == 4
        assert instructions == ['turn off 660,55 through 986,197\n', '\n', 'turn on 160,45 through 786,457\n', '\n', 'turn off 341,304 through 638,850\n', '\n', 'turn off 199,133 through 461,193\n', '\n', 'switch 322,558 through 977,958']
        
        # Command test 1
        inputFile = "./data/input_test.txt"
        size, instructions, type = cli.inputParse(inputFile)
        instruction1 = instructions[0]
        cmd1 = instruction1[0:8] 
        assert cmd1 == "turn off"
        
        # Command test 2
        inputFile = "./data/input_test.txt"
        size, instructions, type = cli.inputParse(inputFile)
        instruction2 = instructions[2]
        cmd2 = instruction2[0:7]
        assert cmd2 == "turn on"
        
        # Command test 3
        inputFile = "./data/input_test.txt"
        size, instructions, type = cli.inputParse(inputFile)
        instruction3 = instructions[8]
        cmd3 = instruction3[0:6]
        assert cmd3 == "switch"
        
        # Coordinate test
        inputFile = "./data/input_test.txt"
        size, instructions, type = cli.inputParse(inputFile)
        instruction4 = instructions[0]
        x1 = instruction4[9:12]
        x2 = instruction4[13:15]
        y1 = instruction4[24:27]
        y2 = instruction4[28:31]
        assert x1 == "660" 
        assert x2 == "55"
        assert y1 == "986"
        assert y2 == "197"
        
    def test_lights(self):
        """Test lights.py.""" 
        
        # Testing matrix creation
        N = 100
        lightMatrix = lights.LightTest.listTest(N)
        count = 0
        for elem in lightMatrix:
            count += 1
        assert count == 100
        
        # Tested regex
        inputFile = "./data/input_test.txt"
        size, instructions, type = cli.inputParse(inputFile)
        regEx = ".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*"
        for i in instructions:
            lightsRegex = lights.LightTest.transCheck(i, type)
            assert lightsRegex == None
            
        # Test invalid coordinates
        invalid1 = "200"
        invalidCheck = lights.LightTest.control(invalid1, 100)
        assert invalidCheck == 100
        
        
        
        
        
        
        
        
        
        
        