"""Returns instance of GUI panel.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from src.childcheck.gui.signs.WetBedPanel import WetBedPanel
from src.childcheck.gui.signs.ImpulsivityPanel import ImpulsivityPanel
from src.childcheck.gui.signs.AntiSocialPanel import AntiSocialPanel
from src.childcheck.gui.signs.ArsonPanel import ArsonPanel
from src.childcheck.gui.signs.NoEmpathyPanel import NoEmpathyPanel
from src.childcheck.gui.violence.GeneralPanel import GeneralPanel
from src.childcheck.gui.violence.CertainSexPanel import CertainSexPanel
from src.childcheck.gui.violence.AnimalsPanel import AnimalsPanel
from src.childcheck.gui.experience.ExperiencePanel import ExperiencePanel
from src.childcheck.data.person.Factor import Factor
from src.childcheck.data.signs.WetBed import WetBed
from src.childcheck.data.signs.Impulsivity import Impulsivity
from src.childcheck.data.signs.AntiSocial import AntiSocial
from src.childcheck.data.signs.Arson import Arson
from src.childcheck.data.signs.NoEmpathy import NoEmpathy
from src.childcheck.data.violence.General import General
from src.childcheck.data.violence.CertainSex import CertainSex
from src.childcheck.data.violence.Animals import Animals
from src.childcheck.data.experience.Abuse import Abuse
from src.childcheck.data.experience.Trauma import Trauma
from src.childcheck.data.experience.Neglect import Neglect


class PanelFactory():
    """Class for building panels."""

    @staticmethod
    def get_panel(parent, factor, buttons=True):  # type: ignore
        """Returns instance of the panel called on."""
        if isinstance(factor, str):
            if factor == "WetBed":
                panel = WetBedPanel(parent, None, buttons)
            elif factor == "Impulsivity":
                panel = ImpulsivityPanel(parent, None, buttons)
            elif factor == "AntiSocial":
                panel = AntiSocialPanel(parent, None, buttons)
            elif factor == "Arson":
                panel = ArsonPanel(parent, None, buttons)
            elif factor == "NoEmpathy":
                panel = NoEmpathyPanel(parent, None, buttons)
            elif factor == "Abuse":
                panel = ExperiencePanel(parent, Abuse(), buttons)
            elif factor == "Trauma":
                panel = ExperiencePanel(parent, Trauma(), buttons)
            elif factor == "Neglect":
                panel = ExperiencePanel(parent, Neglect(), buttons)
            elif factor == "General":
                panel = GeneralPanel(parent, None, buttons)
            elif factor == "CertainSex":
                panel = CertainSexPanel(parent, None, buttons)
            elif factor == "Animals":
                panel = AnimalsPanel(parent, None, buttons)
            else:
                raise ValueError
            return panel
        elif isinstance(factor, Factor):
            if isinstance(factor, WetBed):
                panel = WetBedPanel(parent, factor, buttons)
            elif isinstance(factor, Impulsivity):
                panel = ImpulsivityPanel(parent, factor, buttons)
            elif isinstance(factor, AntiSocial):
                panel = AntiSocialPanel(parent, factor, buttons)
            elif isinstance(factor, Arson):
                panel = ArsonPanel(parent, factor, buttons)
            elif isinstance(factor, NoEmpathy):
                panel = NoEmpathyPanel(parent, factor, buttons)
            elif isinstance(factor, Abuse):
                panel = ExperiencePanel(parent, factor, buttons)
            elif isinstance(factor, Trauma):
                panel = ExperiencePanel(parent, factor, buttons)
            elif isinstance(factor, Neglect):
                panel = ExperiencePanel(parent, factor, buttons)
            elif isinstance(factor, General):
                panel = GeneralPanel(parent, factor, buttons)
            elif isinstance(factor, CertainSex):
                panel = CertainSexPanel(parent, factor, buttons)
            elif isinstance(factor, Animals):
                panel = AnimalsPanel(parent, factor, buttons)
            else:
                raise ValueError
            return panel
