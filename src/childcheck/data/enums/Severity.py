"""All Severity enums.

This is the file with the Severity enums and their string
descriptions.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from enum import Enum


class Severity(str, Enum):
    """Enum class for all Severitiess.

    Associates the enum values with their string descriptions.

    Args:
        str: A string representation of Severity.
        Enum: The enum value associated with the Severity.
    """
    LIGHT = "Light"
    MEDIUM = "Medium"
    SEVERE = "Severe"

    def __str__(self) -> str:
        """String override.

        This method returns a string description of the Severity.

        Returns:
            A string describing the Severity.
        """
        return str(self.value)

    def __repr__(self) -> str:
        """Object representation method.

        This method ensures that a string description of
        the Severity is returned when called upon.

        Returns: A string description of the Severity.
        """
        return str(self)
