"""Level class for HCC"""
# pylint: disable=too-few-public-methods, invalid-name, no-member
from typing import Optional
from src.cell import Cell
from src.vector import Vector

class Level:
    """Level class for HCC"""
    def __init__(self, size: Vector = Vector(32, 32, 1)):
        self.size = size
        self.name = "Untitled"
        self.author = "Anonymous"
        self.map = [Cell.floor()] * size.x * size.y * size.z

    def __to_index(self, pos: int | Vector) -> int:
        return pos if isinstance(pos, int) else pos.to_index(self.size)

    def at(self, pos_or_x: int | Vector, y: Optional[int]=None, z: Optional[int]=None) -> Cell:
        """Returns the map cell at the given position."""
        if y is not None or z is not None:
            assert isinstance(pos_or_x, int) and isinstance(y, int) and isinstance(z, int)
            return self.map[self.__to_index(Vector(pos_or_x, y, z))]
        return self.map[self.__to_index(pos_or_x)]

    def put(self, pos: int | Vector, cell: Cell):
        """Overwrites the map cell at the given position."""
        self.map[self.__to_index(pos)] = cell
