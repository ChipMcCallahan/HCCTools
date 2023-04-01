"""Tests for Elem."""

import unittest
from src.elem import Elem, ElemBuilder, Id, Direction, Color, Rule


class TestElem(unittest.TestCase):
    """Tests for Elem"""

    def test_elem(self):
        """Test HCC elements build correctly"""
        vals = (
            [Direction.N, Color.RED, Rule.OPEN, 10, 20, 30],
            [Direction.E, Color.BLUE, Rule.OPEN, 10, 20, 30],
            [Direction.S, Color.YELLOW, Rule.OPEN, 10, 20, 30],
            [Direction.W, Color.GREEN, Rule.OPEN, 10, 20, 30],
            [Direction.W, Color.BROWN, Rule.OPEN, 10, 20, 30],
        )
        for id_ in Id:
            e = ElemBuilder(id_).north().red().rule(Rule.OPEN).count(10).channel(20) \
                .index(30).build()
            ordered_vals = [id_] + vals[0]
            self.assertEqual(e, Elem(*ordered_vals))

        e = ElemBuilder.floor().east().blue().rule(Rule.OPEN).count(10).channel(20) \
            .index(30).build()
        ordered_vals = [Id.FLOOR] + vals[1]
        self.assertEqual(e, Elem(*ordered_vals))

        e = ElemBuilder.wall().south().yellow().rule(Rule.OPEN).count(10).channel(20) \
            .index(30).build()
        ordered_vals = [Id.WALL] + vals[2]
        self.assertEqual(e, Elem(*ordered_vals))

        e = ElemBuilder.block().west().green().rule(Rule.OPEN).count(10).channel(20) \
            .index(30).build()
        ordered_vals = [Id.BLOCK] + vals[3]
        self.assertEqual(e, Elem(*ordered_vals))

        e = ElemBuilder.force().west().brown().rule(Rule.OPEN).count(10).channel(20) \
            .index(30).build()
        ordered_vals = [Id.FORCE] + vals[4]
        self.assertEqual(e, Elem(*ordered_vals))
