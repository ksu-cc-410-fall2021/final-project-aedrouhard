"""File for the NoEmpathy Sign.

This is the file with the class for the NoEmpathy Sign
which holds all information about the factor.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.signs.Sign import Sign
from typing import List, Set


class NoEmpathy(Sign):
    """NoEmpathy Sign class.

    Manipulates user data and holds notes on sign.

    Attributes:
        __frequent: A private boolian attribute indicating if
        the sign is shown frequently.
    """

    def __init__(self) -> None:
        """Initiater for the NoEmpathy class.

        This method instantiates the Sign's attributes to their default
        values.
        """
        super().__init__()
        self.__frequent: bool = False

    @property
    def name(self) -> str:
        """Name getter.

        This method returns the shortened factor name.

        Returns: A shortened string version of the factor's name.
        """
        return "NoEmpathy"

    @property
    def score(self) -> int:
        """Score getter.

        This method determines what the score of the Sign will be
        based upon its frequency and returns that int value.

        Returns:
            The Sign's total score.
        """
        total = 15
        if self.__frequent:
            total += 15
        return total

    @property
    def frequent(self) -> bool:
        """Frequent getter.

        This method returns the boolian value which indicates
        if the Sign is frequent.

        Returns:
            A boolian value which indicates if the Sign is
            frequent.
        """
        return self.__frequent

    @frequent.setter
    def frequent(self, value: bool) -> None:
        """Frequent setter.

        This method updates the boolian value which indicates
        if the Sign is frequent.

        Args:
            value: The boolian input determining if the Sign
            is frequent.
        """
        self.__frequent = value

    @property
    def notes(self) -> List[str]:
        """Notes getter.

        This method determines which attributes are
        included in the Sign and adds the appropriate messages to
        the notes list.

        Returns:
            A list of strings that indicate which attributes
            to include in the Sign.
        """
        details: List[str] = []
        if self.__frequent:
            details.append("Frequent")
        return details

    def __str__(self) -> str:
        """String override.

        This method returns a string description of the Sign
        based on the frequency and the Sign's name.

        Returns:
            A string describing the Sign.
        """
        if self.__frequent:
            note = "Frequently shows no empathy"
        else:
            note = "Shows no empathy"
        return note

    def __eq__(self, value: object) -> bool:
        """Equality determiner.

        This method determines if an inputted object is equal
        to a NoEmpathy object.

        Args:
            value: The object being compared to the NoEmpathy object.

        Returns:
            A boolian value telling if the object input is equal
            to a NoEmpathy object.
        """
        if isinstance(value, NoEmpathy):
            return (self.__frequent == value.frequent)
        else:
            return False
