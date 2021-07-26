from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QStyleFactory,
    QVBoxLayout, QFormLayout
)
from PyQt5.QtCore import Qt

# Project modules
from widgets import Activation
from models import Color
from client import connect

# PyADS modules
from pyads import Connection
import logging

log = logging.getLogger("__name__")


class Blinker(QDialog):
    def __init__(self, parent=None):
        super(Blinker, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        self.bulb_box()
        self.activate_box()
        self.frequency_box()

        grid = QGridLayout()
        self.setLayout(grid)

        # that is correct. box for main button.
        plc = connect(logger=log)
        red = Color(code="#cc3232", description="Red")

        self.activation = Activation(logger=log, connection=plc, color=red)
        self.activation2 = Activation(logger=log, connection=plc, color=red)
        self.activation3 = Activation(logger=log, connection=plc, color=red)

        widgets = [
            self.activation,
            self.activation2,
            self.activation3
        ]

        positions = [(i, j) for i in range(1) for j in range(len(widgets))]

        for position, widget in zip(positions, widgets):
            grid.addWidget(widget, *position)

        self.setFixedSize(425, 125)

        self.setWindowTitle("Blinker Controller")
        self.changeStyle('Fusion')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        QApplication.setPalette(QApplication.style().standardPalette())

    def activate_box(self) -> QGroupBox:
        """
        Activate button.
        """

        group = QGroupBox("Activate")
        # print(group.title)
        layout = QVBoxLayout()

        button = QPushButton("Activate")
        button.setCheckable(True)

        # todo: get the initial data from the server.
        # togglePushButton.setChecked(True)

        layout.addWidget(button)
        layout.addStretch(1)
        group.setLayout(layout)

        return group

    def frequency_box(self) -> QGroupBox:
        """
        Frequency Input box.
        """

        group = QGroupBox("Frequency Input")
        layout = QGridLayout()

        input = QLineEdit('s3cRe7')

        layout.addWidget(input, 0, 0, 1, 2)
        layout.setRowStretch(5, 1)
        group.setLayout(layout)

        return group

    def bulb_box(self):
        """
        """

        group = QGroupBox("Bulb")
        layout = QVBoxLayout()
        # self.topLeftGroupBox = QGroupBox("Group 1")

        radioButton1 = QRadioButton("Radio button 1")

        layout.addWidget(radioButton1)

        layout.addStretch(1)
        group.setLayout(layout)

        return group


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    blinker = Blinker()
    blinker.show()
    sys.exit(app.exec_())
