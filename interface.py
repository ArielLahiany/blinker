# Python modules
from logging import Logger

# PyQt modules
from PyQt5.QtWidgets import QDialog, QGridLayout, QApplication, QStyleFactory

# PyADS modules
from pyads import Connection

# Project modules
from client import connect
from models import Color
from widgets import ActivationWidget, FrequencyWidget

# todo: remove.
import logging

# log = logging.getLogger("__name__")
#
# plc = connect(logger=log)
red = Color(code="#cc3232", description="Red")


class BlinkerController(QDialog):
    """

    """

    def __init__(
            self,
            # todo: add logging etc.
            logger: Logger,
            connection: Connection,
            color: [Color],
            pallet: QApplication.palette = None,
            grid: QGridLayout = None,
            parent=None
    ):
        super(BlinkerController, self).__init__(parent)

        self.logger = logger
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

        self.setWindowTitle("Blinker Controller")
        self.setLayout(self.grid)

        width: int = 425
        height: int = 125 * len(self.color)
        self.setFixedSize(width, height)

        QApplication.setStyle(QStyleFactory.create("Fusion"))
        QApplication.setPalette(QApplication.style().standardPalette())

        activation = ActivationWidget(
            logger=self.logger,
            connection=self.connection,
            color=red
        )
        frequency = FrequencyWidget(
            logger=self.logger,
            connection=self.connection,
            color=red
        )
        temp_widget = ActivationWidget(
            logger=self.logger,
            connection=self.connection,
            color=red
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
