"""Classes for HCC elements."""
# pylint: disable=invalid-name, too-few-public-methods
from collections import namedtuple
from typing import Optional

from src.enums import ElemId, Color, Direction, Rule, Arg

# Creates an immutable namedtuple with properties matching everything in the Arg enum.
Elem = namedtuple(
    "Elem",
    tuple(str(arg.value) for arg in Arg)[1:]
)


class Elems:
    """Utilities and factories for Elem objects."""
    def __init__(self):
        raise RuntimeError(f"Cannot instantiate {self.__class__} class.")

    @staticmethod
    def of(elemid: ElemId, *,
           rule: Rule = Rule.NONE,
           color: Color = Color.NONE,
           direction: Direction = Direction.NONE,
           count: int = 0,
           index: int = 0,
           channel: int = 0) -> Elem:
        """Construct an element from the provided kwargs."""
        return ElemBuilder().elemid(elemid).rule(rule).color(color).direction(direction) \
            .count(count).index(index).channel(channel).build()


# Dynamically add factory methods for all elements. This allows calling, for example,
# Elems.floor(color=Color.YELLOW) instead of Elems.of(ElemId.FLOOR, color=Color.YELLOW).
def add_factories():
    """Dynamically add factory methods for all elements and associated builders, for example
       Elems.floor() and Elems.floor_builder()."""
    # Every Element gets a factory and builder by name.
    for eid in list(ElemId)[1:]:
        setattr(Elems, eid.value, lambda eid_=eid: Elems.of(eid_))
        setattr(Elems, f"{eid.value}_builder", lambda eid_=eid: ElemBuilder().elemid(eid_))

    # These elements get factory and builder by name and direction.
    direction_eids = [ElemId[n] for n in ("PANEL", "FORCE", "CLONER", "ANT", "FIREBALL", "BALL",
                                          "TANK", "GLIDER", "TEETH", "WALKER", "BLOB", "PARAMECIUM",
                                          "PLAYER")]
    for eid in direction_eids:
        for d in [Direction[char] for char in "NESW"]:
            setattr(Elems, f"{eid.value}_{d.value}",
                    lambda eid_=eid, d_=d: Elems.of(eid_, direction=d_))
            setattr(Elems, f"{eid.value}_{d.value}_builder",
                    lambda eid_=eid, d_=d: ElemBuilder().elemid(eid_).direction(d_))

    # These elements get factory and builder by name and color.
    color_eids = [ElemId[n] for n in ("KEY", "DOOR", "BUTTON")]
    for eid in color_eids:
        for c in list(Color)[1:]:
            setattr(Elems, f"{c}_{eid.value}",
                    lambda eid_=eid, c_=c: Elems.of(eid_, color=c_))
            setattr(Elems, f"{c}_{eid.value}_builder",
                    lambda eid_=eid, c_=c: ElemBuilder().elemid(eid_).color(c_))


add_factories()


class ElemBuilder:
    """Builder class for Elem objects."""

    def __init__(self, elem: Optional[Elem] = None):
        self.args = {
            Arg.ELEMID: ElemId.NONE,
            Arg.RULE: Rule.NONE,
            Arg.COLOR: Color.NONE,
            Arg.DIRECTION: Direction.NONE,
            Arg.COUNT: 0,
            Arg.INDEX: 0,
            Arg.CHANNEL: 0,
        }
        if elem:
            for arg in list(Arg)[1:]:
                self.args[arg] = getattr(elem, arg.value)

        # Set convenience methods on each builder instance.
        # Rename the lambda variable in each call, or it will yield the wrong value.
        for eid in list(ElemId)[1:]:
            setattr(self, eid.value, lambda eid_=eid: self.elemid(eid_))

        for rule in list(Rule)[1:]:
            setattr(self, rule.value, lambda rule_=rule: self.rule(rule_))

        for color in list(Color)[1:]:
            setattr(self, color.value,
                    lambda color_=color: self.color(color_))

        for direction in list(Direction)[1:]:
            setattr(self, direction.value,
                    lambda direction_=direction: self.direction(direction_))

    def __set(self, arg, val):
        self.args[arg] = val
        return self

    def elemid(self, elemid: ElemId):
        """Set the ElemId field of the builder."""
        return self.__set(Arg.ELEMID, elemid)

    def rule(self, rule: Rule):
        """Set the Rule field of the builder."""
        return self.__set(Arg.RULE, rule)

    def color(self, color: Color):
        """Set the Color field of the builder."""
        return self.__set(Arg.COLOR, color)

    def direction(self, direction: Direction):
        """Set the Direction field of the builder."""
        return self.__set(Arg.DIRECTION, direction)

    def count(self, count: int):
        """Set the Count field of the builder."""
        return self.__set(Arg.COUNT, count)

    def index(self, index: int):
        """Set the Index field of the builder."""
        return self.__set(Arg.INDEX, index)

    def channel(self, channel: int):
        """Set the Channel field of the builder."""
        return self.__set(Arg.CHANNEL, channel)

    def build(self) -> Elem:
        """Build the immutable Elem object."""
        ordered_args = []
        for arg in list(Arg)[1:]:
            ordered_args.append(self.args[arg])
        return Elem(*ordered_args)
