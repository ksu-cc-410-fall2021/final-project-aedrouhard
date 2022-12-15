"""File for the ResultsDialog.

This is the file with the class for the Results dialog,
which asks if the results should be saved.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
from tkinter import Button, Label
from tkinter.simpledialog import Dialog  # type: ignore
from typing import List, Optional


class ResultsDialog(Dialog):
    """Class for the Results dialog."""

    def __init__(self, master, title: str = "Results",
                 message: str = "Select an option",
                 options: List[str] = ["Yes", "No"]) -> None:
        """Initiater."""
        self.__message = message
        self.__options = options
        self.result: Optional[str] = None
        super().__init__(master, title)

    def body(self, master) -> None:
        """Body of dialog."""
        message = Label(master=master, text=self.__message)
        message.grid(row=0, column=0, columnspan=len(self.__options),
                     padx=2, pady=2, sticky="EW")
        i: int = 0
        for option in self.__options:
            button = Button(master=master, text=option,
                            command=lambda x=option:  # type: ignore
                            self.action_performed(x))
            button.grid(row=1, column=i, padx=2, pady=2, sticky="EW")
            i += 1

    def buttonbox(self) -> None:
        """Passed method."""
        pass

    def action_performed(self, text: str) -> None:
        """Handles outcome."""
        self.result = text
        self.destroy()
