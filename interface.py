"""
Manages the required main Graphical User Interface dialog box.
"""

# Python modules
import logging

# PyQt modules
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QGridLayout,
    QStyleFactory
)

# PyADS modules
from pyads import Connection

# Project modules
from models import Color
from widgets import ActivationWidget, FrequencyWidget


class BlinkerController(QDialog):
    """
    Blinker controller initialization widget.
    """

    def __init__(
            self,
            connection: Connection,
            color: [Color],
            pallet: QApplication.palette = None,
            grid: QGridLayout = None,
            parent=None
    ):
        super(BlinkerController, self).__init__(parent)

        self.connection = connection
        self.color = color

        self.palette = QApplication.palette() if pallet is None else pallet
        self.grid = QGridLayout(self) if grid is None else grid

        self.interface()

    def interface(self) -> None:
        """
        A base function that defines the main graphical user interface
        of the blinker controller.
        :return: None.
        """

        logging.info(
            msg="Initializing the main Graphical User Interface for the blinker application."
        )

        self.setWindowTitle("Blinker Controller")
        self.setLayout(self.grid)

        width: int = 425
        height: int = 125 * len(self.color)
        self.setFixedSize(width, height)

        QApplication.setStyle(QStyleFactory.create("Fusion"))
        QApplication.setPalette(QApplication.style().standardPalette())

        activation = ActivationWidget(
            connection=self.connection,
            color=self.color[0]
        )
        frequency = FrequencyWidget(
            connection=self.connection,
            color=self.color[0]
        )
        temp_widget = ActivationWidget(
            connection=self.connection,
            color=self.color[0]
        )

        # todo: loop for dynamic rows.
        widgets = [
            activation,
            frequency,
            temp_widget
        ]

        positions = [
            (i, j) for i in range(len(self.color)) for j in range(len(widgets))
        ]

        for position, widget in zip(positions, widgets):
            self.grid.addWidget(widget, *position)
