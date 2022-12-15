"""Test Class for ResultsNumberSingleton.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.results.ResultsNumberSingleton import ResultsNumberSingleton


class TestResultsNumberSingleton():
    """Class for testing ResultsNumberSingleton."""

    def test_results_number_is_sequential(self):
        """Test Results number is sequential."""
        single = ResultsNumberSingleton()
        first = single.get_next_results()
        second = single.get_next_results()
        third = single.get_next_results()
        assert second == first + 1
        assert third == second + 1
