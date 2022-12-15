"""File for the ParentPanel.

This is the file with the class for the parent panel
which serves as another panel interface.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from abc import ABC, abstractmethod
from src.childcheck.data.person.Factor import Factor
from typing import List


class ParentPanel(ABC):
    """Class for the parent panel."""

    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        """Subclasshook method."""
        if cls is ParentPanel:
            callables: List[str] = ['save_factor', 'load_selection_panel']
            ret: bool = True
            for call in callables:
                ret = ret and (hasattr(subclass, call)
                               and callable(getattr(subclass, call)))
            return ret
        else:
            return NotImplemented

    @abstractmethod
    def load_selection_panel(self) -> None:
        """Abstract method."""
        raise NotImplementedError

    @abstractmethod
    def save_factor(self, factor: Factor) -> None:
        """Abstract method."""
        raise NotImplementedError
