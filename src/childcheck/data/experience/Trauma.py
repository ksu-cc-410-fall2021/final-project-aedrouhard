"""File for the trauma experience.

This is the file with the class for the trauma
which holds all information about the experience.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.experience.Experience import Experience
from src.childcheck.data.enums.Severity import Severity


class Trauma(Experience):
    """Trauma experience class.

    Manipulates user data and holds notes on
    the child's experience.

    Attributes:
        _severity: A private Severity attribute for the Severity of the
        experience.
    """

    def __init__(self) -> None:
        """Initiater for the Trauma class.

        This method instantiates the experience's attribute to its default
        value.
        """
        super().__init__()

    @property
    def name(self) -> str:
        """Name getter.

        This method returns the shortened factor name.

        Returns: A shortened string version of the factor's name.
        """
        return "Trauma"

    @property
    def score(self) -> int:
        """Score getter.

        This method determines what the score of the experience will be
        based upon its Severity enum and returns that int value.

        Returns:
            The experience's total score.

        Raises:
            ValueError: The Severity must be a valid Severity enum.
        """
        if self._severity == Severity.LIGHT:
            return 3
        elif self._severity == Severity.MEDIUM:
            return 5
        elif self._severity == Severity.SEVERE:
            return 9
        else:
            raise ValueError("Incorrect Severity")

    def __str__(self) -> str:
        """String override.

        This method returns a string description of the experience
        based on which Severity was chosen and the experience's name.

        Returns:
            A string describing the experience.
        """
        return "{} Trauma".format(self._severity)

    def __eq__(self, value:  object) -> bool:
        """Equality determiner.

        This method determines if an inputted object is equal
        to a trauma object.

        Args:
            value: The object being compared to the trauma object.

        Returns:
            A boolian value telling if the object input is equal
            to a trauma object.
        """
        if isinstance(value, Trauma):
            return (self._severity == value.severity)
        else:
            return False
