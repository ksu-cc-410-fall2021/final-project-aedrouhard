"""Test file for NoEmpathyPanel.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.childcheck.data.signs.NoEmpathy import NoEmpathy
from src.childcheck.gui.PrimaryWindow import PrimaryWindow
from src.childcheck.gui.signs.NoEmpathyPanel import NoEmpathyPanel
import pytest


class TestNoEmpathyPanel:
    """Test Class for NoEmpathyPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: NoEmpathyPanel = NoEmpathyPanel(PrimaryWindow())
        assert_that(panel._factor, is_(NoEmpathy()))

    def test_bad_action_command(self) -> None:
        """Test bad action command."""
        panel: NoEmpathyPanel = NoEmpathyPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    def test_frequent_checkbutton(self) -> None:
        """Test that frequency checkbutton works."""
        item: NoEmpathy = NoEmpathy()
        panel: NoEmpathyPanel = NoEmpathyPanel(PrimaryWindow(), item)
        panel._frequent.set(False)
        panel.action_performed("save")
        assert_that(item.frequent, is_(False))
        panel._frequent.set(True)
        panel.action_performed("save")
        assert_that(item.frequent, is_(True))

    def test_frequent_checkbutton_set_correctly(self) -> None:
        """Test that frequent checkbutton was set correctly."""
        item: NoEmpathy = NoEmpathy()
        item.frequent = False
        panel: NoEmpathyPanel = NoEmpathyPanel(PrimaryWindow(), item)
        assert_that(panel._frequent.get(), is_(False))
        item.frequent = True
        panel: NoEmpathyPanel = NoEmpathyPanel(PrimaryWindow(), item)
        assert_that(panel._frequent.get(), is_(True))

    def test_cancel_button(self) -> None:
        """Test that the cancel button works."""
        item: NoEmpathy = NoEmpathy()
        panel: NoEmpathyPanel = NoEmpathyPanel(PrimaryWindow(), item)
        panel._frequent.set(False)
        panel.action_performed("cancel")
        unchanged: NoEmpathy = NoEmpathy()
        assert_that(item, is_(unchanged))
