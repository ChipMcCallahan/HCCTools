"""Tests for HCC."""

import unittest
from src.hcc import HCCLevel


class TestHCCLevel(unittest.TestCase):
    """Tests for HCCLevel"""

    def test_init_from_scratch(self):
        """Test level when initialized from scratch."""
        level = HCCLevel()
        self.assertEqual(level.title, "Untitled")
        self.assertEqual(level.dimensions, (10, 10, 1))
        self.assertEqual(level.size(), 100)
