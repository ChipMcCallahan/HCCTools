"""Tools for working with HCC files."""
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=multiple-statements
# pylint: disable=missing-class-docstring
from enum import Enum
from collections import namedtuple, defaultdict


class Id(Enum):
    SPACE = 0
    FLOOR = 1
    WALL = 2
    INVISIBLE_WALL = 3
    MYSTERY_WALL = 4
    POP_UP_WALL = 5
    PANEL = 6
    WATER = 7
    FIRE = 8
    FORCE = 9
    ICE = 10
    DIRT = 11
    GRAVEL = 12
    SOCKET = 13
    EXIT = 14
    DOOR = 15
    THIEF = 16
    TOGGLE_WALL = 17
    TELEPORT = 18
    TRAP = 19
    HINT = 20
    CLONER = 21
    BUTTON = 23
    BOMB = 24
    KEY = 25
    FLIPPERS = 26
    FIRE_BOOTS = 27
    SKATES = 28
    SUCTION_BOOTS = 29
    BLOCK = 30
    ANT = 31
    FIREBALL = 32
    BALL = 33
    TANK = 34
    GLIDER = 35
    TEETH = 36
    WALKER = 37
    BLOB = 38
    PARAMECIUM = 39
    PLAYER = 40


class Color(Enum):
    NO_COLOR = 1
    RED = 2
    BLUE = 3
    YELLOW = 4
    GREEN = 5
    BROWN = 6


class Direction(Enum):
    NONE = 0
    N = 1
    E = 2
    S = 3
    W = 4


class Rule(Enum):
    NO_RULE = 0
    BECOMES_WALL = 1
    BECOMES_FLOOR = 2
    PERSISTS = 3
    OPEN = 4
    SHUT = 5
    TOGGLE = 6
    HOLD_ONE = 7
    HOLD_ALL = 8
    SINGLE_USE = 9
    UNLIMITED_USE = 10


# These string values become the property names of the namedtuple
class Arg(Enum):
    ID = "id"
    DIRECTION = "direction"
    COLOR = "color"
    RULE = "rule"
    COUNT = "count"
    CHANNEL = "channel"
    INDEX = "index"


Elem = namedtuple(
    "Elem",
    tuple(arg.value for arg in Arg)
)


class ElemBuilder:
    """Builder class for Elem."""
    def __init__(self, _id):
        self.args = defaultdict(lambda: None)
        self.args[Arg.ID] = _id

    @staticmethod
    def space(): return ElemBuilder(Id.SPACE)

    @staticmethod
    def floor(): return ElemBuilder(Id.FLOOR)

    @staticmethod
    def wall(): return ElemBuilder(Id.WALL)

    @staticmethod
    def invisible_wall(): return ElemBuilder(Id.INVISIBLE_WALL)

    @staticmethod
    def mystery_wall(): return ElemBuilder(Id.MYSTERY_WALL)

    @staticmethod
    def pop_up_wall(): return ElemBuilder(Id.POP_UP_WALL)

    @staticmethod
    def panel(): return ElemBuilder(Id.PANEL)

    @staticmethod
    def water(): return ElemBuilder(Id.WATER)

    @staticmethod
    def fire(): return ElemBuilder(Id.FIRE)

    @staticmethod
    def force(): return ElemBuilder(Id.FORCE)

    @staticmethod
    def ice(): return ElemBuilder(Id.ICE)

    @staticmethod
    def dirt(): return ElemBuilder(Id.DIRT)

    @staticmethod
    def gravel(): return ElemBuilder(Id.GRAVEL)

    @staticmethod
    def socket(): return ElemBuilder(Id.SOCKET)

    @staticmethod
    def exit(): return ElemBuilder(Id.EXIT)

    @staticmethod
    def door(): return ElemBuilder(Id.DOOR)

    @staticmethod
    def thief(): return ElemBuilder(Id.THIEF)

    @staticmethod
    def toggle_wall(): return ElemBuilder(Id.TOGGLE_WALL)

    @staticmethod
    def teleport(): return ElemBuilder(Id.TELEPORT)

    @staticmethod
    def trap(): return ElemBuilder(Id.TRAP)

    @staticmethod
    def hint(): return ElemBuilder(Id.HINT)

    @staticmethod
    def cloner(): return ElemBuilder(Id.CLONER)

    @staticmethod
    def button(): return ElemBuilder(Id.BUTTON)

    @staticmethod
    def bomb(): return ElemBuilder(Id.BOMB)

    @staticmethod
    def key(): return ElemBuilder(Id.KEY)

    @staticmethod
    def flippers(): return ElemBuilder(Id.FLIPPERS)

    @staticmethod
    def fire_boots(): return ElemBuilder(Id.FIRE_BOOTS)

    @staticmethod
    def skates(): return ElemBuilder(Id.SKATES)

    @staticmethod
    def suction_boots(): return ElemBuilder(Id.SUCTION_BOOTS)

    @staticmethod
    def block(): return ElemBuilder(Id.BLOCK)

    @staticmethod
    def ant(): return ElemBuilder(Id.ANT)

    @staticmethod
    def fireball(): return ElemBuilder(Id.FIREBALL)

    @staticmethod
    def ball(): return ElemBuilder(Id.BALL)

    @staticmethod
    def tank(): return ElemBuilder(Id.TANK)

    @staticmethod
    def glider(): return ElemBuilder(Id.GLIDER)

    @staticmethod
    def teeth(): return ElemBuilder(Id.TEETH)

    @staticmethod
    def walker(): return ElemBuilder(Id.WALKER)

    @staticmethod
    def blob(): return ElemBuilder(Id.BLOB)

    @staticmethod
    def paramecium(): return ElemBuilder(Id.PARAMECIUM)

    @staticmethod
    def player(): return ElemBuilder(Id.PLAYER)

    def direction(self, d: Direction):
        self.args[Arg.DIRECTION] = d
        return self

    def north(self): return self.direction(Direction.N)

    def east(self): return self.direction(Direction.E)

    def south(self): return self.direction(Direction.S)

    def west(self): return self.direction(Direction.W)

    def color(self, c: Color):
        self.args[Arg.COLOR] = c
        return self

    def red(self): return self.color(Color.RED)

    def blue(self): return self.color(Color.BLUE)

    def yellow(self): return self.color(Color.YELLOW)

    def green(self): return self.color(Color.GREEN)

    def brown(self): return self.color(Color.BROWN)

    def rule(self, r: Rule):
        self.args[Arg.RULE] = r
        return self

    def count(self, c: int):
        self.args[Arg.COUNT] = c
        return self

    def channel(self, c: int):
        self.args[Arg.CHANNEL] = c
        return self

    def index(self, i: int):
        self.args[Arg.INDEX] = i
        return self

    def build(self):
        ordered_args = []
        for arg in Arg:
            ordered_args.append(self.args[arg])
        return Elem(*ordered_args)
