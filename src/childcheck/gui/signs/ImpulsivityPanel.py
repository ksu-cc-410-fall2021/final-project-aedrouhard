"""File for the Impulsivity panel.

This is the file determines how the
panel will look for the Impulsivity sign.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Button
from src.childcheck.data.signs.Impulsivity import Impulsivity
from src.childcheck.gui.FactorPanel import FactorPanel
from src.childcheck.gui.HelpDialog import HelpDialog


class ImpulsivityPanel(FactorPanel):
    """Impulsivity panel class.

    Displays all the ordering choices for this particular
    Factor.

    Attributes:
        _factor: The accepted instance of an Factor.
        __master: The primary panel.
    """

    def __init__(self, master, factor=None,
                 buttons: bool = True) -> None:
        """Initiater for the Impulsivity panel class.

        This method instantiates the class that displays the
        menu Factor options.

        Args:
            master: The panel class that instantiates this one.
            factor: A particular instance of this Factor.
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)

        if factor is None:
            self._factor = Impulsivity()
        else:
            self._factor = factor

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        title = tk.Label(master=self, text="Impulsivity")
        title.grid(row=0, column=1, padx=2, pady=2, sticky="SEW")

        self._frequent = tk.BooleanVar(value=bool
                                       (self._factor.frequent))
        frequent = tk.Checkbutton(master=self, text="Frequent",
                                  variable=self._frequent, onvalue=True,
                                  offvalue=False)
        frequent.grid(row=1, column=1, padx=2, pady=2, sticky="W")

        if buttons:
            save = Button(master=self, text="Save",
                          command=lambda:  # type: ignore
                          self.action_performed("save"))
            save.grid(row=2, column=1, sticky="EW")

            self.grid_rowconfigure(3, weight=1)
            cancel = Button(master=self, text="Cancel",
                            command=lambda:  # type: ignore
                            self.action_performed("cancel"))
            cancel.grid(row=3, column=1, sticky="NEW")
        else:
            self.grid_rowconfigure(2, weight=1)
        link = Button(master=self, text="Factor Definition",
                      command=lambda:  # type: ignore
                      self.action_performed("help"))
        link.grid(row=3, column=1, sticky="S")

    def action_performed(self, text):
        """Action performed method.

        This method loads up the selection panel after saving edits.

        Args:
            text: A string that indicates data must be saved.
        """
        print(text)
        if text == "save":
            self._factor.frequent = self._frequent.get()
            self.__master.save_factor(self._factor)
            self.__master.load_selection_panel()
        elif text == "cancel":
            self.__master.load_selection_panel()
        elif text == "help":
            dialog = HelpDialog(self.__master, title="Factor Definition",
                                message="Use this link: https://www.understood.org/en/articles/understanding-impulsivity/",
                                options=["Exit"])
