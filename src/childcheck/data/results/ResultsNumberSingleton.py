"""Generates new results number.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
import threading
from typing import Optional


class ResultsNumberSingleton:
    """Class to update the results number."""

    _instance: Optional["ResultsNumberSingleton"] = None
    lock = threading.Lock()

    def __new__(cls) -> "ResultsNumberSingleton":
        """Creates new instance of class if needed."""
        cls._next_results_number = 0
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def get_next_results() -> int:
        """Updates results number."""
        with ResultsNumberSingleton.lock:
            inst = ResultsNumberSingleton()
            inst._next_results_number = inst._next_results_number + 1
            return inst._next_results_number
