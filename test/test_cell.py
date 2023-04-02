"""Tests for Cell."""
# pylint: disable=no-member
import unittest
from src.cell import Cells,CellBuilder, Layer
from src.elem import Elems, ElemId


class TestCellBuilder(unittest.TestCase):
    """Tests for CellBuilder"""

    def test_all_ids_assigned_to_layer(self):
        """Test that every ElemId is assigned to exactly one layer."""
        terrain = CellBuilder.ELEMENTS_BY_LAYER[Layer.TERRAIN]
        button = CellBuilder.ELEMENTS_BY_LAYER[Layer.BUTTON]
        pickup = CellBuilder.ELEMENTS_BY_LAYER[Layer.PICKUP]
        mob = CellBuilder.ELEMENTS_BY_LAYER[Layer.MOB]
        sides = CellBuilder.ELEMENTS_BY_LAYER["sides"]
        all_ = terrain.union(button).union(pickup).union(mob).union(sides)
        self.assertEqual(len(all_),
                         len(terrain) + len(button) + len(pickup) + len(mob) + len(sides))
        self.assertEqual(len(ElemId) - 1, len(all_))  # Don't count ElemId.NONE

    def test_build(self):
        """Test build method of CellBuilder class."""
        cell = CellBuilder().add(Elems.floor(), Elems.button(), Elems.chip(), Elems.ball(),
                                 Elems.panel_n(), Elems.panel_e(),
                                 Elems.panel_s(), Elems.panel_w()).build()
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
        cell = Cells.of(Elems.floor(), Elems.button(), Elems.chip(), Elems.ball(),
                                 Elems.panel_n(), Elems.panel_e(),
                                 Elems.panel_s(), Elems.panel_w())
        self.assertEqual(cell.terrain.elemid, ElemId.FLOOR)
        self.assertEqual(cell.button.elemid, ElemId.BUTTON)
        self.assertEqual(cell.pickup.elemid, ElemId.CHIP)
        self.assertEqual(cell.mob.elemid, ElemId.BALL)
        self.assertEqual(cell.n.elemid, ElemId.PANEL)
        self.assertEqual(cell.e.elemid, ElemId.PANEL)
        self.assertEqual(cell.s.elemid, ElemId.PANEL)
        self.assertEqual(cell.w.elemid, ElemId.PANEL)
