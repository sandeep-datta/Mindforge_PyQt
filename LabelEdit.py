from PyQt5 import QtWidgets
from PyQt5.QtGui import QKeyEvent, QTextFormat

from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt

class LabelEdit(QLabel):

    def __init__(self, text):
        super().__init__(text)
        self.setTextFormat(Qt.PlainText)
        self.label.setStyleSheet("border: 1px solid red")
        self.label.setMaximumWidth(600)
        self.label.setWordWrap(True)

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Return:
            self.editAccepted.emit()
            e.accept()
        elif e.key() == Qt.Key_Escape:
            self.editRejected.emit()
            e.accept()
        else:
            super().keyPressEvent(e)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    txt = LabelEdit("Hello world!")

    vbox = QVBoxLayout()
    vbox.addStretch()
    vbox.addWidget(txt)
    vbox.addStretch()

    hbox = QHBoxLayout()
    hbox.addStretch()
    hbox.addLayout(vbox)
    hbox.addStretch()

    w = QWidget()
    w.setLayout(hbox)
    w.show()

    sys.exit(app.exec_())