"""
Main entry point for Blinker application.
"""
# todo: move to here all the main logic.
#       control the logging.
# Python modules
import sys
import logging

# PyQt modules
from PyQt5.QtWidgets import QApplication

# Project modules
from interface import BlinkerController
from models import Color
from client import connect

log = logging.getLogger("__name__")

if __name__ == "__main__":
    # Runs the GUI application.
    application = QApplication(
        sys.argv
    )

    plc = connect(logger=log)
    red = Color(code="#cc3232", description="Red")
    green = Color(code="#2dc937", description="Red")

    # The main window for the blinker controller.
    blinker = BlinkerController(
        logger=log,
        connection=plc,
        color=[
            red,
            # green
        ]
    )
    blinker.show()

    # Defines the exit of the application.
    sys.exit(
        application.exec_()
    )
