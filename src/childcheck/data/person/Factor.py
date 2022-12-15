"""Interface for the childcheck project.

This is the interface file with the Factor class which checks
to see if all subclasses have the score and
notes getter methods.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from abc import ABC, abstractmethod
from typing import List


class Factor(ABC):
    """The Factor class.

    Checks if subclasses have correct getters.

    Attributes:
        callables: List of strings that represent the
        desired included methods.
    """

    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        """Interface method.

        This method will compare a subclass's methods with
        those in the callables list.

        Args:
            cls: The class.
            subclass: The subclass being checked.

        Returns:
            A boolean value telling if the subclass meets all
            requirements or NotImplemented if not.
        """
        if cls is Factor:
            attrs: List[str] = ['score', 'notes']
            callables: List[str] = []
            ret = True
            for attr in attrs:
                ret = ret and (hasattr(subclass, attr)
                               and isinstance(getattr(subclass, attr),
                               property))
            for call in callables:
                ret = ret and (hasattr(subclass, call) and
                               callable(getattr(subclass, call)))
            return ret
        else:
            return NotImplemented

    @property
    @abstractmethod
    def name(self) -> str:
        """Name getter.

        This method returns the shortened factor name.

        Returns: A shortened string version of the factor's name.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def score(self) -> float:
        """An abstract score method.

        This stands as the placeholder for the score method.

        Returns: Score of person.

        Raises:
            NotImplementedError: Raised if the method is absent.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def notes(self) -> List[str]:
        """An abstract notes method.

        This stands as the placeholder for the notes method.

        Raises:
            NotImplementedError: Raised if the method is absent.
        """
        raise NotImplementedError
