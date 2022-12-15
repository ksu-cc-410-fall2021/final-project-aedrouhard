from src.childcheck.data.violence.Animals import Animals
from src.childcheck.data.enums.Severity import Severity
from src.childcheck.data.violence.General import General
import pytest
from src.childcheck.data.violence.Violence import Violence
from src.childcheck.data.person.Factor import Factor


class TestAnimals:

    def test_notes_should_be_empty_at_start(self):
        violence = Animals()
        assert len(violence.notes) == 0

    def test_default_severity_set_correctly(self):
        violence = Animals()
        assert violence.severity == Severity.MEDIUM

    def test_returns_correct_name(self):
        violence = Animals()
        assert violence.name == "Animals"

    @pytest.mark.parametrize("severity,score", [(Severity.LIGHT, 15),
                                                (Severity.MEDIUM, 25),
                                                (Severity.SEVERE, 30)])
    def test_score_correct(self, severity, score):
        violence = Animals()
        violence.severity = severity
        assert violence.score == score

    @pytest.mark.parametrize("severity,score", [(Severity.LIGHT, 15),
                                                (Severity.MEDIUM, 25),
                                                (Severity.SEVERE, 30)])
    def test_score_with_addon(self, severity, score):
        violence = Animals()
        violence.severity = severity
        violence.torture = True
        assert violence.score == score + 2

    @pytest.mark.parametrize("severity,name", [(Severity.LIGHT, "Light"),
                                               (Severity.MEDIUM, "Medium"),
                                               (Severity.SEVERE, "Severe")])
    def test_name_set_correctly(self, severity, name):
        violence = Animals()
        violence.severity = severity
        assert str(violence) == "{} Animal Violence".format(name)

    @pytest.mark.parametrize("detail", ["torture", "murder", "mutilation"])
    def test_each_additional_detail_not_included(self, detail):
        test = "Animals.{}".format(detail)
        assert not exec(test)

    @pytest.mark.parametrize("detail", ["torture", "murder",
                                        "mutilation"])
    def test_changing_details_updates_notes(self, detail):
        violence = Animals()
        test = "violence.{}".format(detail)
        exec(test+"= True")
        assert len(violence.notes) == 1

    def test_changing_multiple_details_updates_notes(self):
        violence = Animals()
        violence.torture = True
        violence.mutilation = True
        assert len(violence.notes) == 2

    def test_two_instances_of_same_factor_are_equal(self):
        violence1 = Animals()
        violence2 = Animals()
        assert violence1 == violence2

    def test_factors_with_different_severities_are_not_equal(self):
        violence1 = Animals()
        violence1.severity = Severity.MEDIUM
        violence2 = Animals()
        violence2.severity = Severity.LIGHT
        assert violence1 != violence2

    def test_two_different_factors_are_not_equal(self):
        violence1 = Animals()
        violence2 = General()
        assert violence1 != violence2

    def test_error_raised_for_score_when_invalid_severity_is_entered(self):
        violence = Animals()
        violence.severity = "small"
        with pytest.raises(ValueError):
            score = violence.score
            assert score == 0

    def test_object_inherits_from_correct_base_class(self):
        violence = Animals()
        assert isinstance(violence, Violence)

    def test_object_implements_factor_interface(self):
        violence = Animals()
        assert isinstance(violence, Factor)
