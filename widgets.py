# Python modules
from logging import Logger

# PyADS modules
from pyads import Connection, ADSError

# PyQt modules
from PyQt5.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QPushButton

# Project modules
from models import Color


class Activation(QWidget):
    """
    Activation button initialization widget.
    """

    def __init__(self,
                 logger: Logger,
                 connection: Connection,
                 color: Color,
                 status: bool = None,
                 group: QGroupBox = None,
                 layout: QVBoxLayout = None,
                 button: QPushButton = None,
                 parent=None):
        super(Activation, self).__init__(parent)

        self.logger = logger
        self.connection = connection
        self.color = color

        self.status = self.state() if status is None else status
        self.group = QGroupBox(self) if group is None else group
        self.layout = QVBoxLayout(self) if layout is None else layout
        self.button = QPushButton("Activate") if button is None else button

        self.controller()
        self.interface()

    def interface(self) -> QGroupBox:
        """
        A base function that defines the graphical user interface of the group.
        :return: QGroupBox object.
        """

        self.group.setTitle(self.__class__.__name__)
        self.group.setGeometry(0, 0, 125, 100)
        self.layout.addWidget(self.button)
        self.group.setLayout(self.layout)
        return self.group

    def state(self) -> bool:
        """
        A base function that reads the initial state of each LED bulb.
        :return: QLineEdit object.
        """

        try:
            status = self.connection.read_by_name(
                "MAIN.Active"
            )
        except ADSError as e:
            self.logger.error(
                msg="ADS error: {}".format(e)
            )
        else:
            return status

    def listener(self) -> None:
        """
        A base function that act as changes listener for the activation button
        of each LED bulb.
        :return: None.
        """

        # Updates.
        self.status = not self.status

        try:
            self.connection.write_by_name(
                "MAIN.Active",
                self.status
            )
        except ADSError as e:
            self.logger.error(
                msg="ADS error: {}.".format(e)
            )
        else:
            self.logger.info(
                msg="Activation status has changed successfully."
            )

    def controller(self) -> QPushButton:
        """
        A base function that controls the activation of each LED bulb.
        :return: QLineEdit object.
        """

        self.button.setCheckable(True)
        self.button.setChecked(self.status)
        self.button.clicked.connect(self.listener)
        return self.button


class Frequency(QWidget):
    pass


class Bulb(QWidget):
    # todo: consider doing by radio checkbox.
    pass
