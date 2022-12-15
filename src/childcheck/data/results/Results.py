"""Represents a collection of Factors.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.person.Factor import Factor
from typing import Iterator, Iterable, List
from src.childcheck.data.results.ResultsNumberSingleton import ResultsNumberSingleton


class Results(Iterable[Factor]):
    """Class to represent a collection of Factors."""

    def __init__(self) -> None:
        """Constructor."""
        self.__factors: List[Factor] = list()
        self.__results_num: int = 0

    def add_factor(self, factor: Factor) -> None:
        """Add an Factor to the set.

        Args:
            factor: The Factor to add
        """
        self.__factors.append(factor)

    def remove_factor(self, factor: Factor) -> None:
        """Remove an Factor from the set.

        Args:
            factor: The Factor to remove
        """
        if factor not in self.__factors:
            print("Factor not in results")
        else:
            self.__factors.remove(factor)

    @property
    def results_num(self) -> int:
        """Getter for results number."""
        inst = ResultsNumberSingleton()
        self.__results_num = inst.get_next_results()
        return self.__results_num

    @property
    def total(self) -> int:
        """Sum the Factor scores."""
        result: int = 0
        for factor in self.__factors:
            result += factor.score
        return result

    def __iter__(self) -> Iterator[Factor]:
        """Iterates through Factor list."""
        return iter(self.__factors)

    def __len__(self) -> int:
        """Returns the length of results list."""
        return len(self.__factors)

    def __getitem__(self, position: int) -> Factor:
        """Returns a particular Factor in the results."""
        return self.__factors[position]
