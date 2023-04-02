"""Tests for Elem."""
#pylint: disable=no-member, invalid-name
import unittest
from src.enums import ElemId, Direction, Rule, Color, Arg
from src.elem import Elems, ElemBuilder


class TestElemBuilder(unittest.TestCase):
    """Tests for ElemBuilder"""

    def test_builder_convenience_methods(self):
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

    def test_builder_build(self):
        """Tests for building the ElemBuilder object."""
        e = ElemBuilder().floor().n().open().yellow().count(10).index(20).channel(30).build()
        self.assertEqual(e.elemid, ElemId.FLOOR)
        self.assertEqual(e.direction, Direction.N)
        self.assertEqual(e.rule, Rule.OPEN)
        self.assertEqual(e.color, Color.YELLOW)
        self.assertEqual(e.count, 10)
        self.assertEqual(e.index, 20)
        self.assertEqual(e.channel, 30)

    def test_builder_from_elem(self):
        """Tests for creating an ElemBuilder from an existing Elem."""
        elem = ElemBuilder().floor().n().open().yellow().count(10).index(20).channel(30).build()
        builder = ElemBuilder(elem)
        self.assertEqual(elem, builder.build())


class TestElems(unittest.TestCase):
    """Tests for Elems"""
    def test_factories(self):
        """Test dynamically added factory methods."""
        # Every Element gets a factory and builder by name.
        for eid in list(ElemId)[1:]:
            elem = getattr(Elems, eid.value)()
            builder = getattr(Elems, f"{eid.value}_builder")()
            self.__do_assertions(elem, builder, eid)

        # These elements get factory and builder by name and direction.
        direction_eids = [ElemId[n] for n in ("PANEL", "FORCE", "CLONER", "ANT", "FIREBALL", "BALL",
                                              "TANK", "GLIDER", "TEETH", "WALKER", "BLOB",
                                              "PARAMECIUM", "PLAYER")]
        for eid in direction_eids:
            for d in [Direction[char] for char in "NESW"]:
                elem = getattr(Elems, f"{eid.value}_{d.value}")()
                builder = getattr(Elems, f"{eid.value}_{d.value}_builder")()
                self.__do_assertions(elem, builder, eid, direction=d)

        # These elements get factory and builder by name and color.
        color_eids = [ElemId[n] for n in ("KEY", "DOOR", "BUTTON")]
        for eid in color_eids:
            for c in list(Color)[1:]:
                elem = getattr(Elems, f"{c}_{eid.value}")()
                builder = getattr(Elems, f"{c}_{eid.value}_builder")()
                self.__do_assertions(elem, builder, eid, color=c)

    def __do_assertions(self, elem, builder, elemid, *, color=Color.NONE, direction=Direction.NONE):
        self.assertEqual(elem, builder.build())
        self.assertEqual(elem.elemid, elemid)
        self.assertEqual(elem.color, color)
        self.assertEqual(elem.direction, direction)
