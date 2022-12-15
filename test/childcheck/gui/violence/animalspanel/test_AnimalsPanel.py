"""Test file for AnimalsPanel.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.childcheck.data.violence.Animals import Animals
from src.childcheck.data.enums.Severity import Severity
from src.childcheck.gui.PrimaryWindow import PrimaryWindow
from src.childcheck.gui.violence.AnimalsPanel import AnimalsPanel
import pytest


class TestAnimalsPanel:
    """Test Class for AnimalsPanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow())
        assert_that(panel._factor, is_(Animals()))

    def test_bad_action_command(self) -> None:
        """Test bad action command."""
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("severity", Severity)
    def test_severity_combo_box(self, severity: Severity) -> None:
        """Test the severity combobox."""
        item: Animals = Animals()
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        panel._severity.set(str(severity))
        panel.action_performed("save")
        assert_that(item.severity, is_(severity))

    @pytest.mark.parametrize("severity", Severity)
    def test_severity_combo_box_set_correctly(self,
                                              severity: Severity) -> None:
        """Test if combobox was set correctly."""
        item: Animals = Animals()
        item.severity = severity
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        assert_that(panel._severity.get(), is_(str(severity)))

    def test_torture_checkbutton(self) -> None:
        """Test torture checkbutton."""
        item: Animals = Animals()
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        panel._torture.set(False)
        panel.action_performed("save")
        assert_that(item.torture, is_(False))
        panel._torture.set(True)
        panel.action_performed("save")
        assert_that(item.torture, is_(True))

    def test_torture_checkbutton_set_correctly(self) -> None:
        """Test torture button set."""
        item: Animals = Animals()
        item.torture = False
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        assert_that(panel._torture.get(), is_(False))
        item.torture = True
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        assert_that(panel._torture.get(), is_(True))

    def test_murder_checkbutton(self) -> None:
        """Test murder checkbutton."""
        item: Animals = Animals()
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        panel._murder.set(False)
        panel.action_performed("save")
        assert_that(item.murder, is_(False))
        panel._murder.set(True)
        panel.action_performed("save")
        assert_that(item.murder, is_(True))

    def test_murder_checkbutton_set_correctly(self) -> None:
        """Test button set correctly."""
        item: Animals = Animals()
        item.murder = False
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        assert_that(panel._murder.get(), is_(False))
        item.murder = True
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        assert_that(panel._murder.get(), is_(True))

    def test_mutilation_checkbutton(self) -> None:
        """Test mutilation button."""
        item: Animals = Animals()
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        panel._mutilation.set(False)
        panel.action_performed("save")
        assert_that(item.mutilation, is_(False))
        panel._mutilation.set(True)
        panel.action_performed("save")
        assert_that(item.mutilation, is_(True))

    def test_mutilation_checkbutton_set_correctly(self) -> None:
        """Test button set correctly."""
        item: Animals = Animals()
        item.mutilation = False
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        assert_that(panel._mutilation.get(), is_(False))
        item.mutilation = True
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        assert_that(panel._mutilation.get(), is_(True))

    def test_cancel_button(self) -> None:
        """Test cancel button."""
        item: Animals = Animals()
        panel: AnimalsPanel = AnimalsPanel(PrimaryWindow(), item)
        if item.severity == Severity.MEDIUM:
            panel._severity.set(str(Severity.SEVERE))
        elif item.severity == Severity.SEVERE:
            panel._severity.set(str(Severity.MEDIUM))
        else:
            panel._severity.set(str(Severity.SEVERE))
        panel._torture.set(True)
        panel._murder.set(True)
        panel._mutilation.set(True)
        panel.action_performed("cancel")
        unchanged: Animals = Animals()
        assert_that(item, is_(unchanged))
