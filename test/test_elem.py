"""Tests for HCC."""

import unittest
from src.elem import Elem, ElemBuilder, Id, Direction, Color, Rule


class TestElem(unittest.TestCase):
    """Tests for Elem"""

    def test_elem(self):
        """Test HCC elements"""
        vals = [Direction.N, Color.RED, Rule.OPEN, 10, 20, 30]
        for id_ in Id:
            e = ElemBuilder(id_).north().red().rule(Rule.OPEN).count(10).channel(20) \
                .index(30).build()
            ordered_vals = [id_] + vals
            self.assertEqual(e, Elem(*ordered_vals))
