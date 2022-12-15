"""Test file for CertainSexPanel.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.childcheck.data.violence.CertainSex import CertainSex
from src.childcheck.data.enums.Severity import Severity
from src.childcheck.gui.PrimaryWindow import PrimaryWindow
from src.childcheck.gui.violence.CertainSexPanel import CertainSexPanel
import pytest


class TestCertainSexPanel:
    """Test Class for CertainSexPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow())
        assert_that(panel._factor, is_(CertainSex()))

    def test_bad_action_command(self) -> None:
        """Test bad action command."""
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("severity", Severity)
    def test_severity_combo_box(self, severity: Severity) -> None:
        """Test the severity combobox."""
        item: CertainSex = CertainSex()
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        panel._severity.set(str(severity))
        panel.action_performed("save")
        assert_that(item.severity, is_(severity))

    @pytest.mark.parametrize("severity", Severity)
    def test_severity_combo_box_set_correctly(self,
                                              severity: Severity) -> None:
        """Test if combobox was set correctly."""
        item: CertainSex = CertainSex()
        item.severity = severity
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        assert_that(panel._severity.get(), is_(str(severity)))

    def test_physical_checkbutton(self) -> None:
        """Test physical checkbutton."""
        item: CertainSex = CertainSex()
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        panel._physical.set(False)
        panel.action_performed("save")
        assert_that(item.physical, is_(False))
        panel._physical.set(True)
        panel.action_performed("save")
        assert_that(item.physical, is_(True))

    def test_physical_checkbutton_set_correctly(self) -> None:
        """Test physical button set."""
        item: CertainSex = CertainSex()
        item.physical = False
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        assert_that(panel._physical.get(), is_(False))
        item.physical = True
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        assert_that(panel._physical.get(), is_(True))

    def test_verbal_checkbutton(self) -> None:
        """Test verbal checkbutton."""
        item: CertainSex = CertainSex()
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        panel._verbal.set(False)
        panel.action_performed("save")
        assert_that(item.verbal, is_(False))
        panel._verbal.set(True)
        panel.action_performed("save")
        assert_that(item.verbal, is_(True))

    def test_verbal_checkbutton_set_correctly(self) -> None:
        """Test button set correctly."""
        item: CertainSex = CertainSex()
        item.verbal = False
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        assert_that(panel._verbal.get(), is_(False))
        item.verbal = True
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        assert_that(panel._verbal.get(), is_(True))

    def test_sexual_checkbutton(self) -> None:
        """Test sexual button."""
        item: CertainSex = CertainSex()
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        panel._sexual.set(False)
        panel.action_performed("save")
        assert_that(item.sexual, is_(False))
        panel._sexual.set(True)
        panel.action_performed("save")
        assert_that(item.sexual, is_(True))

    def test_sexual_checkbutton_set_correctly(self) -> None:
        """Test button set correctly."""
        item: CertainSex = CertainSex()
        item.sexual = False
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        assert_that(panel._sexual.get(), is_(False))
        item.sexual = True
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        assert_that(panel._sexual.get(), is_(True))

    def test_cancel_button(self) -> None:
        """Test cancel button."""
        item: CertainSex = CertainSex()
        panel: CertainSexPanel = CertainSexPanel(PrimaryWindow(), item)
        if item.severity == Severity.MEDIUM:
            panel._severity.set(str(Severity.SEVERE))
        elif item.severity == Severity.SEVERE:
            panel._severity.set(str(Severity.MEDIUM))
        else:
            panel._severity.set(str(Severity.SEVERE))
        panel._physical.set(True)
        panel._verbal.set(True)
        panel._sexual.set(True)
        panel.action_performed("cancel")
        unchanged: CertainSex = CertainSex()
        assert_that(item, is_(unchanged))
