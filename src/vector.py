"""Vector class and helpers for HCC tools."""
# pylint: disable=invalid-name,too-many-boolean-expressions
from collections import namedtuple


Vector = namedtuple(
    "Vector",
    ("x", "y", "z")
)


class Vectors:
    """Factories and helpers for Vector class."""

    def __init__(self):
        raise RuntimeError(f"Cannot instantiate {self.__class__} class.")

    @staticmethod
    def of(x: int, y: int, z: int) -> Vector:
        """Vector factory."""
        return Vector(x, y, z)

    @staticmethod
    def to_index(position_vector: Vector, size_vector: Vector) -> int:
        """Convert a position vector to an integer index based on a map size."""
        Vectors.validate_size_vector(size_vector)
        x, y, z = position_vector
        if (x < 0 or x >= size_vector.x) or \
           (y < 0 or y >= size_vector.y) or \
           (z < 0 or z >= size_vector.z):
            raise ValueError(
                f"Position {position_vector} does not fit in size {size_vector}")
        height, width, _ = size_vector
        return z * (height * width) + y * width + x

    @staticmethod
    def from_index(position_index: int, size_vector: Vector) -> Vector:
        """Convert an integer index to a position vector based on a map size."""
        Vectors.validate_size_vector(size_vector)
        height, width, depth = size_vector
        if position_index < 0 or position_index >= height * width * depth:
            raise ValueError(
                f"Position {position_index} does not fit in size {size_vector}")
        z = position_index // (height * width)
        y = (position_index % (height * width)) // width
        x = (position_index % (height * width)) % width
        return Vectors.of(x, y, z)

    @staticmethod
    def is_within(position_vector: Vector, size_vector: Vector) -> bool:
        """Returns true if the position vector falls within a level with a size 
           of the size_vector."""
        x, y, z = position_vector
        width, height, depth = size_vector
        return 0 <= x < width and 0 <= y < height and 0 <= z < depth

    @staticmethod
    def validate_size_vector(size_vector: Vector):
        """Raises ValueError if size_vector has non-positive component(s)."""
        x, y, z = size_vector
        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError(
                f"Found non-positive component on a size vector: {size_vector}")
