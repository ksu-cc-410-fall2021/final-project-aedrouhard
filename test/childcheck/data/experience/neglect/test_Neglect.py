from src.childcheck.data.experience.Neglect import Neglect
from src.childcheck.data.enums.Severity import Severity
from src.childcheck.data.experience.Abuse import Abuse
import pytest
from src.childcheck.data.experience.Experience import Experience
from src.childcheck.data.person.Factor import Factor


class TestNeglect:

    def test_default_severity_set_correctly(self):
        experience = Neglect()
        assert experience.severity == Severity.MEDIUM

    def test_returns_correct_name(self):
        experience = Neglect()
        assert experience.name == "Neglect"

    @pytest.mark.parametrize("severity,score", [(Severity.LIGHT, 2),
                                                (Severity.MEDIUM, 4),
                                                (Severity.SEVERE, 10)])
    def test_score_set_correctly(self, severity, score):
        experience = Neglect()
        experience.severity = severity
        assert experience.score == score

    @pytest.mark.parametrize("severity,name", [(Severity.LIGHT, "Light"),
                                               (Severity.MEDIUM, "Medium"),
                                               (Severity.SEVERE, "Severe")])
    def test_name_set_correctly(self, severity, name):
        experience = Neglect()
        experience.severity = severity
        assert str(experience) == "{} Neglect".format(name)

    def test_two_instances_of_same_object_are_equal(self):
        experience1 = Neglect()
        experience2 = Neglect()
        assert experience1 == experience2

    def test_objects_with_different_severities_are_not_equal(self):
        experience1 = Neglect()
        experience1.severity = Severity.LIGHT
        experience2 = Neglect()
        experience2.severity = Severity.MEDIUM
        assert experience1 != experience2

    def test_two_different_objects_are_not_equal(self):
        experience1 = Neglect()
        experience2 = Abuse()
        assert experience1 != experience2

    def test_error_raised_for_score_when_invalid_severity_is_entered(self):
        experience = Neglect()
        experience.severity = "small"
        with pytest.raises(ValueError):
            score = experience.score
            assert score == 0

    def test_notes_should_be_empty(self):
        experience = Neglect()
        assert len(experience.notes) == 0

    def test_object_inherits_from_correct_base_class(self):
        experience = Neglect()
        assert isinstance(experience, Experience)

    def test_object_implements_factor_interface(self):
        experience = Neglect()
        assert isinstance(experience, Factor)
