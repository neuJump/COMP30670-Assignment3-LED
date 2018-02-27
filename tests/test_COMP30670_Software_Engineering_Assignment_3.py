#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `COMP30670_Software_Engineering_Assignment_3` package."""


import unittest
from click.testing import CliRunner

from COMP30670_Software_Engineering_Assignment_3 import COMP30670_Software_Engineering_Assignment_3
from COMP30670_Software_Engineering_Assignment_3 import cli


class TestComp30670_software_engineering_assignment_3(unittest.TestCase):
    """Tests for `COMP30670_Software_Engineering_Assignment_3` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'COMP30670_Software_Engineering_Assignment_3.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
