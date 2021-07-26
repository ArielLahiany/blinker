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
# from widgets import ActivationWidget
from interface import BlinkerController
from models import Color
from client import connect

log = logging.getLogger("__name__")

if __name__ == "__main__":
    # Runs the GUI application.
    application = QApplication(
        sys.argv
    )

    # todo: temp.

    plc = connect(logger=log)
    red = Color(code="#cc3232", description="Red")

    # activation = ActivationWidget(logger=log, connection=plc, color=red)
    # activation.show()
    blinker = BlinkerController()
    blinker.show()

    # Defines the exit of the application.
    sys.exit(
        application.exec_()
    )
