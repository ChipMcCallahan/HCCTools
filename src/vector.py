"""Vector class and helpers for HCC tools."""
# pylint: disable=invalid-name
from collections import namedtuple


Vector = namedtuple(
    "Vector",
    ("x", "y", "z")
)


class Vectors:
    """Factories and helpers for Vector class."""
    def __init__(self):
        raise RuntimeError("Cannot instantiate Vectors class.")

    @staticmethod
    def of(x: int, y: int, z: int = 0) -> Vector:
        """Vector factory. Can omit the z arg for 2D cases."""
        return Vector(x, y, z)

    @staticmethod
    def to_index(position_vector: Vector, size_vector: Vector) -> int:
        """Convert a position vector to an integer index based on a map size."""
        x, y, z = position_vector
        height, width, _ = size_vector
        return z * (height * width) + y * width + x

    @staticmethod
    def from_index(position_index: int, size_vector: Vector) -> Vector:
        """Convert an integer index to a position vector based on a map size."""
        height, width, _ = size_vector
        z = position_index // (height * width)
        y = (position_index % (height * width)) // width
        x = (position_index % (height * width)) % width
        return Vectors.of(x, y, z)
