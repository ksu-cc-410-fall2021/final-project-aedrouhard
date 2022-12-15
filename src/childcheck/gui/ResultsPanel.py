"""File for the ResultsPanel.

This is the file with the class for the Results panel
which displays an Results and associated values.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview, Scrollbar, Frame, Button
from typing import Dict
from src.childcheck.data.person.Factor import Factor
from src.childcheck.gui.PanelFactory import PanelFactory
from src.childcheck.data.results.Results import Results
from src.childcheck.gui.ResultsDialog import ResultsDialog
from cc410.register.ReceiptPrinter import ReceiptPrinter
from src.childcheck.data.experience.Abuse import Abuse
from src.childcheck.data.experience.Trauma import Trauma
from src.childcheck.data.signs.Arson import Arson
from src.childcheck.data.signs.NoEmpathy import NoEmpathy
from src.childcheck.data.signs.WetBed import WetBed
from src.childcheck.data.signs.Impulsivity import Impulsivity
from src.childcheck.data.signs.AntiSocial import AntiSocial
from src.childcheck.data.violence.Animals import Animals
from src.childcheck.data.violence.General import General
from src.childcheck.data.violence.CertainSex import CertainSex


class ResultsPanel(tk.Frame):
    """Results panel class.

    Organizes the information related to the Results.

    Args:
        __master: The primary panel.
    """

    def __init__(self, master) -> None:
        """Initiater for the Results panel class.

        This method instantiates the class that displays the
        Results information.

        Args:
            master: The panel class that instantiates this one.
        """
        self.__master = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.__results: Results = Results()

        results_label = tk.Label(master=self, text="Results #")
        results_label.grid(row=0, column=0, padx=2, pady=2, sticky="E")

        self.__results_num = tk.Label(master=self,
                                      text="{}".format(self.__results.results_num))
        self.__results_num.grid(row=0, column=1, padx=2, pady=2, sticky="W")

        self.__factors: Dict[str, Factor] = dict()
        list_frame = Frame(master=self)
        list_frame.grid_columnconfigure(0, weight=1)
        list_frame.grid_rowconfigure(0, weight=1)
        self.__results_list = Treeview(master=list_frame, show="tree",
                                       selectmode="browse")
        results_list_scrollbar = Scrollbar(master=list_frame, orient="vertical",
                                           command=self.__results_list.yview)
        self.__results_list.configure(yscrollcommand=results_list_scrollbar.set)
        self.__results_list.grid(row=0, column=0, sticky="NSEW")
        results_list_scrollbar.grid(row=0, column=1, sticky="NSE")
        list_frame.grid(row=1, column=0, columnspan=2, sticky="NSEW")

        edit_button = tk.Button(master=self, text="Edit",
                                command=lambda:  # type: ignore
                                self.action_performed("edit"))
        edit_button.grid(row=2, column=0, columnspan=1, padx=2,
                         pady=2, sticky="NSEW")

        delete_button = Button(master=self, text="Delete",
                               command=lambda:  # type: ignore
                               self.action_performed("delete"))
        delete_button.grid(row=2, column=1, columnspan=1, padx=2,
                           pady=2, sticky="NSEW")

        total = tk.Label(master=self, text="Total Score:")
        total.grid(row=3, column=0, padx=2, pady=2, sticky="E")

        self.__total = self.__results.total
        self.__total_num = tk.Label(master=self, text=self.__total)
        self.__total_num.grid(row=3, column=1, padx=2, pady=2, sticky="W")

        new_button = Button(master=self, text="New Results",
                            command=lambda:  # type: ignore
                            self.action_performed("new"))
        new_button.grid(row=4, column=0, columnspan=1, padx=2,
                        pady=2, sticky="NSEW")

        submit_button = Button(master=self, text="Submit",
                               command=lambda:  # type: ignore
                               self.action_performed("submit"))
        submit_button.grid(row=4, column=1, columnspan=1, padx=2,
                           pady=2, sticky="NSEW")

    def action_performed(self, text: str) -> None:
        """Handle button actions."""
        print(text)
        if text == "edit":
            node = self.__results_list.focus()
            if node:
                while node not in self.__factors:
                    node = self.__results_list.parent(node)
                factor: Factor = self.__factors[node]
                self.__results.remove_factor(factor)
                panel = PanelFactory()
                self.__master.load_panel(panel.get_panel(self.__master,
                                                         factor))

        elif text == "delete":
            node = self.__results_list.focus()
            if node:
                while node not in self.__factors:
                    node = self.__results_list.parent(node)
                self.__results.remove_factor(self.__factors[node])
                del self.__factors[node]
                self.__results_list.delete(node)
                self.__total_num['text'] = self.__results.total

        elif text == "new":
            self.__results = Results()
            self.__results_num['text'] = self.__results.results_num
            self.__factors = dict()
            for node in self.__results_list.get_children():
                self.__results_list.delete(node)
            self.__total_num['text'] = self.__results.total

        elif text == "submit":
            dialog = ResultsDialog(self.__master, title="Submit",
                                   message="Submit Results?",
                                   options=["Yes", "No"])
            if dialog.result == "Yes":
                test_results = ReceiptPrinter()
                test_results.start_receipt()
                test_results.print_line("Results Number: {}".format(self.__results.results_num-1))
                for thing in self.__results:
                    test_results.print_line("\n")
                    test_results.print_line(thing.name)
                    for x in thing.notes:
                        test_results.print_line("    " + x)
                    test_results.print_line("Score: " + str(thing.score))
                test_results.print_line("\nTotal Offender Score: {}\n".format(self.__results.total))
                s = 0
                v = 0
                m = 0
                for factor in self.__results:
                    if isinstance(factor, Abuse):
                        s += 10
                        m += 10
                    elif isinstance(factor, AntiSocial):
                        s += 20
                        m += 20
                    elif isinstance(factor, Impulsivity):
                        s += 15
                        v += 15
                    elif isinstance(factor, General):
                        if factor.sexual:
                            s += 17
                        if factor.physical:
                            v += 17
                            m += 17
                        if factor.verbal:
                            v += 17
                    elif isinstance(factor, WetBed):
                        s += 30
                        m += 30
                    elif isinstance(factor, Trauma):
                        v += 5
                    elif isinstance(factor, Arson):
                        v += 25
                    elif isinstance(factor, Animals):
                        m += 25
                    elif isinstance(factor, NoEmpathy):
                        s += 30
                        m += 30
                    elif isinstance(factor, CertainSex):
                        s += 17
                test_results.print_line("\nTotal Sex Offender Score: {} / 122\n".format(s))
                test_results.print_line("\nTotal Violent Offender Score: {} / 79\n".format(v))
                test_results.print_line("\nTotal Murderer Score: {} / 132\n".format(m))

                if int(self.__results.total) <= 89:
                    test_results.print_line("Low probability of becoming an offender")
                elif 89 < int(self.__results.total) <= 178:
                    test_results.print_line("High probability of becoming an offender")
                elif 178 < int(self.__results.total) <= 267:
                    test_results.print_line("Very high probability of becoming an offender")
                if int(self.__results.total) > 89:
                    if s > v:
                        if s > m:
                            test_results.print_line("Most likely crime: sex offender")
                        else:
                            test_results.print_line("Most likely crime: murderer")
                    else:
                        if v > m:
                            test_results.print_line("Most likely crime: violent offender")
                        else:
                            test_results.print_line("Most likely crime: murderer")

                test_results.end_receipt()
                test_results.close()

    def save_factor(self, factor: Factor) -> None:
        """Method to save Factor."""
        for factor_id, value in self.__factors.items():
            if factor is value:
                self.__update_tree(factor, factor_id)
                self.__results.add_factor(factor)
                self.__total_num['text'] = self.__results.total
                return
        self.__factors[self.__update_tree(factor)] = factor
        self.__results.add_factor(factor)
        self.__total_num['text'] = self.__results.total

    def __update_tree(self, factor: Factor, index: str = "end") -> str:
        """Private method to update tree."""
        if index == "end":
            index = self.__results_list.insert(parent="", index="end",
                                               text=str(factor))
        else:
            self.__results_list.item(index, text=str(factor))
            for child in self.__results_list.get_children(index):
                self.__results_list.delete(child)
        self.__results_list.item(index, open=True)
        for line in factor.notes:
            self.__results_list.insert(parent=index, index="end",
                                       text=line)
        return index
