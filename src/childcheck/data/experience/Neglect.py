"""File for the neglect Experience.

This is the file with the class for the neglect
which holds all information about the child's experience.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.experience.Experience import Experience
from src.childcheck.data.enums.Severity import Severity


class Neglect(Experience):
    """Neglect Experience class.

    Manipulates user data and holds notes on
    the child's experience.

    Attributes:
        _severity: A protected severity attribute for the severity of the
        Experience.
    """

    def __init__(self) -> None:
        """Initiater for the Neglect class.

        This method instantiates the Experience's attribute to its default
        value.
        """
        super().__init__()

    @property
    def name(self) -> str:
        """Name getter.

        This method returns the shortened factor name.

        Returns: A shortened string version of the factor's name.
        """
        return "Neglect"

    @property
    def score(self) -> int:
        """Score getter.

        This method determines what the score of the Experience will be
        based upon its severity enum and returns that int value.

        Returns:
            The Experience's total score.

        Raises:
            ValueError: The severity must be a valid severity enum.
        """
        if self._severity == Severity.LIGHT:
            return 2
        elif self._severity == Severity.MEDIUM:
            return 4
        elif self._severity == Severity.SEVERE:
            return 10
        else:
            raise ValueError("Incorrect severity")

    def __str__(self) -> str:
        """String override.

        This method returns a string description of the Experience
        based on which severity was chosen and the Experience's name.

        Returns:
            A string describing the Experience.
        """
        return "{} Neglect".format(self._severity)

    def __eq__(self, value: object) -> bool:
        """Equality determiner.

        This method determines if an inputted object is equal
        to a Neglect object.

        Args:
            value: The object being compared to the Neglect object.

        Returns:
            A boolian value telling if the object input is equal
            to a Neglect object.
        """
        if isinstance(value, Neglect):
            return (self._severity == value.severity)
        else:
            return False
