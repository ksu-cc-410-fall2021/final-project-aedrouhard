"""File for the parent violence class.

This is the file with the class parent
violence class which the others are derived.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.person.Factor import Factor
from src.childcheck.data.enums.Severity import Severity
from abc import abstractmethod
from typing import List


class Violence(Factor):
    """Violence class.

    Serves as a parent class to the other violence classes.
    """

    def __init__(self) -> None:
        """Initiater for the violence class.

        Sets the severity attribute.
        """
        self._severity = Severity.MEDIUM

    @property
    def severity(self) -> Severity:
        """Severity getter.

        This method returns the desired severity enum.

        Returns:
            The violence's severity.
        """
        return self._severity

    @severity.setter
    def severity(self, value: Severity) -> None:
        """Severity setter.

        This method updates the violence's severity enum to
        the type indicated by the user.

        Args:
            value: The violence's given severity.
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
    @abstractmethod
    def notes(self) -> List[str]:
        """An abstract notes method.

        This method is implemented by the child classes.

        Raises:
            NotImplementedError: Raised if the method is not
            included in the child classes.
        """
        raise NotImplementedError
