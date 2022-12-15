"""File for all experience panels.

This is the file determines how an experience
option will look once one is chosen.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
import tkinter as tk
from tkinter import ttk
import webbrowser
from tkinter.ttk import Button
from src.childcheck.data.enums.Severity import Severity
from src.childcheck.gui.HelpDialog import HelpDialog


class ExperiencePanel(tk.Frame):
    """Experience panel class.

    Displays all the experience choices for a child.

    Attributes:
        _factor: The accepted instance of a factor.
        __master: The primary panel.
    """

    def __init__(self, master, factor, buttons: bool = True) -> None:
        """Initiater for the experience panel class.

        This method instantiates the class that displays the
        experience options.

        Args:
            master: The panel class that instantiates this one.
            factor: A particular instance of this factor.
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)

        self._factor = factor

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        title = tk.Label(master=self, text=self._factor.name)
        title.grid(row=0, column=1, padx=2, pady=2, sticky="SEW")

        self._severity = tk.StringVar(value=str(self._factor.severity))
        severity_combo = ttk.Combobox(master=self,
                                      textvariable=self._severity)
        severity_combo['values'] = [str(x) for x in Severity]
        severity_combo.grid(row=1, column=1, padx=2, pady=2, sticky="W")

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
            self.grid_rowconfigure(1, weight=1)

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
            self._factor.severity = Severity(self._severity.get())
            self.__master.save_factor(self._factor)
            self.__master.load_selection_panel()
        elif text == "cancel":
            self.__master.load_selection_panel()
        elif text == "help":
            dialog = HelpDialog(self.__master, title="Factor Definition",
                                message="Use this link: https://www.dshs.wa.gov/altsa/home-and-community-services/types-and-signs-abuse/",
                                options=["Exit"])
