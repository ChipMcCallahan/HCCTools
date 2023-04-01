"""Classes and enums for map cells."""
# pylint: disable=missing-function-docstring
# pylint: disable=multiple-statements
# pylint: disable=missing-class-docstring
from enum import Enum
from collections import defaultdict, namedtuple
from .elem import Elem, ElemBuilder, Id, Direction


class Layer(Enum):
    TERRAIN = "terrain"
    BUTTON = "button"
    PICKUP = "pickup"
    MOB = "mob"
    N = "north"
    E = "east"
    S = "south"
    W = "west"


Cell = namedtuple(
    "Cell",
    tuple(layer.value for layer in Layer)
)


class CellBuilder:
    """Builder class for cell."""
    ELEMENTS_BY_LAYER = {
        Layer.TERRAIN: {Id.SPACE, Id.FLOOR, Id.WALL, Id.INVISIBLE_WALL, Id.MYSTERY_WALL,
                        Id.POP_UP_WALL, Id.WATER, Id.FIRE, Id.FORCE, Id.ICE, Id.DIRT, Id.GRAVEL,
                        Id.SOCKET, Id.EXIT, Id.DOOR, Id.THIEF, Id.TOGGLE_WALL, Id.TELEPORT, Id.TRAP,
                        Id.HINT, Id.CLONER},
        Layer.BUTTON: {Id.BUTTON},
        Layer.PICKUP: {Id.KEY, Id.FLIPPERS, Id.FIRE_BOOTS, Id.SKATES, Id.SUCTION_BOOTS, Id.CHIP,
                       Id.BOMB},
        Layer.MOB: {Id.BLOCK, Id.ANT, Id.FIREBALL, Id.BALL, Id.TANK, Id.GLIDER, Id.TEETH, Id.WALKER,
                    Id.BLOB, Id.PARAMECIUM, Id.PLAYER},
        "sides": {Id.PANEL}
    }

    def __init__(self):
        self.args = defaultdict(lambda: None)

    def __add(self, t: Elem | ElemBuilder | Id, layer):
        t = ElemBuilder(t).build() if isinstance(t, Id) else t
        t = t if isinstance(t, Elem) else t.build()
        if t.id not in CellBuilder.ELEMENTS_BY_LAYER["sides" if layer.name in "NESW" else layer]:
            raise ValueError(f"Cannot place {t} in {layer} layer.")
        self.args[layer] = t
        return self

    def terrain(self, t: Elem | ElemBuilder | Id): return self.__add(t, Layer.TERRAIN)

    def button(self, t: Elem | ElemBuilder | Id): return self.__add(t, Layer.BUTTON)

    def pickup(self, t: Elem | ElemBuilder | Id): return self.__add(t, Layer.PICKUP)

    def mob(self, t: Elem | ElemBuilder | Id): return self.__add(t, Layer.MOB)

    def __sides(self, t: Elem | ElemBuilder | Id, d: Direction): return self.__add(t, Layer[d.name])

    def north(self, t: Elem | ElemBuilder | Id): return self.__sides(t, Direction.N)

    def east(self, t: Elem | ElemBuilder | Id): return self.__sides(t, Direction.E)

    def south(self, t: Elem | ElemBuilder | Id): return self.__sides(t, Direction.S)

    def west(self, t: Elem | ElemBuilder | Id): return self.__sides(t, Direction.W)

    def build(self):
        ordered_args = []
        for layer in Layer:
            ordered_args.append(self.args[layer])
        return Cell(*ordered_args)
