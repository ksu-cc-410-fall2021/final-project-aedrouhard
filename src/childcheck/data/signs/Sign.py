"""File for the parent Sign class.

This is the file with the class parent
Sign class which the others are derived.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.person.Factor import Factor
from typing import List
from abc import abstractmethod


class Sign(Factor):
    """Sign class.

    Serves as a parent class to the other Sign classes.
    """

    def __init__(self) -> None:
        """Initiater for the Sign class.

        Passed.
        """
        pass

    @property
    @abstractmethod
    def score(self) -> float:
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
