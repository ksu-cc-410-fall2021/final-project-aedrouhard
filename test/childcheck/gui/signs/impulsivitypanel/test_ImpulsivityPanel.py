"""Test file for ImpulsivityPanel.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.childcheck.data.signs.Impulsivity import Impulsivity
from src.childcheck.gui.PrimaryWindow import PrimaryWindow
from src.childcheck.gui.signs.ImpulsivityPanel import ImpulsivityPanel
import pytest


class TestImpulsivityPanel:
    """Test Class for ImpulsivityPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: ImpulsivityPanel = ImpulsivityPanel(PrimaryWindow())
        assert_that(panel._factor, is_(Impulsivity()))

    def test_bad_action_command(self) -> None:
        """Test bad action command."""
        panel: ImpulsivityPanel = ImpulsivityPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    def test_frequent_checkbutton(self) -> None:
        """Test that frequency checkbutton works."""
        item: Impulsivity = Impulsivity()
        panel: ImpulsivityPanel = ImpulsivityPanel(PrimaryWindow(), item)
        panel._frequent.set(False)
        panel.action_performed("save")
        assert_that(item.frequent, is_(False))
        panel._frequent.set(True)
        panel.action_performed("save")
        assert_that(item.frequent, is_(True))

    def test_frequent_checkbutton_set_correctly(self) -> None:
        """Test that frequent checkbutton was set correctly."""
        item: Impulsivity = Impulsivity()
        item.frequent = False
        panel: ImpulsivityPanel = ImpulsivityPanel(PrimaryWindow(), item)
        assert_that(panel._frequent.get(), is_(False))
        item.frequent = True
        panel: ImpulsivityPanel = ImpulsivityPanel(PrimaryWindow(), item)
        assert_that(panel._frequent.get(), is_(True))

    def test_cancel_button(self) -> None:
        """Test that the cancel button works."""
        item: Impulsivity = Impulsivity()
        panel: ImpulsivityPanel = ImpulsivityPanel(PrimaryWindow(), item)
        panel._frequent.set(False)
        panel.action_performed("cancel")
        unchanged: Impulsivity = Impulsivity()
        assert_that(item, is_(unchanged))
