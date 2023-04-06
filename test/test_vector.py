"""Tests for Vector class."""
# pylint: disable=invalid-name,no-member
import unittest
from src.vector import Vector

class TestVector(unittest.TestCase):
    """Tests for Vector"""
    def test_of(self):
        """Tests for 'of' factory on Vector."""
        v1 = Vector(10, 10, 10)
        self.assertEqual(v1, Vector(10, 10, 10))

    def test_to_index(self):
        """Tests for 'to_index' utility on Vector."""
        pos = Vector(9, 9, 1)
        size = Vector(10, 10, 2)
        self.assertEqual(pos.to_index(size), 199)

    def test_from_index(self):
        """Tests for 'from_index' factory on Vector."""
        pos = 199
        size = Vector(10, 10, 2)
        self.assertEqual(Vector.from_index(pos, size), Vector(9, 9, 1))
