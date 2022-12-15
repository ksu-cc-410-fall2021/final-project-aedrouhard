"""File for the General panel.

This is the file determines how the general
violence panel will look once specified.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Button
from src.childcheck.data.enums.Severity import Severity
from src.childcheck.data.violence.General import General
from src.childcheck.gui.FactorPanel import FactorPanel
from src.childcheck.gui.HelpDialog import HelpDialog


class GeneralPanel(FactorPanel):
    """General panel class.

    Displays all the choices for this particular
    Factor.

    Attributes:
        _factor: The accepted instance of a Factor.
        __master: The primary panel.
    """

    def __init__(self, master, factor=None,
                 buttons: bool = True) -> None:
        """Initiater for the General panel class.

        This method instantiates the class that displays the
        Factor options.

        Args:
            master: The panel class that instantiates this one.
            factor: A particular instance of this Factor.
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)

        if factor is None:
            self._factor = General()
        else:
            self._factor = factor

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        title = tk.Label(master=self, text="General Violence")
        title.grid(row=0, column=1, padx=2, pady=2, sticky="SEW")

        self._severity = tk.StringVar(value=str(self._factor.severity))
        severity_combo = ttk.Combobox(master=self,
                                      textvariable=self._severity)
        severity_combo['values'] = [str(x) for x in Severity]
        severity_combo.grid(row=1, column=1, padx=2, pady=2, sticky="W")

        self._physical = tk.BooleanVar(value=bool
                                       (self._factor.physical))
        physical = tk.Checkbutton(master=self, text="Physical",
                                  variable=self._physical, onvalue=True,
                                  offvalue=False)
        physical.grid(row=2, column=1, padx=2, pady=2, sticky="W")

        self._verbal = tk.BooleanVar(value=bool
                                     (self._factor.verbal))
        verbal = tk.Checkbutton(master=self, text="Verbal",
                                variable=self._verbal, onvalue=True,
                                offvalue=False)
        verbal.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        self._sexual = tk.BooleanVar(value=bool(self._factor.sexual))
        sexual = tk.Checkbutton(master=self, text="Sexual",
                                variable=self._sexual, onvalue=True,
                                offvalue=False)
        sexual.grid(row=4, column=1, padx=2, pady=2, sticky="W")

        if buttons:
            save = Button(master=self, text="Save",
                          command=lambda:  # type: ignore
                          self.action_performed("save"))
            save.grid(row=5, column=1, sticky="EW")

            self.grid_rowconfigure(6, weight=1)

            cancel = Button(master=self, text="Cancel",
                            command=lambda:  # type: ignore
                            self.action_performed("cancel"))
            cancel.grid(row=6, column=1, sticky="NEW")
        else:
            self.grid_rowconfigure(5, weight=1)
        link = Button(master=self, text="Factor Definition",
                      command=lambda:  # type: ignore
                      self.action_performed("help"))
        link.grid(row=7, column=1, sticky="S")

    def action_performed(self, text):
        """Action performed method.

        This method loads up the selection panel after saving edits.

        Args:
            text: A string that indicates data must be acted upon.
        """
        print(text)
        if text == "save":
            self._factor.severity = Severity(self._severity.get())
            self._factor.physical = self._physical.get()
            self._factor.verbal = self._verbal.get()
            self._factor.sexual = self._sexual.get()
            self.__master.save_factor(self._factor)
            self.__master.load_selection_panel()
        elif text == "cancel":
            self.__master.load_selection_panel()
        elif text == "help":
            dialog = HelpDialog(self.__master, title="Factor Definition",
                                message="Use this link: https://www.aacap.org/AACAP/Families_and_Youth/Facts_for_Families/FFF-Guide/Understanding-Violent-Behavior-In-Children-and-Adolescents-055.aspx/",
                                options=["Exit"])
