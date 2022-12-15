from src.childcheck.data.signs.AntiSocial import AntiSocial
from src.childcheck.data.signs.Arson import Arson
import pytest
from src.childcheck.data.signs.Sign import Sign
from src.childcheck.data.person.Factor import Factor


class TestAntiSocial:

    def test_notes_should_be_empty_at_start(self):
        sign = AntiSocial()
        assert len(sign.notes) == 0

    def test_returns_correct_name(self):
        sign = AntiSocial()
        assert sign.name == "AntiSocial"

    def test_score_is_correct_if_frequent(self):
        sign = AntiSocial()
        sign.frequent = True
        assert (sign.score == 20)

    def test_frequent_not_set_by_default(self):
        sign = AntiSocial()
        assert len(sign.notes) == 0

    def test_adding_frequent_updates_notes(self):
        sign = AntiSocial()
        sign.frequent = True
        assert len(sign.notes) == 1

    def test_removing_frequent_updates_notes(self):
        sign = AntiSocial()
        sign.frequent = True
        assert len(sign.notes) == 1
        sign.frequent = False
        assert len(sign.notes) == 0

    def test_two_instances_of_same_object_are_equal(self):
        sign1 = AntiSocial()
        sign2 = AntiSocial()
        assert sign1 == sign2

    def test_objects_with_different_frequencies_are_not_equal(self):
        sign1 = AntiSocial()
        sign2 = AntiSocial()
        sign2.frequent = True
        assert sign1 != sign2

    def test_two_different_objects_are_not_equal(self):
        sign1 = AntiSocial()
        sign2 = Arson()
        assert sign1 != sign2

    def test_correct_string_description_returned(self):
        sign = AntiSocial()
        assert str(sign) == "Anti-Social"

    def test_correct_string_description_returned_frequent(self):
        sign = AntiSocial()
        sign.frequent = True
        assert str(sign) == "Frequently anti-social"

    def test_object_inherits_from_correct_base_class(self):
        sign = AntiSocial()
        assert isinstance(sign, Sign)

    def test_object_implements_factor_interface(self):
        sign = AntiSocial()
        assert isinstance(sign, Factor)
