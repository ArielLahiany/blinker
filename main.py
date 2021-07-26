"""
Main entry point for Blinker application.
"""
# Python modules
import os
import sys
import logging
import logging.config

# PyQt modules
from PyQt5.QtWidgets import QApplication

# Project modules
from interface import BlinkerController
from models import Color
from client import connect


# Logging configuration.
def logging_controller():
    if not os.path.exists("logs/"):
        os.makedirs("logs/")
    logging.config.fileConfig("logging.conf")


if __name__ == "__main__":

    # Runs the logging controller for the entire project.
    logging_controller()

    # Connects to the TwinCAT backend server.
    plc = connect()

    # Defines colors for the LED bulbs.
    red = Color(code="#cc3232", description="Red")
    green = Color(code="#2dc937", description="Red")

    # Runs the GUI application.
    application = QApplication(
        sys.argv
    )

    # The main window for the blinker controller.
    blinker = BlinkerController(
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
