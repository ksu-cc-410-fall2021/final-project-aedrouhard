"""Test file for ExperiencePanel.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""

from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.childcheck.data.experience.Experience import Experience
from src.childcheck.data.enums.Severity import Severity
from src.childcheck.gui.PrimaryWindow import PrimaryWindow
from src.childcheck.gui.experience.ExperiencePanel import ExperiencePanel
import pytest
from src.childcheck.data.experience.Abuse import Abuse


class TestExperiencePanel:
    """Test class for ExperiencePanel."""

    def test_default_constructor(self) -> None:
        """Test the default constructor."""
        panel: ExperiencePanel = ExperiencePanel(PrimaryWindow(), Abuse())
        assert_that(panel._factor, is_(Abuse()))

    def test_bad_action_command(self) -> None:
        """Test bad action command."""
        panel: ExperiencePanel = ExperiencePanel(PrimaryWindow(), Abuse())
        try:
            panel.action_performed("bad")
        except Exception:
            pytest.fail("Unexpected Exception")

    @pytest.mark.parametrize("severity", Severity)
    def test_severity_combo_box(self, severity: Severity) -> None:
        """Test the severity combobox."""
        item: Experience = Abuse()
        panel: ExperiencePanel = ExperiencePanel(PrimaryWindow(), item)
        panel._severity.set(str(severity))
        panel.action_performed("save")
        assert_that(item.severity, is_(severity))

    @pytest.mark.parametrize("severity", Severity)
    def test_severity_combo_box_set_correctly(self,
                                              severity: Severity) -> None:
        """Test if combobox was set correctly."""
        item: Experience = Abuse()
        item.severity = severity
        panel: ExperiencePanel = ExperiencePanel(PrimaryWindow(), item)
        assert_that(panel._severity.get(), is_(str(severity)))

    def test_cancel_button(self) -> None:
        """Test cancel button."""
        item: Experience = Abuse()
        panel: ExperiencePanel = ExperiencePanel(PrimaryWindow(), item)
        if item.severity == Severity.MEDIUM:
            panel._severity.set(str(Severity.SEVERE))
        elif item.severity == Severity.SEVERE:
            panel._severity.set(str(Severity.MEDIUM))
        else:
            panel._severity.set(str(Severity.SEVERE))
        panel.action_performed("cancel")
        unchanged: Experience = Abuse()
        assert_that(item, is_(unchanged))
