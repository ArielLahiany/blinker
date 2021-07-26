# PyQt modules
import logging

from PyQt5.QtWidgets import QDialog, QGroupBox, QVBoxLayout, QGridLayout, QHBoxLayout, QApplication, QStyleFactory, \
    QPushButton

from client import connect
from models import Color
from widgets import ActivationWidget, FrequencyWidget

log = logging.getLogger("__name__")

plc = connect(logger=log)
red = Color(code="#cc3232", description="Red")


class BlinkerController(QDialog):
    """

    """

    def __init__(
            self,
            # todo: add logging etc.
            pallet: QApplication.palette = None,
            grid: QGridLayout = None,
            parent=None
    ):
        super(BlinkerController, self).__init__(parent)

        self.palette = QApplication.palette() if pallet is None else pallet
        self.grid = QGridLayout(self) if grid is None else grid

        self.interface()

    def interface(self) -> None:
        """

        """

        self.setWindowTitle("Blinker Controller")
        self.setLayout(self.grid)
        self.setFixedSize(425, 125)

        QApplication.setStyle(QStyleFactory.create("Fusion"))
        QApplication.setPalette(QApplication.style().standardPalette())

        activation = ActivationWidget(logger=log, connection=plc, color=red)
        frequency = FrequencyWidget(logger=log, connection=plc, color=red)
        temp_widget = ActivationWidget(logger=log, connection=plc, color=red)

        widgets = [
            activation,
            frequency,
            temp_widget
        ]

        positions = [
            (i, j) for i in range(1) for j in range(len(widgets))
        ]

        for position, widget in zip(positions, widgets):
            self.grid.addWidget(widget, *position)
