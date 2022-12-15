"""Test Class for Results.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from unittest.mock import patch, PropertyMock
from src.childcheck.data.results.Results import Results
import pytest
from src.childcheck.data.violence.General import General
from src.childcheck.data.signs.WetBed import WetBed
from src.childcheck.data.results.ResultsNumberSingleton import ResultsNumberSingleton


class TestResults():
    """Test Class for Results."""

    def test_results_has_zero_factors(self):
        """Test Results has 0 factors."""
        results = Results()
        assert len(results) == 0

    def test_total_is_zero(self):
        """Test total is zero."""
        results = Results()
        assert results.total == 0

    @patch('src.childcheck.data.signs.WetBed', spec=WetBed)
    def test_adding_factor_changes_properties(self, sign) -> None:
        """Test Change Results properties."""
        type(sign).score = PropertyMock(return_value=10)
        results = Results()
        results.add_factor(sign)
        assert_that(results.total, is_(10))
        assert_that(len(results), is_(1))

    @patch('src.childcheck.data.signs.WetBed', spec=WetBed)
    def test_removing_factor_changes_properties(self, sign) -> None:
        """Test Change Results properties."""
        type(sign).score = PropertyMock(return_value=10)
        results = Results()
        results.add_factor(sign)
        results.remove_factor(sign)
        assert_that(results.total, is_(0))
        assert_that(len(results), is_(0))

    def test_new_results_has_correct_results_number(self):
        """Test new Results has correct number."""
        num = ResultsNumberSingleton()
        num._next_results_number = 3
        results = Results()
        assert_that(results.results_num, is_(4))

    def test_removing_factor_does_not_throw_exception(self, capsys):
        """Test you can remove invalid factor."""
        results = Results()
        results.remove_factor(WetBed())
        captured = capsys.readouterr()
        assert captured.out == "Factor not in results\n"

    @patch('src.childcheck.data.violence.General', spec=General)
    @patch('src.childcheck.data.signs.WetBed', spec=WetBed)
    def test_factor_in_correct_results(self, sign, violence) -> None:
        """Test factors in right order."""
        results = Results()
        results.add_factor(sign)
        results.add_factor(violence)
        assert results[0] == sign
        assert results[1] == violence
