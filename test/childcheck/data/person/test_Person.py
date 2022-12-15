from src.childcheck.data.person.Person import Person
from src.childcheck.data.enums.Severity import Severity
from src.childcheck.data.violence.General import General
from src.childcheck.data.violence.CertainSex import CertainSex
from src.childcheck.data.violence.Animals import Animals
from src.childcheck.data.experience.Abuse import Abuse
from src.childcheck.data.experience.Trauma import Trauma
from src.childcheck.data.experience.Neglect import Neglect
from src.childcheck.data.signs.Sign import Sign


class TestPerson:

    def test_sign_list_contains_all_signs(self):
        person = Person()
        sign_list = person.signs()
        for i in sign_list:
            assert isinstance(i, Sign)
        assert len(sign_list) == 5

    def test_all_severities_in_experience_list(self):
        person = Person()
        experience_list = person.experience()
        f = 0
        s = 0
        y = 0
        for i in experience_list:
            if isinstance(i, Abuse):
                if i.severity == Severity.LIGHT:
                    f += 1
                elif i.severity == Severity.MEDIUM:
                    f += 3
                elif i.severity == Severity.SEVERE:
                    f += 5
            elif isinstance(i, Trauma):
                if i.severity == Severity.LIGHT:
                    s += 1
                elif i.severity == Severity.MEDIUM:
                    s += 3
                elif i.severity == Severity.SEVERE:
                    s += 5
            elif isinstance(i, Neglect):
                if i.severity == Severity.LIGHT:
                    y += 1
                elif i.severity == Severity.MEDIUM:
                    y += 3
                elif i.severity == Severity.SEVERE:
                    y += 5
        assert (f == 9 and s == 9 and y == 9)

    def test_experience_list_is_correct_length(self):
        person = Person()
        experience_list = person.experience()
        assert len(experience_list) == 9

    def test_all_severities_in_violence_list(self):
        person = Person()
        violence_list = person.violence()
        f = 0
        r = 0
        s = 0
        for i in violence_list:
            if isinstance(i, General):
                if i.severity == Severity.LIGHT:
                    f += 1
                elif i.severity == Severity.MEDIUM:
                    f += 3
                elif i.severity == Severity.SEVERE:
                    f += 5
            elif isinstance(i, CertainSex):
                if i.severity == Severity.LIGHT:
                    r += 1
                elif i.severity == Severity.MEDIUM:
                    r += 3
                elif i.severity == Severity.SEVERE:
                    r += 5
            elif isinstance(i, Animals):
                if i.severity == Severity.LIGHT:
                    s += 1
                elif i.severity == Severity.MEDIUM:
                    s += 3
                elif i.severity == Severity.SEVERE:
                    s += 5
        assert (f == 9 and s == 9 and r == 9)

    def test_violence_list_is_correct_length(self):
        person = Person()
        violence_list = person.violence()
        assert len(violence_list) == 9

    def test_full_list_contains_everything(self):
        person = Person()
        item_list = person.fulllist()
        fr = 0
        sn = 0
        ya = 0
        f = 0
        r = 0
        s = 0
        c = 0
        for i in item_list:
            if isinstance(i, Abuse):
                if i.severity == Severity.LIGHT:
                    fr += 1
                elif i.severity == Severity.MEDIUM:
                    fr += 3
                elif i.severity == Severity.SEVERE:
                    fr += 5
            elif isinstance(i, Trauma):
                if i.severity == Severity.LIGHT:
                    sn += 1
                elif i.severity == Severity.MEDIUM:
                    sn += 3
                elif i.severity == Severity.SEVERE:
                    sn += 5
            elif isinstance(i, Neglect):
                if i.severity == Severity.LIGHT:
                    ya += 1
                elif i.severity == Severity.MEDIUM:
                    ya += 3
                elif i.severity == Severity.SEVERE:
                    ya += 5
            elif isinstance(i, General):
                if i.severity == Severity.LIGHT:
                    f += 1
                elif i.severity == Severity.MEDIUM:
                    f += 3
                elif i.severity == Severity.SEVERE:
                    f += 5
            elif isinstance(i, CertainSex):
                if i.severity == Severity.LIGHT:
                    r += 1
                elif i.severity == Severity.MEDIUM:
                    r += 3
                elif i.severity == Severity.SEVERE:
                    r += 5
            elif isinstance(i, Animals):
                if i.severity == Severity.LIGHT:
                    s += 1
                elif i.severity == Severity.MEDIUM:
                    s += 3
                elif i.severity == Severity.SEVERE:
                    s += 5
            elif isinstance(i, Sign):
                c += 1
        assert (fr == 9 and sn == 9 and ya == 9 and f == 9
                and s == 9 and r == 9 and c == 5)

    def test_full_list_is_correct_length(self):
        person = Person()
        factor_list = person.fulllist()
        assert len(factor_list) == 23
