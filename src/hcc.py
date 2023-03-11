"""Tools for working with HCC files."""

class HCCCell:
    """Class that represents a single HCC cell with all valid placements."""
    def __init__(self):
        self.terrain, self.button, self.pickup, self.mob = None, None, None, None
        self.north, self.east, self.south, self.west = None, None, None, None

class HCCLevel:
    """Class that represents an HCC level."""
    # pylint: disable=too-many-instance-attributes
    def __init__(self, *, cc1Level=None):
        if cc1Level:
            raise ValueError("Can't parse CC1Levels yet.")
        self.title = "Untitled"
        self.dimensions = (10, 10, 1)
        self.map = [HCCCell() for p in range(self.size())]

    def size(self):
        """Return the x * y * z size of the level."""
        x, y, z = self.dimensions
        return x * y * z
