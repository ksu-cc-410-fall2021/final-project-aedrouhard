"""File for the FactorPanel.

This is the file with the class for the factor panel
which allows me to direct other panels here when empty.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from tkinter import Frame


class FactorPanel(Frame):
    """Class for FactorPanel."""

    def __init__(self, master) -> None:
        """Initiater."""
        Frame.__init__(self, master=master)

    def action_performed(self, text: str) -> None:
        """Passed method."""
        pass
