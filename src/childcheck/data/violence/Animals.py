"""File for the violence against animals class.

This is the file with the class for violence against animals
which holds all information about the violence factor.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.violence.Violence import Violence
from typing import List
from src.childcheck.data.enums.Severity import Severity


class Animals(Violence):
    """Animals violence class.

    Manipulates user data and holds notes on
    the violence specifics.

    Attributes:
        _severity: A protected enum attribute for the severity of the
        violence.
        __torture: A private boolian attribute determining
        if the violence had torture aspects.
        __murder: A private boolian attribute determining
        if the violence involved murder.
        __mutilation: A private boolian attribute determining
        if the violence involved mutilation.
    """

    def __init__(self) -> None:
        """Initiater for the Animals class.

        This method instantiates the violence's attributes to their default
        values.
        """
        super().__init__()
        self.__torture: bool = False
        self.__murder: bool = False
        self.__mutilation: bool = False

    @property
    def name(self) -> str:
        """Name getter.

        This method returns the shortened factor name.

        Returns: A shortened string version of the factor's name.
        """
        return "Animals"

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
        if self.__torture:
            add_on += 2
        if self.__murder:
            add_on += 2
        if self.__mutilation:
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
    def torture(self) -> bool:
        """Torture getter.

        This method returns the boolian value which indicates
        if the violence will have the torture aspects.

        Returns:
            A boolian value which indicates if the violence will
            have the torture aspects.
        """
        return self.__torture

    @torture.setter
    def torture(self, value: bool) -> None:
        """Torture setter.

        This method updates the boolian value which indicates
        if the violence will include the torture aspects.

        Args:
            value: The boolian input determining if the violence will
            have the torture aspects.
        """
        self.__torture = value

    @property
    def murder(self) -> bool:
        """Murder getter.

        This method returns the boolian value which indicates
        if the violence will have the murder aspects.

        Returns:
            A boolian value which indicates if the violence will
            have the murder aspects.
        """
        return self.__murder

    @murder.setter
    def murder(self, value: bool) -> None:
        """Murder setter.

        This method updates the boolian value which indicates
        if the violence will include the murder aspects.

        Args:
            value: The boolian input determining if the violence will
            have the murder aspects.
        """
        self.__murder = value

    @property
    def mutilation(self) -> bool:
        """Mutilation getter.

        This method returns the boolian value which indicates
        if the violence will have the mutilation aspects.

        Returns:
            A boolian value which indicates if the violence will
            have the mutilation aspects.
        """
        return self.__mutilation

    @mutilation.setter
    def mutilation(self, value: bool) -> None:
        """Mutilation setter.

        This method updates the boolian value which indicates
        if the violence will include the mutilation aspects.

        Args:
            value: The boolian input determining if the violence will
            have the mutilation aspects.
        """
        self.__mutilation = value

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
        if self.__torture:
            details.append("Torture present")
        if self.__murder:
            details.append("Murder present")
        if self.__mutilation:
            details.append("Mutilation present")
        return details

    def __str__(self) -> str:
        """String override.

        This method returns a string description of the violence
        based on which severity was chosen and the violence's name.

        Returns:
            A string describing the violence.
        """
        return "{} Animal Violence".format(self._severity)

    def __eq__(self, value:  object) -> bool:
        """Equality determiner.

        This method determines if an inputted object is equal
        to a Animals object.

        Args:
            value: The object being compared to the Animals object.

        Returns:
            A boolian value telling if the object input is equal
            to a Animals object.
        """
        if isinstance(value, Animals):
            return (self._severity == value.severity and
                    self.__torture == value.torture and
                    self.__murder == value.murder and
                    self.__mutilation == value.mutilation)
        else:
            return False
