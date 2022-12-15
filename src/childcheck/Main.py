"""Main Class.

Author: Allison Drouhard aedrouhard@ksu.edu
Version: 0.1
"""

from typing import List
from src.childcheck.gui.PrimaryWindow import PrimaryWindow


class Main:
    """Main Class."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Main method."""
        PrimaryWindow().mainloop()
