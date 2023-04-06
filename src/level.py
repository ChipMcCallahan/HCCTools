"""Level class for HCC"""
# pylint: disable=too-few-public-methods, invalid-name, no-member
from src.cell import Cell
from src.vector import Vector, Vectors

class Level:
    """Level class for HCC"""
    def __init__(self, size: Vector = Vectors.of(32, 32, 1)):
        self.size = size
        self.name = "Untitled"
        self.author = "Anonymous"
        self.map = [Cell.floor()] * size.x * size.y * size.z

    def __to_index(self, pos: int | Vector) -> int:
        return pos if isinstance(pos, int) else Vectors.to_index(pos, self.size)

    def at(self, pos: int | Vector) -> Cell:
        """Returns the map cell at the given position."""
        return self.map[self.__to_index(pos)]

    def put(self, pos: int | Vector, cell: Cell):
        """Overwrites the map cell at the given position."""
        self.map[self.__to_index(pos)] = cell
