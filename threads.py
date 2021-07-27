# Python modules
import sys

# PyADS modules
from pyads import Connection

# PyQt modules
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject


class BulbMonitor(QThread):

    signal = pyqtSignal(str)

    @pyqtSlot()
    def refresh(self):
        # I'm guessing this is an infinite while loop that monitors files

        while True:
            # if file_has_changed:
                self.signal.emit()


class MyWidget(QtGui.QWidget):

    def __init__(self, ...)
        ...
        self.file_monitor = FileMonitor()
        self.thread = QtCore.QThread(self)
        self.file_monitor.image_signal.connect(self.image_callback)
        self.file_monitor.moveToThread(self.thread)
        self.thread.started.connect(self.file_monitor.monitor_images)
        self.thread.start()

    @QtCore.pyqtSlot(str)
    def image_callback(self, filepath):
        pixmap = QtGui.QPixmap(filepath)
# class BulbThread(QThread):
#     """
#
#     """
#
#     signal = pyqtSignal(bool)
#
#     def __init__(self,
#                  connection: Connection,
#                  status: bool
#                  ):
#         super().__init__()
#
#         self.connection = connection
#         self.status = status
#
#     # def refresh(self):
#     while True:
#         # emit = the thing that the signal retuerns.
#         self.signal.emit(self.status)
