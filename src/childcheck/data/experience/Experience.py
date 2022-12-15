"""File for the parent Experience class.

This is the file with the class parent
experience class which the others are derived.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.person.Factor import Factor
from src.childcheck.data.enums.Severity import Severity
from typing import List
from abc import abstractmethod


class Experience(Factor):
    """Experience class.

    Serves as a parent class to the other Experience classes.
    """

    def __init__(self) -> None:
        """Initiater for the Experience class.

        Sets the severity attribute.
        """
        self._severity = Severity.MEDIUM

    @property
    def severity(self) -> Severity:
        """Severity getter.

        This method returns the desired Severity enum.

        Returns:
            The experience's severity.
        """
        return self._severity

    @severity.setter
    def severity(self, value: Severity) -> None:
        """Severity setter.

        This method updates the experience's severity enum to
        the type indicated by the user.

        Args:
            value: The experience's given severity.
        """
        self._severity = value

    @property
    @abstractmethod
    def score(self) -> int:
        """An abstract score method.

        This method is implemented by the child classes.

        Raises:
            NotImplementedError: Raised if the method is not
            included in the child classes.
        """
        raise NotImplementedError

    @property
    def notes(self) -> List[str]:
        """An notes getter.

        This method is not implemented by the child classes.

        Returns: An empty list.
        """
        empty_list: List[str] = []
        return empty_list
