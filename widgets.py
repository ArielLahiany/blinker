# Python modules
from logging import Logger

# PyADS modules
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from pyads import Connection, ADSError

# PyQt modules
from PyQt5.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QPushButton, QLineEdit

# Project modules
from models import Color


class ActivationWidget(QWidget):
    """
    Activation button initialization widget.
    """

    def __init__(
            self,
            logger: Logger,
            connection: Connection,
            color: Color,
            status: bool = None,
            group: QGroupBox = None,
            layout: QVBoxLayout = None,
            button: QPushButton = None,
            parent=None
    ):
        """
        :param logger:
        :param connection:
        :param color:
        :param status:
        :param group:
        :param layout:
        :param button:
        :param parent:
        """

        super(ActivationWidget, self).__init__(parent)

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

        self.group.setTitle("Activation")
        self.group.setGeometry(0, 0, 125, 100)
        self.layout.addWidget(self.button)
        self.group.setLayout(self.layout)
        return self.group

    def state(self) -> bool:
        """
        A base function that reads the initial state of each LED bulb.
        :return: Boolean object.
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

        # Updated the bulb status.
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
        :return: QPushButton object.
        """

        self.button.setCheckable(True)
        self.button.setChecked(self.status)
        self.button.clicked.connect(self.listener)
        return self.button


class FrequencyWidget(QWidget):
    """"
    Frequency input box initialization widget.
    """

    def __init__(
            self,
            logger: Logger,
            connection: Connection,
            color: Color,
            frequency: int = None,
            group: QGroupBox = None,
            layout: QVBoxLayout = None,
            line: QLineEdit = None,
            parent=None
    ):
        """

        :param logger:
        :param connection:
        :param color:
        :param frequency:
        :param group:
        :param layout:
        :param line:
        :param parent:
        """

        super(FrequencyWidget, self).__init__(parent)

        self.logger = logger
        self.connection = connection
        self.color = color

        self.frequency = self.state() if frequency is None else frequency
        self.group = QGroupBox(self) if group is None else group
        self.layout = QVBoxLayout(self) if layout is None else layout
        self.line = QLineEdit("Frequency") if line is None else line

        self.controller()
        self.interface()

    def interface(self) -> QGroupBox:
        """
        A base function that defines the graphical user interface of the group.
        :return: QGroupBox object.
        """

        self.group.setTitle("Frequency")
        self.group.setGeometry(0, 0, 125, 100)
        self.layout.addWidget(self.line)
        self.group.setLayout(self.layout)
        return self.group

    def state(self) -> int:
        """
        A base function that reads the initial frequency value of each LED bulb.
        :return: Integer object.
        """

        try:
            frequency = self.connection.read_by_name(
                "MAIN.{}Frequency".format(self.color.description)
            )
        except ADSError as e:
            self.logger.error(
                msg="ADS error: {}".format(e)
            )
        else:
            return frequency

    def listener(self) -> None:
        """
        A base function that act as changes listener for the frequency input box
        of each LED bulb.
        :return: None.
        """

        try:
            self.connection.write_by_name(
                "MAIN.{}Frequency".format(self.color.description),
                int(self.line.text())
            )
        except ADSError as e:
            self.logger.error(
                msg="ADS error: {}.".format(e)
            )
        else:
            self.logger.info(
                msg="Frequency value has changed successfully."
            )

    def controller(self) -> QLineEdit:
        """
        A base function that controls the frequency of each LED bulb.
        :return: QLineEdit object.
        """

        # Sets bulb frequency validation.
        # todo: validate better.
        validator = QRegExpValidator(QRegExp("[0-9]*"))

        self.line.setValidator(validator)
        self.line.setText(str(self.frequency))
        self.line.editingFinished.connect(self.listener)
        return self.line


class Bulb(QWidget):
    # todo: consider doing by radio checkbox.
    pass
