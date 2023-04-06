"""Classes for HCC elements."""
# pylint: disable=invalid-name,too-few-public-methods,no-name-in-module
from versatuple import versatuple

from src.enums import ElemId, Color, Direction, Rule, Arg

# Creates an immutable namedtuple with properties matching everything in the Arg enum.
args = ("elemid", "direction", "color", "rule", "count", "channel", "index")
assert args == tuple(str(arg.value) for arg in Arg)[1:]
Elem = versatuple(
    "Elem",
    args,
    defaults=(ElemId.NONE, Direction.NONE, Color.NONE, Rule.NONE, 0, 0, 0),
    validators={
        "elemid": lambda elemid: isinstance(elemid, ElemId) and elemid != ElemId.NONE, # Required.
        "direction": lambda direction: isinstance(direction, Direction), # May be NONE.
        "color": lambda color: isinstance(color, Color), # May be NONE.
        "rule": lambda rule: isinstance(rule, Rule), # May be NONE.
        "count": lambda count: isinstance(count, int) and count >= 0,
        "channel": lambda channel: isinstance(channel, int) and channel >= 0,
        "index": lambda index: isinstance(index, int) and index >= 0
    },
    shortcuts={
        "direction": tuple((d.value, d) for d in list(Direction)[1:]),
        "color": tuple((color.value, color) for color in list(Color)[1:]),
        "rule": tuple((rule.value, rule) for rule in list(Rule)[1:]),
    },
    factories={elemid.value: {"elemid": elemid} for elemid in list(ElemId)[1:]} | \
              {f"{color.value}_key": {"elemid": ElemId.KEY, "color": color}
               for color in list(Color)[1:]} | \
              {f"{color.value}_door": {"elemid": ElemId.DOOR, "color": color}
               for color in list(Color)[1:]} | \
              {f"{color.value}_button": {"elemid": ElemId.BUTTON, "color": color}
               for color in list(Color)[1:]} | \
              {f"{elemid.value}_{d.value}": {"elemid": elemid, "direction": d}
                for d in [Direction.N, Direction.E, Direction.S, Direction.W]
                for elemid in [ElemId.PANEL, ElemId.FORCE, ElemId.CLONER, ElemId.ANT,
                               ElemId.FIREBALL, ElemId.BALL, ElemId.TANK, ElemId.GLIDER,
                               ElemId.TEETH, ElemId.WALKER, ElemId.BLOB, ElemId.PARAMECIUM,
                               ElemId.PLAYER]}
)
