"""Tests for Cell."""

import unittest
from src.cell import Cell, CellBuilder, Layer
from src.elem import Elem, ElemBuilder, Id, Direction, Color, Rule


class TestCell(unittest.TestCase):
    """Tests for Cell"""

    def test_all_ids_assigned_to_layer(self):
        """Test that every Id is assigned to exactly one layer."""
        terrain = CellBuilder.ELEMENTS_BY_LAYER[Layer.TERRAIN]
        button = CellBuilder.ELEMENTS_BY_LAYER[Layer.BUTTON]
        pickup = CellBuilder.ELEMENTS_BY_LAYER[Layer.PICKUP]
        mob = CellBuilder.ELEMENTS_BY_LAYER[Layer.MOB]
        sides = CellBuilder.ELEMENTS_BY_LAYER["sides"]
        all_ = terrain.union(button).union(pickup).union(mob).union(sides)
        self.assertEqual(len(all_),
                         len(terrain) + len(button) + len(pickup) + len(mob) + len(sides))
        self.assertEqual(len(Id), len(all_))

    def test_layer_checks(self):
        """Test Layer checks for cell builder"""
        for id_ in Id:
            elem = ElemBuilder(id_).build()
            builder = CellBuilder()
            if id_ not in CellBuilder.ELEMENTS_BY_LAYER[Layer.TERRAIN]:
                with self.assertRaises(ValueError):
                    builder.terrain(elem)
            if id_ not in CellBuilder.ELEMENTS_BY_LAYER[Layer.BUTTON]:
                with self.assertRaises(ValueError):
                    builder.button(elem)
            if id_ not in CellBuilder.ELEMENTS_BY_LAYER[Layer.PICKUP]:
                with self.assertRaises(ValueError):
                    builder.pickup(elem)
            if id_ not in CellBuilder.ELEMENTS_BY_LAYER[Layer.MOB]:
                with self.assertRaises(ValueError):
                    builder.mob(elem)
            if id_ not in CellBuilder.ELEMENTS_BY_LAYER["sides"]:
                with self.assertRaises(ValueError):
                    builder.north(elem)
                    builder.east(elem)
                    builder.south(elem)
                    builder.west(elem)

    def test_builder(self):
        cell = CellBuilder().terrain(Id.FLOOR).button(Id.BUTTON).pickup(Id.CHIP).mob(Id.BALL) \
            .north(Id.PANEL).east(Id.PANEL).south(Id.PANEL).west(Id.PANEL).build()
        self.assertEqual(cell.terrain.id, Id.FLOOR)
        self.assertEqual(cell.button.id, Id.BUTTON)
        self.assertEqual(cell.pickup.id, Id.CHIP)
        self.assertEqual(cell.mob.id, Id.BALL)
        self.assertEqual(cell.north.id, Id.PANEL)
        self.assertEqual(cell.east.id, Id.PANEL)
        self.assertEqual(cell.south.id, Id.PANEL)
        self.assertEqual(cell.west.id, Id.PANEL)
