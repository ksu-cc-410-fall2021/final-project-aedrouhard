from src.childcheck.data.signs.Arson import Arson
from src.childcheck.data.signs.AntiSocial import AntiSocial
import pytest
from src.childcheck.data.signs.Sign import Sign
from src.childcheck.data.person.Factor import Factor


class TestArson:

    def test_notes_should_be_empty_at_start(self):
        sign = Arson()
        assert len(sign.notes) == 0

    def test_returns_correct_name(self):
        sign = Arson()
        assert sign.name == "Arson"

    def test_score_is_correct_if_frequent(self):
        sign = Arson()
        sign.frequent = True
        assert (sign.score == 25)

    def test_frequent_not_set_by_default(self):
        sign = Arson()
        assert len(sign.notes) == 0

    def test_adding_frequent_updates_notes(self):
        sign = Arson()
        sign.frequent = True
        assert len(sign.notes) == 1

    def test_removing_frequent_updates_notes(self):
        sign = Arson()
        sign.frequent = True
        assert len(sign.notes) == 1
        sign.frequent = False
        assert len(sign.notes) == 0

    def test_two_instances_of_same_object_are_equal(self):
        sign1 = Arson()
        sign2 = Arson()
        assert sign1 == sign2

    def test_objects_with_different_frequencies_are_not_equal(self):
        sign1 = Arson()
        sign2 = Arson()
        sign2.frequent = True
        assert sign1 != sign2

    def test_two_different_objects_are_not_equal(self):
        sign1 = Arson()
        sign2 = AntiSocial()
        assert sign1 != sign2

    def test_correct_string_description_returned(self):
        sign = Arson()
        assert str(sign) == "Committing arson"

    def test_correct_string_description_returned_frequent(self):
        sign = Arson()
        sign.frequent = True
        assert str(sign) == "Frequently committing arson"

    def test_object_inherits_from_correct_base_class(self):
        sign = Arson()
        assert isinstance(sign, Sign)

    def test_object_implements_factor_interface(self):
        sign = Arson()
        assert isinstance(sign, Factor)
