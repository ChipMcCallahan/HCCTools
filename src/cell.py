"""Classes for HCC cells."""
# pylint: disable=no-member, too-few-public-methods, invalid-name
from versatuple import versatuple

from src.elem import Elem
from src.enums import Layer, ElemId

# Creates an immutable namedtuple with properties matching everything in the Layer enum.
layers = ("terrain", "button", "pickup", "mob", "n", "e", "s", "w")
assert layers == tuple(str(layer.value) for layer in Layer)[1:]
Cell = versatuple(
    "Cell",
    layers,
    defaults=tuple([ElemId.NONE]*len(layers)),
    validators={layer_name: lambda layer: isinstance(layer, Layer) for layer_name in layers},
    factories={"space": {"terrain": Elem.new().space()}, "floor": {"terrain": Elem.new().floor()}}
)

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

def add(self, *elems: Elem):
    """Add an element or group of elements to the cell, inferring layers. Elements will be
    overwritten if they share a common layer."""
    updated_layers = {}
    for elem in elems:
        updated = False
        for layer_key, layer_set in ELEMENTS_BY_LAYER.items():
            if not updated and elem.elemid in layer_set:
                layer = Layer[elem.direction.name] if layer_key == "sides" else layer_key
                updated_layers[layer] = elem
                updated = True
        if not updated:
            raise ValueError(f"{elem} could not be mapped to a layer.")
    args = [updated_layers.get(layer, getattr(self, layer.value)) for layer in list(Layer)[1:]]
    return Cell(*args)

setattr(Cell, "add", add)
