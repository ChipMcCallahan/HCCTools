"""Tests for Level class."""
# pylint: disable=invalid-name,no-member
import unittest
from src.cell import Cell
from src.level import Level
from src.vector import Vector

class TestLevel(unittest.TestCase):
    """Tests for Level class."""
    def test_constructor(self):
        """Tests for Level constructor."""
        level = Level(Vector(10, 10, 1))
        self.assertEqual(level.size, Vector(10, 10, 1))

    def test_at(self):
        """Tests for the Level 'at' method."""  
        level = Level(Vector(10, 10, 1))
        self.assertEqual(level.at(0, 0, 0), Cell.floor())
        self.assertEqual(level.at(9, 9, 0), Cell.floor())

        # x out of bounds
        with self.assertRaises(ValueError):
            level.at(-1, 0, 0)
        with self.assertRaises(ValueError):
            level.at(10, 0, 0)

        # y out of bounds
        with self.assertRaises(ValueError):
            level.at(0, -1, 0)
        with self.assertRaises(ValueError):
            level.at(0, 10, 0)

        # z out of bounds
        with self.assertRaises(ValueError):
            level.at(0, 0, -1)
        with self.assertRaises(ValueError):
            level.at(0, 0, 1)
        