"""Tests for Cell."""
# pylint: disable=no-member,invalid-name
import unittest
from src.cell import Cell, ELEMENTS_BY_LAYER
from src.elem import Elem
from src.enums import ElemId, Layer


class TestCellBuilder(unittest.TestCase):
    """Tests for CellBuilder"""
    def test_all_ids_assigned_to_layer(self):
        """Test that every ElemId is assigned to exactly one layer."""
        terrain = ELEMENTS_BY_LAYER[Layer.TERRAIN]
        button = ELEMENTS_BY_LAYER[Layer.BUTTON]
        pickup = ELEMENTS_BY_LAYER[Layer.PICKUP]
        mob = ELEMENTS_BY_LAYER[Layer.MOB]
        sides = ELEMENTS_BY_LAYER["sides"]
        all_ = terrain.union(button).union(pickup).union(mob).union(sides)
        self.assertEqual(len(all_),
                         len(terrain) + len(button) + len(pickup) + len(mob) + len(sides))
        self.assertEqual(len(ElemId) - 1, len(all_))  # Don't count ElemId.NONE

    def test_build(self):
        """Test build method of CellBuilder class."""
        new = Elem.new()
        cell = Cell.new().add(new.floor(), new.button(), new.chip(), new.ball(),
                              new.panel_n(), new.panel_e(), new.panel_s(), new.panel_w())
        self.assertEqual(cell.terrain.elemid, ElemId.FLOOR)
        self.assertEqual(cell.button.elemid, ElemId.BUTTON)
        self.assertEqual(cell.pickup.elemid, ElemId.CHIP)
        self.assertEqual(cell.mob.elemid, ElemId.BALL)
        self.assertEqual(cell.n.elemid, ElemId.PANEL)
        self.assertEqual(cell.e.elemid, ElemId.PANEL)
        self.assertEqual(cell.s.elemid, ElemId.PANEL)
        self.assertEqual(cell.w.elemid, ElemId.PANEL)


class TestCells(unittest.TestCase):
    """Tests for the Cells class."""
    def test_factories(self):
        """Test factory methods of the Cells class."""
        e = Elem.new()
        cell = Cell.new().add(e.floor(), e.button(), e.chip(), e.ball(),
                              e.panel_n(), e.panel_e(), e.panel_s(), e.panel_w())
        self.assertEqual(cell.terrain.elemid, ElemId.FLOOR)
        self.assertEqual(cell.button.elemid, ElemId.BUTTON)
        self.assertEqual(cell.pickup.elemid, ElemId.CHIP)
        self.assertEqual(cell.mob.elemid, ElemId.BALL)
        self.assertEqual(cell.n.elemid, ElemId.PANEL)
        self.assertEqual(cell.e.elemid, ElemId.PANEL)
        self.assertEqual(cell.s.elemid, ElemId.PANEL)
        self.assertEqual(cell.w.elemid, ElemId.PANEL)
