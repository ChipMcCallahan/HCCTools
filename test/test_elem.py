"""Tests for Elem."""
#pylint: disable=no-member, invalid-name
import unittest
from src.enums import ElemId, Direction, Color
from src.elem import Elem


class TestElem(unittest.TestCase):
    """Tests for Elem"""
    def test_factories(self):
        """Test dynamically added factory methods."""
        # Every Element gets a factory and builder by name.
        for eid in list(ElemId)[1:]:
            elem = getattr(Elem.new(), eid.value)()
            self.__do_assertions(elem, eid)

        # These elements get factory and builder by name and direction.
        direction_eids = [ElemId[n] for n in ("PANEL", "FORCE", "CLONER", "ANT", "FIREBALL", "BALL",
                                              "TANK", "GLIDER", "TEETH", "WALKER", "BLOB",
                                              "PARAMECIUM", "PLAYER")]
        for eid in direction_eids:
            for d in [Direction[char] for char in "NESW"]:
                elem = getattr(Elem.new(), f"{eid.value}_{d.value}")()
                self.__do_assertions(elem, eid, direction=d)

        # These elements get factory and builder by name and color.
        color_eids = [ElemId[n] for n in ("KEY", "DOOR", "BUTTON")]
        for eid in color_eids:
            for c in list(Color)[1:]:
                elem = getattr(Elem.new(), f"{c.value}_{eid.value}")()
                self.__do_assertions(elem, eid, color=c)

    def __do_assertions(self, elem, elemid, *, color=Color.NONE, direction=Direction.NONE):
        self.assertEqual(elem.elemid, elemid)
        self.assertEqual(elem.color, color)
        self.assertEqual(elem.direction, direction)
