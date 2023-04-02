"""Tests for HCC Enums"""
import enum
import unittest

from src import enums


class TestEnums(unittest.TestCase):
    """Tests for HCC Enums"""

    def test_enums(self):
        """Test that everything in our enums module is standardized."""
        for k, v in enums.__dict__.items():
            if not k.startswith("__") and not k == "Enum":
                # Only enums should be in this module.
                self.assertIsInstance(v, enum.EnumType)

                # Every enum should have a default value named NONE.
                self.assertIsNotNone(v["NONE"])
                for i in v:
                    # Every enum's value should be its name in lowercase.
                    self.assertEqual(i.name.lower(), i.value)
