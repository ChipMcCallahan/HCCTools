"""Tests for HCC."""

import os
import unittest
from cc_tools import DATHandler
from src.hcc import HCCLevel


class TestHCCLevel(unittest.TestCase):
    """Tests for HCCLevel"""

    def test_init_from_scratch(self):
        """Test level when initialized from scratch."""
        level = HCCLevel()
        self.assertEqual(level.title, "Untitled")
        self.assertEqual(level.dimensions, (10, 10, 1))
        self.assertEqual(level.size(), 100)

    def test_init_from_cc1level(self):
        """Test level when initialized from scratch."""
        with open(os.path.join(os.getcwd(), "sets/dat/test_set.dat"), "rb") as f:
            test_set = DATHandler.parse(f.read())
        self.assertEqual(len(test_set.levels), 1)
