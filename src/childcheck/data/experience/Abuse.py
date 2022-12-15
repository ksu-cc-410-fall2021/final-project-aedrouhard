"""File for the Abuse experience.

This is the file with the class for the Abuse
which holds all information about the person.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.experience.Experience import Experience
from src.childcheck.data.enums.Severity import Severity


class Abuse(Experience):
    """Abuse experience class.

    Manipulates user data and holds details about
    child's experience.

    Attributes:
        _severity: A protected Severity attribute for the severiy of the
        experience.
    """

    def __init__(self) -> None:
        """Initiater for the Abuse class.

        This method instantiates the experience's attribute to its default
        value.
        """
        super().__init__()

    @property
    def name(self) -> str:
        """Name getter.

        This method returns the shortened experience name.

        Returns: A shortened string version of the experience's name.
        """
        return "Abuse"

    @property
    def score(self) -> int:
        """Score getter.

        This method determines what the score of the experience will be
        based upon its severity enum and returns that int value.

        Returns:
            The experience's total score.

        Raises:
            ValueError: The severity must be a valid Severity enum.
        """
        if self._severity == Severity.LIGHT:
            return 5
        elif self._severity == Severity.MEDIUM:
            return 10
        elif self._severity == Severity.SEVERE:
            return 15
        else:
            raise ValueError("Incorrect severity")

    def __str__(self) -> str:
        """String override.

        This method returns a string description of the experience
        based on which severity was chosen and the experience's name.

        Returns:
            A string describing the experience.
        """
        return "{} Abuse".format(self._severity)

    def __eq__(self, value: object) -> bool:
        """Equality determiner.

        This method determines if an inputted object is equal
        to an Abuse object.

        Args:
            value: The object being compared to the Abuse object.

        Returns:
            A boolian value telling if the object input is equal
            to an Abuse object.
        """
        if isinstance(value, Abuse):
            return (self._severity == value.severity)
        else:
            return False
