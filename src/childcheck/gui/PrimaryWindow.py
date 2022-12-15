"""File for the PrimaryWindow.

This is the file with the class for the primary panel
which calls on the other main panels to instantiate.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
import tkinter as tk
from src.childcheck.gui.ResultsPanel import ResultsPanel
from src.childcheck.gui.SelectionPanel import SelectionPanel
from src.childcheck.data.person.Factor import Factor
from src.childcheck.gui.ParentPanel import ParentPanel


class PrimaryWindow(tk.Tk, ParentPanel):
    """Primary panel class.

    Calls upon the other main panels to appear as indicated.
    """

    def __init__(self) -> None:
        """Initiater for the primary panel class.

        This method creates the title shown in the primary panel
        and instantiates the Results panel.

        Args:
            __main: An attribute checked later, set to None.
            __results: An instance of a selection panel.
        """
        tk.Tk.__init__(self)
        self.minsize(width=1024, height=740)
        self.title("ChildCheck")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(0, weight=2)

        self.__main = None
        self.load_selection_panel()

        self.__results = ResultsPanel(self)
        self.__results.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")

    def load_selection_panel(self):
        """Method for loading the selection panel.

        This method will load a selection panel when called upon.
        """
        self.load_panel(SelectionPanel(self))

    def load_panel(self, panel):
        """Method for loading general panels.

        This method accepts panels to load.

        Args:
            panel: The panel that will be loaded.
        """
        if self.__main is not None:
            self.__main.destroy()
        self.__main = panel
        self.__main.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

    def save_factor(self, factor: Factor) -> None:
        """Method for saving a factor."""
        self.__results.save_factor(factor)
