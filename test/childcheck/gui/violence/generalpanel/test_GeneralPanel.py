"""Test file for GeneralPanel.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.childcheck.data.violence.General import General
from src.childcheck.data.enums.Severity import Severity
from src.childcheck.gui.PrimaryWindow import PrimaryWindow
from src.childcheck.gui.violence.GeneralPanel import GeneralPanel
import pytest


class TestGeneralPanel:
    """Test Class for GeneralPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: GeneralPanel = GeneralPanel(PrimaryWindow())
        assert_that(panel._factor, is_(General()))

    def test_bad_action_command(self) -> None:
        """Test bad action command."""
        panel: GeneralPanel = GeneralPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("severity", Severity)
    def test_severity_combo_box(self, severity: Severity) -> None:
        """Test the severity combobox."""
        item: General = General()
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        panel._severity.set(str(severity))
        panel.action_performed("save")
        assert_that(item.severity, is_(severity))

    @pytest.mark.parametrize("severity", Severity)
    def test_severity_combo_box_set_correctly(self,
                                              severity: Severity) -> None:
        """Test if combobox was set correctly."""
        item: General = General()
        item.severity = severity
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        assert_that(panel._severity.get(), is_(str(severity)))

    def test_physical_checkbutton(self) -> None:
        """Test physical checkbutton."""
        item: General = General()
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        panel._physical.set(False)
        panel.action_performed("save")
        assert_that(item.physical, is_(False))
        panel._physical.set(True)
        panel.action_performed("save")
        assert_that(item.physical, is_(True))

    def test_physical_checkbutton_set_correctly(self) -> None:
        """Test physical button set."""
        item: General = General()
        item.physical = False
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        assert_that(panel._physical.get(), is_(False))
        item.physical = True
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        assert_that(panel._physical.get(), is_(True))

    def test_verbal_checkbutton(self) -> None:
        """Test verbal checkbutton."""
        item: General = General()
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        panel._verbal.set(False)
        panel.action_performed("save")
        assert_that(item.verbal, is_(False))
        panel._verbal.set(True)
        panel.action_performed("save")
        assert_that(item.verbal, is_(True))

    def test_verbal_checkbutton_set_correctly(self) -> None:
        """Test button set correctly."""
        item: General = General()
        item.verbal = False
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        assert_that(panel._verbal.get(), is_(False))
        item.verbal = True
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        assert_that(panel._verbal.get(), is_(True))

    def test_sexual_checkbutton(self) -> None:
        """Test sexual button."""
        item: General = General()
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        panel._sexual.set(False)
        panel.action_performed("save")
        assert_that(item.sexual, is_(False))
        panel._sexual.set(True)
        panel.action_performed("save")
        assert_that(item.sexual, is_(True))

    def test_sexual_checkbutton_set_correctly(self) -> None:
        """Test button set correctly."""
        item: General = General()
        item.sexual = False
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        assert_that(panel._sexual.get(), is_(False))
        item.sexual = True
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
        assert_that(panel._sexual.get(), is_(True))

    def test_cancel_button(self) -> None:
        """Test cancel button."""
        item: General = General()
        panel: GeneralPanel = GeneralPanel(PrimaryWindow(), item)
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
        unchanged: General = General()
        assert_that(item, is_(unchanged))
