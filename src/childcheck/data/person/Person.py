"""File for the Person class.

Contains static getter methods for Person Factors.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.data.person.Factor import Factor
from src.childcheck.data.violence.Animals import Animals
from src.childcheck.data.violence.General import General
from src.childcheck.data.violence.CertainSex import CertainSex
from src.childcheck.data.experience.Abuse import Abuse
from src.childcheck.data.experience.Neglect import Neglect
from src.childcheck.data.experience.Trauma import Trauma
from src.childcheck.data.signs.Arson import Arson
from src.childcheck.data.signs.NoEmpathy import NoEmpathy
from src.childcheck.data.signs.WetBed import WetBed
from src.childcheck.data.signs.Impulsivity import Impulsivity
from src.childcheck.data.signs.AntiSocial import AntiSocial
from typing import List
from src.childcheck.data.enums.Severity import Severity


class Person():
    """Person class.

    Contains methods that will return lists of Factors.
    """

    @staticmethod
    def signs() -> List[Factor]:
        """Sign list method.

        This creates a list of all posible signs.

        Returns: A list of signs.
        """
        sign_factor: List[Factor] = list()
        sign_factor.append(Arson())
        sign_factor.append(NoEmpathy())
        sign_factor.append(WetBed())
        sign_factor.append(Impulsivity())
        sign_factor.append(AntiSocial())
        return sign_factor

    @staticmethod
    def experience() -> List[Factor]:
        """Experience list method.

        This creates a list of all possible experiences.

        Returns: A list of experiences.
        """
        experience_list: List[Factor] = list()
        abusem = Abuse()
        experience_list.append(abusem)
        abusel = Abuse()
        abusel.severity = Severity.LIGHT
        experience_list.append(abusel)
        abuses = Abuse()
        abuses.severity = Severity.SEVERE
        experience_list.append(abuses)
        neglectm = Neglect()
        experience_list.append(neglectm)
        neglectl = Neglect()
        neglectl.severity = Severity.LIGHT
        experience_list.append(neglectl)
        neglects = Neglect()
        neglects.severity = Severity.SEVERE
        experience_list.append(neglects)
        traumam = Trauma()
        experience_list.append(traumam)
        traumal = Trauma()
        traumal.severity = Severity.LIGHT
        experience_list.append(traumal)
        traumas = Trauma()
        traumas.severity = Severity.SEVERE
        experience_list.append(traumas)
        return experience_list

    @staticmethod
    def violence() -> List[Factor]:
        """Violence list method.

        This creates a list of all posible violence.

        Returns: A list of violence.
        """
        violence_factor: List[Factor] = list()
        animalm = Animals()
        violence_factor.append(animalm)
        animall = Animals()
        animall.severity = Severity.LIGHT
        violence_factor.append(animall)
        animals = Animals()
        animals.severity = Severity.SEVERE
        violence_factor.append(animals)
        generalm = General()
        violence_factor.append(generalm)
        generall = General()
        generall.severity = Severity.LIGHT
        violence_factor.append(generall)
        generals = General()
        generals.severity = Severity.SEVERE
        violence_factor.append(generals)
        certainsexm = CertainSex()
        violence_factor.append(certainsexm)
        certainsexl = CertainSex()
        certainsexl.severity = Severity.LIGHT
        violence_factor.append(certainsexl)
        certainsexs = CertainSex()
        certainsexs.severity = Severity.SEVERE
        violence_factor.append(certainsexs)
        return violence_factor

    @staticmethod
    def fulllist() -> List[Factor]:
        """Factor list method.

        This creates a list of all posible Factors.

        Returns: A list of Factors.
        """
        signs = Person.signs()
        experience = Person.experience()
        violence = Person.violence()
        full_person = signs+experience+violence
        return full_person
