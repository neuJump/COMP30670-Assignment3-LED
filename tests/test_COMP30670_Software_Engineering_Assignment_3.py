#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `COMP30670_Software_Engineering_Assignment_3` package."""


import unittest
from click.testing import CliRunner

# Import urllib
import urllib.request

# Import project
from COMP30670_Software_Engineering_Assignment_3 import cli

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
        assert instructions == ['turn off 660,55 through 986,197\n', '\n', 'turn off 341,304 through 638,850\n', '\n', 'turn off 199,133 through 461,193\n', '\n', 'switch 322,558 through 977,958']