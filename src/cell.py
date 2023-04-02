"""Classes for HCC cells."""
# pylint: disable=no-member, too-few-public-methods, invalid-name
from collections import namedtuple
from typing import Optional

from src.elem import Elem
from src.enums import Layer, ElemId

# Creates an immutable namedtuple with properties matching everything in the Layer enum.
Cell = namedtuple(
    "Cell",
    tuple(str(layer.value) for layer in Layer)[1:]
)


class Cells:
    """Factories and utilites for Cell class."""
    def __init__(self):
        raise RuntimeError(f"Cannot instantiate {self.__class__} class.")

    @staticmethod
    def of(*elems: Elem) -> Cell:
        """Returns a cell containing all the elems. Elems sharing a layer will overwrite."""
        return CellBuilder().add(*elems).build()

class CellBuilder:
    """Builder class for Cell."""
    ELEMENTS_BY_LAYER = {
        Layer.TERRAIN: {ElemId.SPACE, ElemId.FLOOR, ElemId.WALL, ElemId.INVISIBLE_WALL,
                        ElemId.MYSTERY_WALL, ElemId.POP_UP_WALL, ElemId.WATER, ElemId.FIRE,
                        ElemId.FORCE, ElemId.ICE, ElemId.DIRT, ElemId.GRAVEL, ElemId.SOCKET,
                        ElemId.EXIT, ElemId.DOOR, ElemId.THIEF, ElemId.TOGGLE_WALL, ElemId.TELEPORT,
                        ElemId.TRAP, ElemId.HINT, ElemId.CLONER},
        Layer.BUTTON: {ElemId.BUTTON},
        Layer.PICKUP: {ElemId.KEY, ElemId.FLIPPERS, ElemId.FIRE_BOOTS, ElemId.SKATES,
                       ElemId.SUCTION_BOOTS, ElemId.CHIP, ElemId.BOMB},
        Layer.MOB: {ElemId.BLOCK, ElemId.ANT, ElemId.FIREBALL, ElemId.BALL, ElemId.TANK,
                    ElemId.GLIDER, ElemId.TEETH, ElemId.WALKER, ElemId.BLOB, ElemId.PARAMECIUM,
                    ElemId.PLAYER},
        "sides": {ElemId.PANEL}
    }

    def __init__(self, cell: Optional[Cell] = None):
        self.args = {layer: None for layer in list(Layer)[1:]}
        if cell:
            for layer in list(Layer)[1:]:
                self.args[layer] = getattr(cell, layer.value)

    def add(self, *elems: Elem):
        """Add an element or group of elements to the cell, inferring layers. Elements will be
        overwritten if they share a common layer."""
        by_layer = CellBuilder.ELEMENTS_BY_LAYER
        for elem in elems:
            updated = False
            for layer_key, layer_set in by_layer.items():
                if not updated and elem.elemid in layer_set:
                    layer = Layer[elem.direction.name] if layer_key == "sides" else layer_key
                    self.args[layer] = elem
                    updated = True
            if not updated:
                raise ValueError(f"{elem} could not be mapped to a layer.")
        return self

    def build(self) -> Cell:
        """Build the immutable Cell object."""
        ordered_args = []
        for layer in list(Layer)[1:]:
            ordered_args.append(self.args[layer])
        return Cell(*ordered_args)
