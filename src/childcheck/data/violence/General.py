"""File for the general violence class.

This is the file with the class for general violence
which holds all information about the violence factor.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.violence.Violence import Violence
from typing import List
from src.childcheck.data.enums.Severity import Severity


class General(Violence):
    """General violence class.

    Manipulates user data and holds notes on
    the violence specifics.

    Attributes:
        _severity: A protected enum attribute for the severity of the
        violence.
        __physical: A private boolian attribute determining
        if the violence had physical aspects.
        __verbal: A private boolian attribute determining
        if the violence was verbal.
        __sexual: A private boolian attribute determining
        if the violence was sexual.
    """

    def __init__(self) -> None:
        """Initiater for the General class.

        This method instantiates the violence's attributes to their default
        values.
        """
        super().__init__()
        self.__physical: bool = False
        self.__verbal: bool = False
        self.__sexual: bool = False

    @property
    def name(self) -> str:
        """Name getter.

        This method returns the shortened factor name.

        Returns: A shortened string version of the factor's name.
        """
        return "General"

    @property
    def score(self) -> int:
        """Score getter.

        This method determines what the score of the violence will be
        based upon its severity enum and returns that int value.

        Returns:
            The violence's total score.

        Raises:
            ValueError: The severity must be a valid severity enum.
        """
        add_on: int = 0
        if self.__physical:
            add_on += 2
        if self.__verbal:
            add_on += 2
        if self.__sexual:
            add_on += 2
        if self._severity == Severity.LIGHT:
            return 15 + add_on
        elif self._severity == Severity.MEDIUM:
            return 25 + add_on
        elif self.severity == Severity.SEVERE:
            return 30 + add_on
        else:
            raise ValueError("Incorrect severity")

    @property
    def physical(self) -> bool:
        """Physical getter.

        This method returns the boolian value which indicates
        if the violence has physical aspects.

        Returns:
            A boolian value which indicates if the violence
            has physical aspects.
        """
        return self.__physical

    @physical.setter
    def physical(self, value: bool) -> None:
        """Physical setter.

        This method updates the boolian value which indicates
        if the violence includes physical aspects.

        Args:
            value: The boolian input determining if the violence
            has physical aspects.
        """
        self.__physical = value

    @property
    def verbal(self) -> bool:
        """Verbal getter.

        This method returns the boolian value which indicates
        if the violence has verbal aspects.

        Returns:
            A boolian value which indicates if the violence
            has verbal aspects.
        """
        return self.__verbal

    @verbal.setter
    def verbal(self, value: bool) -> None:
        """Verbal setter.

        This method updates the boolian value which indicates
        if the violence has verbal aspects.

        Args:
            value: The boolian input determining if the violence
            has verbal aspects.
        """
        self.__verbal = value

    @property
    def sexual(self) -> bool:
        """Sexual getter.

        This method returns the boolian value which indicates
        if the violence has sexual aspects.

        Returns:
            A boolian value which indicates if the violence
            has sexual aspects.
        """
        return self.__sexual

    @sexual.setter
    def sexual(self, value: bool) -> None:
        """Sexual setter.

        This method updates the boolian value which indicates
        if the violence has sexual aspects.

        Args:
            value: The boolian input determining if the violence
            has sexual aspects.
        """
        self.__sexual = value

    @property
    def notes(self) -> List[str]:
        """Notes getter.

        This method determines which aspects attributes are
        included in the violence and adds the appropriate messages to
        the notes list.

        Returns:
            A list of strings that indicate which aspectss
            to include in the violence.
        """
        details: List[str] = []
        if self.__physical:
            details.append("Physical present")
        if self.__verbal:
            details.append("Verbal present")
        if self.__sexual:
            details.append("Sexual present")
        return details

    def __str__(self) -> str:
        """String override.

        This method returns a string description of the violence
        based on which severity was chosen and the violence's name.

        Returns:
            A string describing the violence.
        """
        return "{} General Violence".format(self._severity)

    def __eq__(self, value: object) -> bool:
        """Equality determiner.

        This method determines if an inputted object is equal
        to a General object.

        Args:
            value: The object being compared to the General object.

        Returns:
            A boolian value telling if the object input is equal
            to a General object.
        """
        if isinstance(value, General):
            return (self._severity == value.severity and
                    self.__physical == value.physical and
                    self.__verbal == value.verbal and
                    self.__sexual == value.sexual)
        else:
            return False
