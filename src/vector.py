"""Vector class and helpers for HCC tools."""
# pylint: disable=invalid-name,too-many-boolean-expressions,no-member
from collections import namedtuple


Vector = namedtuple(
    "Vector",
    ("x", "y", "z")
)

@staticmethod
def from_index(position_index: int, size_vector: Vector) -> Vector:
    """Convert an integer index to a position vector based on a map size."""
    Vector.validate_size(size_vector)
    height, width, depth = size_vector
    if position_index < 0 or position_index >= height * width * depth:
        raise ValueError(
            f"Position {position_index} does not fit in size {size_vector}")
    z = position_index // (height * width)
    y = (position_index % (height * width)) // width
    x = (position_index % (height * width)) % width
    return Vector(x, y, z)
setattr(Vector, "from_index", from_index)

@staticmethod
def validate_size(size_vector: Vector):
    """Raises ValueError if size_vector has non-positive component(s)."""
    x, y, z = size_vector
    if x <= 0 or y <= 0 or z <= 0:
        raise ValueError(
            f"Found non-positive component on a size vector: {size_vector}")
setattr(Vector, "validate_size", validate_size)

def to_index(self, size_vector: Vector) -> int:
    """Convert a position vector to an integer index based on a map size."""
    self.validate_size(size_vector)
    x, y, z = self
    if (x < 0 or x >= size_vector.x) or \
        (y < 0 or y >= size_vector.y) or \
        (z < 0 or z >= size_vector.z):
        raise ValueError(
            f"Position {self} does not fit in size {size_vector}")
    height, width, _ = size_vector
    return z * (height * width) + y * width + x
setattr(Vector, "to_index", to_index)

def is_within(self, size_vector: Vector) -> bool:
    """Returns true if the position vector falls within a level with a size 
        of the size_vector."""
    x, y, z = self
    width, height, depth = size_vector
    return 0 <= x < width and 0 <= y < height and 0 <= z < depth
setattr(Vector, "is_within", is_within)
