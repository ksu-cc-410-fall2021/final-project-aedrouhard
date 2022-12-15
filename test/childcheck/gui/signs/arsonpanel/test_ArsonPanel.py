"""Test file for ArsonPanel.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.childcheck.data.signs.Arson import Arson
from src.childcheck.gui.PrimaryWindow import PrimaryWindow
from src.childcheck.gui.signs.ArsonPanel import ArsonPanel
import pytest


class TestArsonPanel:
    """Test Class for ArsonPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: ArsonPanel = ArsonPanel(PrimaryWindow())
        assert_that(panel._factor, is_(Arson()))

    def test_bad_action_command(self) -> None:
        """Test bad action command."""
        panel: ArsonPanel = ArsonPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    def test_frequent_checkbutton(self) -> None:
        """Test that frequency checkbutton works."""
        item: Arson = Arson()
        panel: ArsonPanel = ArsonPanel(PrimaryWindow(), item)
        panel._frequent.set(False)
        panel.action_performed("save")
        assert_that(item.frequent, is_(False))
        panel._frequent.set(True)
        panel.action_performed("save")
        assert_that(item.frequent, is_(True))

    def test_frequent_checkbutton_set_correctly(self) -> None:
        """Test that frequent checkbutton was set correctly."""
        item: Arson = Arson()
        item.frequent = False
        panel: ArsonPanel = ArsonPanel(PrimaryWindow(), item)
        assert_that(panel._frequent.get(), is_(False))
        item.frequent = True
        panel: ArsonPanel = ArsonPanel(PrimaryWindow(), item)
        assert_that(panel._frequent.get(), is_(True))

    def test_cancel_button(self) -> None:
        """Test that the cancel button works."""
        item: Arson = Arson()
        panel: ArsonPanel = ArsonPanel(PrimaryWindow(), item)
        panel._frequent.set(False)
        panel.action_performed("cancel")
        unchanged: Arson = Arson()
        assert_that(item, is_(unchanged))
