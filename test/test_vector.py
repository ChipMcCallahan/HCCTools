"""Tests for Vector class."""
# pylint: disable=invalid-name
import unittest
from src.vector import Vector, Vectors

class TestVector(unittest.TestCase):
    """Tests for Vector"""
    def test_of(self):
        """Tests for 'of' factory on Vectors."""
        v1 = Vectors.of(10, 10, 10)
        self.assertEqual(v1, Vector(10, 10, 10))
        v2 = Vectors.of(10, 10)
        self.assertEqual(v2, Vector(10, 10, 0))

    def test_to_index(self):
        """Tests for 'to_index' utility on Vectors."""
        pos = Vectors.of(9, 9, 1)
        size = Vectors.of(10, 10, 2)
        self.assertEqual(Vectors.to_index(pos, size), 199)

    def test_from_index(self):
        """Tests for 'from_index' factory on Vectors."""
        pos = 199
        size = Vectors.of(10, 10, 2)
        self.assertEqual(Vectors.from_index(pos, size), Vector(9, 9, 1))
