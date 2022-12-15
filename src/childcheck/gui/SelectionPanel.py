"""File for the SelectionPanel.

This is the file with the class for the selection panel
which displays all the buttons for the factors.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
import tkinter as tk
from tkinter.ttk import Button
from src.childcheck.data.person.Person import Person
from src.childcheck.gui.PanelFactory import PanelFactory


class SelectionPanel(tk.Frame):
    """Selection panel class.

    Displays all selection factor buttons and accepts arguments
    for changes to attributes.

    Attributes:
        __master: The primary window class.
    """

    def __init__(self, master) -> None:
        """Initiater for the selection panel class.

        This method instantiates the class that displays the
        selection factor buttons.

        Args:
            master: The panel class that instantiates this one.
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_columnconfigure(4, weight=1)

        i = 0
        for sign in Person.signs():
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(0, weight=1)
            button = tk.Button(master=self, text=sign.name,
                               command=lambda x=sign.name:  # type: ignore
                               self.action_performed(x))
            button.grid(row=i, column=0, padx=2, pady=2, sticky="NSEW")
            i += 1

        i = 0
        for violence in Person.violence():
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(1, weight=1)
            button = tk.Button(master=self,
                               text=violence.name+": "+violence.severity,  # type: ignore
                               command=lambda x=violence.name,  # type: ignore
                               y=violence:
                               self.action_performed(x, y))
            button.grid(row=i, column=1, padx=2, pady=2, sticky="NSEW")
            i += 1

        i = 0
        for experience in Person.experience():
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(2, weight=1)
            button = tk.Button(master=self,
                               text=experience.name+": "+experience.severity,  # type: ignore
                               command=lambda x=experience.name,  # type: ignore
                               y=experience:
                               self.action_performed(x, y))
            button.grid(row=i, column=2, padx=2, pady=2, sticky="NSEW")
            i += 1

    def action_performed(self, text: str, factor=None) -> None:
        """Action performed method.

        This method calls on a particular panel selected by a selection user.

        Args:
            text: A shortened string version of the factor's name.
            factor: A predetermined instance of an factor.
        """
        print(text)
        if factor is None:
            panel = PanelFactory()
            self.__master.load_panel(panel.get_panel(self.__master, text))
        else:
            panel = PanelFactory()
            self.__master.load_panel(panel.get_panel(self.__master, factor))
