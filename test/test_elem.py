"""Tests for Elem."""
#pylint: disable=no-member
import unittest
from src.enums import ElemId, Direction, Rule, Color, Arg
from src.elem import ElemBuilder


class TestElemBuilder(unittest.TestCase):
    """Tests for ElemBuilder"""

    def test_convenience_methods(self):
        """Test convenience methods on ElemBuilder."""
        b = ElemBuilder()
        for eid in list(ElemId)[1:]:
            b = getattr(b, eid.value)()
            self.assertEqual(b.args[Arg.ELEMID], eid)

        for rule in list(Rule)[1:]:
            b = getattr(b, rule.value)()
            self.assertEqual(b.args[Arg.RULE], rule)

        for color in list(Color)[1:]:
            b = getattr(b, color.value)()
            self.assertEqual(b.args[Arg.COLOR], color)

        for direction in list(Direction)[1:]:
            b = getattr(b, direction.value)()
            self.assertEqual(b.args[Arg.DIRECTION], direction)

        b = b.floor().n().open().yellow()
        self.assertEqual(b.args[Arg.ELEMID], ElemId.FLOOR)
        self.assertEqual(b.args[Arg.DIRECTION], Direction.N)
        self.assertEqual(b.args[Arg.RULE], Rule.OPEN)
        self.assertEqual(b.args[Arg.COLOR], Color.YELLOW)

    def test_build(self):
        """Tests for building the ElemBuilder object."""
        e = ElemBuilder().floor().n().open().yellow().count(10).index(20).channel(30).build()
        self.assertEqual(e.elemid, ElemId.FLOOR)
        self.assertEqual(e.direction, Direction.N)
        self.assertEqual(e.rule, Rule.OPEN)
        self.assertEqual(e.color, Color.YELLOW)
        self.assertEqual(e.count, 10)
        self.assertEqual(e.index, 20)
        self.assertEqual(e.channel, 30)

    def test_from_elem(self):
        """Tests for creating an ElemBuilder from an existing Elem."""
        elem = ElemBuilder().floor().n().open().yellow().count(10).index(20).channel(30).build()
        builder = ElemBuilder(elem)
        self.assertEqual(elem, builder.build())
