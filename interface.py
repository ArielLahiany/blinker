# PyQt modules
from PyQt5.QtWidgets import QDialog, QGroupBox, QVBoxLayout, QGridLayout, QHBoxLayout, QApplication, QStyleFactory, \
    QPushButton


class BlinkerController(QDialog):
    """

    """

    def __init__(self, parent=None):
        super(BlinkerController, self).__init__(parent)

        #
        self.activate_group_box()

        #
        self.interface_initializer()

    def interface_initializer(self):
        """

        """

        # Sets the title of the dialog window.
        self.setWindowTitle("Blinker Controller")

        # Sets the style of the dialog window.
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        QApplication.setPalette(QApplication.style().standardPalette())

        top_layout = QHBoxLayout(self)
        top_layout.addStretch(1)

        main_layout = QGridLayout(self)

        main_layout.addLayout(top_layout, 0, 0, 1, 2)

        main_layout.addWidget(self.activate_group_box(), 1, 0)

        return main_layout

    def activate_group_box(self):
        active_group_box = QGroupBox("Activate")

        button = QPushButton("Toggle Push Button")
        button.setCheckable(True)
        # button.setChecked(True)

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addStretch(1)

        active_group_box.setLayout(layout)

        return active_group_box

    def frequency_group_box(self):
        pass

    def bulb_group_box(self):
        pass


if __name__ == '__main__':

    import sys

    red = Color(code="#cc3232", description="Red")

    app = QApplication(sys.argv)
    blinker = BlinkerController()
    blinker.show()
    sys.exit(app.exec_())
